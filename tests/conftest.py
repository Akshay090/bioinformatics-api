import os
import pytest
from datetime import datetime
from app import create_app, db
from app.models import Question, Answer
from app.config import Config
from app.utils import populate_db

basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'


@pytest.fixture(scope='module')
def new_question():
    iso_date = "2020-01-01T09:40:54.017"
    datetime_object = datetime.fromisoformat(iso_date)
    question = Question(Id=1,
                        AcceptedAnswerId=None,
                        CreationDate=datetime_object,
                        Score=1,
                        ViewCount=1,
                        Body="body test",
                        OwnerUserId=1,
                        Title="title test",
                        LastActivityDate=datetime_object,
                        Tags="test tag",
                        AnswerCount=1,
                        CommentCount=1
                        )
    return question


@pytest.fixture(scope='module')
def new_answer():
    iso_date = "2020-01-01T09:40:54.017"
    datetime_object = datetime.fromisoformat(iso_date)
    answer = Answer(Id=1,
                    ParentId=1,
                    CreationDate=datetime_object,
                    Score=1,
                    Body="body test",
                    OwnerUserId=1,
                    LastActivityDate=datetime_object,
                    CommentCount=1
                    )
    return answer


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestConfig)
    db.init_app(flask_app)

    # Creating test client by Werkzeug test Client provided by flask
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Populate db with test data
    populate_db(db, "tests/test_posts_se.xml")

    yield db

    db.drop_all()
