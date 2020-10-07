from tutor.routes import home, course  # noqa


def test_flash_message(client):
    # check flash message
    response = client.get('/flash')
    assert b'Test message' in response.data
