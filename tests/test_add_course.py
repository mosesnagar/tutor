from tutor.routes import home, course # noqa
from user_functions import register_and_login
from course_functions import search_course_name


def test_add_course(client):
    test_course = {'name': 'Open Source'}
    # Test add course without logging in
    response = client.post('/addcourse', data=test_course, follow_redirects=True)
    assert b'You must be logged in to add course' in response.data
    register_and_login(client)
    # Test after login
    response = client.post('/addcourse', data=test_course, follow_redirects=True)
    assert search_course_name('Open Source')
