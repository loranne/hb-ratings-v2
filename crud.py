"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, description, release_date, poster_path):
    """Create and return a new movie."""

    movie= Movie(title=title, 
                description=description,
                release_date=release_date,
                poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, rating):
    """Create and return a new rating."""

    rating = Rating(user=user, 
                    movie=movie, 
                    rating=rating)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movies():
    """Return a list of all movies"""

    movies = db.session.query(Movie).all()

    return movies

def get_movie_by_id(movie_id):
    """Returns movie based on id"""

    movie = Movie.query.get(movie_id)

    return movie

def get_users():
    """Returns a list of all users"""

    users = User.query.all()

    return users

def get_user_by_id(user_id):
    """Returns user based on id"""

    user = User.query.get(user_id)

    return user


def get_user_by_email(email):
    ''' return a user by email'''

    return User.query.filter(User.email == email).first()


def validate_user_password(password):
    """checks for valid password on login"""

    return User.query.filter(User.password == password).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)   