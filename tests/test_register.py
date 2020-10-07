from tutor import bcrypt
from tutor.routes import home, course # noqa
from user_functions import search_user_name


def test_register_user(client):
    # Test register user
    user = {
        'username': 'test_register',
        'email': 'test@email.com',
        'password': '123',
        'confirm_password': '123',
        'submit': 'Sign Up'
    }
    # Register new user
    client.post('/register', data=user, follow_redirects=True)
    test_user = search_user_name("test_register")
    # Test new user
    assert test_user.username == 'test_register'
    assert test_user.email == 'test@email.com'
    # Test password hash
    assert bcrypt.check_password_hash(test_user.password, '123')
    # Test trying to register an already registered username and email
    response = client.post('/register', data=user, follow_redirects=True)
    assert b'Username already registered' and b'Email already registered' in response.data
