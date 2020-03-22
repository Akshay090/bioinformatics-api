from datetime import datetime


def test_new_question(new_question):
    """
    GIVEN a Question model
    WHEN a new Question is created
    THEN check the id, CreationDate, Score, ViewCount,
    Body, OwnerUserId, Title, LastActivityDate, Tags, AnswerCount, CommentCount fields are defined correctly
    """
    iso_date = "2020-01-01T09:40:54.017"
    datetime_object = datetime.fromisoformat(iso_date)
    assert new_question.Id == 1
    assert new_question.Id is not None
    assert new_question.CreationDate == datetime_object
    assert new_question.Score == 1
    assert new_question.ViewCount == 1
    assert new_question.Body == "body test"
    assert new_question.OwnerUserId == 1
    assert new_question.Title == "title test"
    assert new_question.LastActivityDate == datetime_object
    assert new_question.Tags == "test tag"
    assert new_question.AnswerCount == 1
    assert new_question.CommentCount == 1


def test_new_answer(new_answer):
    """
    GIVEN a Answer model
    WHEN a new Answer is created
    THEN check the id, ParentId, CreationDate, Score,
    Body, OwnerUserId, LastActivityDate, CommentCount fields are defined correctly
    """
    iso_date = "2020-01-01T09:40:54.017"
    datetime_object = datetime.fromisoformat(iso_date)
    assert new_answer.Id == 1
    assert new_answer.Id is not None
    assert new_answer.ParentId == 1
    assert new_answer.CreationDate == datetime_object
    assert new_answer.Score == 1
    assert new_answer.Body == "body test"
    assert new_answer.OwnerUserId == 1
    assert new_answer.LastActivityDate == datetime_object
    assert new_answer.CommentCount == 1
