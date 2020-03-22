from app import db
from app.api import bp
from flask import jsonify, request, abort

from app.models import Question, QuestionSchema, Answer, AnswerSchema, QuesAnswerSchema

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)

question_ans_schema = QuesAnswerSchema()  # Nested Schema of Question Schema with Answer Schema
ques_ans_schema = QuesAnswerSchema(many=True)


@bp.route("/questions", methods=['GET'])
@bp.route("/questions/<int:page>", methods=['GET'])
def get_questions(page=1):
    per_page = 15
    orderby = request.args.get('orderby')
    questions = []
    paginate_obj = None
    if orderby == "views":
        paginate_obj = Question.query.order_by(Question.ViewCount.desc()).paginate(page, per_page,
                                                                                   error_out=False)
        questions = paginate_obj.items
    if orderby == "score":
        paginate_obj = Question.query.order_by(Question.Score.desc()).paginate(page, per_page,
                                                                               error_out=False)
        questions = paginate_obj.items
    if orderby != "views" and "score":
        paginate_obj = Question.query.order_by(Question.CreationDate.desc()).paginate(page, per_page,
                                                                                      error_out=False)
        questions = paginate_obj.items
    if len(questions) == 0:
        abort(404, description='Page not found')
    result = questions_schema.dump(questions)
    total_pages = paginate_obj.pages
    total_pages = {
        'total_pages': total_pages
    }
    result.insert(0, total_pages)
    return jsonify(result)


@bp.route("/question/<int:question_id>", methods=['GET'])
def question_details(question_id):
    question = Question.query.filter_by(Id=question_id).first()
    if question is None:
        abort(404, description="Resource not found")
    return jsonify(question_ans_schema.dump(question))


@bp.route("/search_q", methods=['GET'])
def search_q():
    search_term = request.args.get('q')
    search_term = f"%{search_term}%"
    questions = Question.query.filter((Question.Body.like(search_term)) | Question.Title.like(search_term)).all()
    print(questions)
    return jsonify(ques_ans_schema.dump(questions))


@bp.route("/search_a", methods=['GET'])
def search_a():
    search_term = request.args.get('q')
    search_term = f"%{search_term}%"
    answers = Answer.query.filter(Answer.Body.like(search_term)).all()
    print(answers)
    response = []
    for answer in answers:
        if answer.question is not None:  # some answers in xml file didn't had a question for them
            dump = question_ans_schema.dump(answer.question)
            response.append(dump)
    return jsonify(response)


@bp.errorhandler(404)
def resource_not_found(error):
    return jsonify(error=str(error)), 404


@bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify(error=str(error)), 500
