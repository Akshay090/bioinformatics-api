from app import db, ma


class Answer(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    ParentId = db.Column(db.Integer, db.ForeignKey('question.Id'), nullable=False)
    CreationDate = db.Column(db.DateTime)
    Score = db.Column(db.Integer)
    Body = db.Column(db.Text, index=True)
    OwnerUserId = db.Column(db.Integer)
    LastActivityDate = db.Column(db.DateTime)
    CommentCount = db.Column(db.Integer)


class AnswerSchema(ma.ModelSchema):
    class Meta:
        model = Answer


class Question(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    AcceptedAnswerId = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    Score = db.Column(db.Integer)
    ViewCount = db.Column(db.Integer)
    Body = db.Column(db.Text, index=True)
    OwnerUserId = db.Column(db.Integer)
    LastActivityDate = db.Column(db.DateTime)
    Title = db.Column(db.Text, index=True)
    Tags = db.Column(db.Text, index=True)
    AnswerCount = db.Column(db.Integer)
    CommentCount = db.Column(db.Integer)
    answers = db.relationship('Answer', backref='question', lazy=True)


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question


class QuesAnswerSchema(ma.ModelSchema):
    answers = ma.Nested(AnswerSchema, many=True)

    class Meta:
        model = Question
