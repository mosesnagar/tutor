from tutor import db
from tutor.models.users import Users
from tutor.models.course import Course


def test_fav(client):
    # create new user
    u = Users(username='pypy', email='email@email.com', password='pass')
    u.save()

    # check that user exists and has no favorites
    user = Users.query.filter_by(username='pypy').first()
    assert [] == user.favorites

    # create new course and add it to the user's favorites
    c = Course(name="python course")
    user.addFavorite(c)

    # check the course added to user favorites
    same_user = Users.query.filter_by(username='pypy').first()
    assert c == same_user.favorites[0]

    # clean up db
    same_user.removeAllFavorites()
    db.session.delete(c)
    db.session.delete(same_user)
    db.session.commit()
