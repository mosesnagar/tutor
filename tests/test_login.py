from tutor.routes import home, course # noqa
from user_functions import create_test_user


def test_login(client):
    # Test login without register
    login_user = {
        'email': 'test@email.com',
        'password': '123',
        'submit': 'Login'
    }
    response = client.post('/login', data=login_user, follow_redirects=True)
    assert b'Login unsuccessful' in response.data
    # Create test user
    create_test_user(username="test", email="test@email.com", password="123")
    # Test user login
    response = client.post('/login', data=login_user, follow_redirects=True)
    assert b'Welcome' in response.data
    # Test login after user already logged in
    response = client.post('/login', data=login_user, follow_redirects=True)
    assert b'You are already logged in' in response.data
