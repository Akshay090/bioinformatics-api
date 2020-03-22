import os
from lxml import etree as ET
from datetime import datetime
from app.models import Question, Answer


def populate_db(db, rel_path):
    """
    Populate db with data from bioinformatics_posts_se.xml.
    :param str rel_path: Relative path of xml file to project root
    :param db: database obj
    :Example:
    rel_path = "app/bioinformatics_posts_se.xml"
    """
    populate_questions(db, rel_path)
    populate_answers(db, rel_path)
    db.session.commit()


def populate_questions(db, rel_path):
    """Populate db with questions from xml file.
    :param db: database obj
    :param str rel_path:
    """
    file_path = os.path.abspath(os.path.join(rel_path))

    tree = ET.parse(file_path)

    for elem in tree.xpath("./row[@PostTypeId='1']"):
        print(elem.attrib['Id'])
        accepted_answer_id = None
        if 'AcceptedAnswerId' in elem.attrib:
            accepted_answer_id = elem.attrib['AcceptedAnswerId']
            print('accepted_ans_id set')
        creation_date = datetime.fromisoformat(elem.attrib['CreationDate'])
        last_activity_date = datetime.fromisoformat(elem.attrib['LastActivityDate'])
        new_question = Question(Id=elem.attrib['Id'],
                                AcceptedAnswerId=accepted_answer_id,
                                CreationDate=creation_date,
                                Score=elem.attrib['Score'],
                                ViewCount=elem.attrib['ViewCount'],
                                Body=elem.attrib['Body'],
                                OwnerUserId=elem.attrib['OwnerUserId'],
                                LastActivityDate=last_activity_date,
                                Title=elem.attrib['Title'],
                                Tags=elem.attrib['Tags'],
                                AnswerCount=elem.attrib['AnswerCount'],
                                CommentCount=elem.attrib['CommentCount'])
        db.session.add(new_question)
        #db.session.commit()


def populate_answers(db, rel_path):
    """Populate db with answers from xml file.
    :param db: database obj
    :param str rel_path:
    """
    file_path = os.path.abspath(os.path.join(rel_path))

    tree = ET.parse(file_path)
    print('answers below')
    for elem in tree.xpath("./row[@PostTypeId='2']"):
        print(elem.attrib['Id'])
        creation_date = datetime.fromisoformat(elem.attrib['CreationDate'])
        last_activity_date = datetime.fromisoformat(elem.attrib['LastActivityDate'])
        new_answer = Answer(Id=elem.attrib['Id'],
                            ParentId=elem.attrib['ParentId'],
                            CreationDate=creation_date,
                            Score=elem.attrib['Score'],
                            Body=elem.attrib['Body'],
                            OwnerUserId=elem.attrib['OwnerUserId'],
                            LastActivityDate=last_activity_date,
                            CommentCount=elem.attrib['CommentCount'])
        db.session.add(new_answer)
        #db.session.commit()
