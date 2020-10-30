"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

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

