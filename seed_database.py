"""Script to seed database."""

import os
# This is a module from Python’s standard library. It contains 
# code related to working with your computer’s operating system.
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server


# seed_database.py is one of the few files that you’ll write as a script. What 
# this means for you is that you won’t have to define functions! Sounds scary, we 
# know, but this file will only be used to re-create your database.

# The first thing you do when re-creating a database is run dropdb and createdb. 
# You can get Python to run those commands for you using os.system. Add
#  the following lines of code to seed_database.py.
os.system('dropdb ratings')
# More code will go here
os.system('createdb ratings')

# After that, you connect to the database and call db.create_all:
model.connect_to_db(server.app)
model.db.create_all()

# Then, load data from data/movies.json and save it to a variable:
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title, description, poster_path = (movie['title'],
                                    movie['overview'],
                                    movie['poster_path'])
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title,
                                 description,
                                 release_date,
                                 poster_path)
    movies_in_db.append(db_movie)


for n in range(10):
    email = f'user{n}@test.com' 
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_movie, score)