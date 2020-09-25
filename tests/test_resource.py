from tutor.models.course import Resource


def test_add_new_resource():
    client = app.test_client()
    assert Resource.query.all() == []
    response = client.post('/resource', data=dict(
        title='test_resource_title'
        content='test_resource_content'
        link='test_resource_link'))
    assert Resource.query.first().title == 'test_resource_title'

