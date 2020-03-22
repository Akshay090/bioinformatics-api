"""
This file (test_api.py) contains the functional tests for the api blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the api blueprint.
"""


def test_valid_question_page(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/questions/1' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/questions/1')
    assert response.status_code == 200
    assert b"total_pages" in response.data


def test_invalid_question_page(test_client, init_database):
    """
    GIVEN a Flask application WHEN the '/questions/2' page is requested (GET) THEN check the response is invalid as
    the pagination is set to 15 items per page and the test db is only of 15 items, so only page 1 will exist other pages should give error
    """
    response = test_client.get('/questions/2')
    assert response.status_code == 404


def test_valid_question(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/question/<int:question_id>' page is requested (GET)
    THEN check the response is valid if valid question_id is given
    """
    response = test_client.get('/question/11063')
    assert response.status_code == 200


def test_invalid_question(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/question/<int:question_id>' page is requested (GET)
    THEN check the response is valid if invalid question_id is given
    """
    response = test_client.get('/question/00')
    assert response.status_code == 404


def test_valid_search_question(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/search_q' page is requested (GET) with search term as q in query string
    THEN check the response is valid if search term exist in db
    """
    response = test_client.get('/search_q', query_string={'q': "I am"})
    assert response.status_code == 200


def test_invalid_search_question(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/search_q' page is requested (GET) with search term as q in query string
    THEN check the response is valid if search term don't exist in db
    """
    response = test_client.get('/search_q', query_string={'q': "I xxx"})
    assert response.status_code == 200
    assert b'[]\n' in response.data


def test_valid_search_answers(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/search_a' page is requested (GET) with search term as q in query string
    THEN check the response is valid if search term exist in db
    """
    response = test_client.get('/search_a', query_string={'q': "I am"})
    assert response.status_code == 200


def test_valid_search_answers_no_ques(test_client, init_database):
    """
    GIVEN a Flask application WHEN the '/search_a' page is requested (GET) with search term as q in query string,
    the search term exist in answer but the answer don't have a question in db,
    THEN check the response is valid it return empty list
    """
    response = test_client.get('/search_a', query_string={'q': "If you have"})
    assert response.status_code == 200
    assert b'[]\n' in response.data