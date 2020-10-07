from tutor.routes import home, course # noqa
from user_functions import register_and_login


def test_logout(client):
    # Test logout without user logged in
    response = client.get('/logout', follow_redirects=True)
    assert b'Tutor - Sharing Towards Excellence' in response.data
    # Register and login test user
    register_and_login(client)
    # Logout user
    response = client.get('/logout', follow_redirects=True)
    assert b'Goodbye' in response.data
