from tutor.routes import home, course # noqa
from course_functions import search_course_name


def test_add_course(client):
    test_course = {'name': 'Open Source'}
    client.post('/addcourse', data=test_course, follow_redirects=True)
    assert search_course_name('Open Source')
