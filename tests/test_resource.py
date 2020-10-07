from tutor.routes import home, course, resources # noqa
from course_functions import create_test_course, search_resource_title


def test_resource_create(client):
    create_test_course(3000, "test_course")
    resource = {
        'title': 'resource_name',
        'content': 'content',
        'link': 'https://www.google.com',
        'submit': 'Post'
    }
    client.post('/resource/new?id=3000', data=resource, follow_redirects=True)
    test_resource = search_resource_title("resource_name")
    assert test_resource.title == 'resource_name'
    assert test_resource.content == 'content'
    assert test_resource.link == 'https://www.google.com'
