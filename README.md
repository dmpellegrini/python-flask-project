# Danny's Python Flask App

Welcome to Danny's Flask API App, where bread ingredients come to turn into recipes

## The Install Dependencies are the following

--pipenv
--peewee
--flask
--psycopq2-binary

## Running the API

In order to run the API you will need to create a bread_recipes database with the following command

```
CREATE DATABASE bread_recipes
```

After that you will need to clone this repo and set up your virtual environment within the python-flask-project directory with the following commands

```
git clone git@github.com:dmpellegrini/python-flask-project.git
```
```
pipenv shell
```

Finally, run the following command and you will have access to the api endpoints on 127.0.0.1:9000

```
python3 app.py
```

## API Endpoints

If you simply access [127.0.0.1:9000/bread](127.0.0.1:9000/bread) you can either retrieve all the bread recipes with a GET request, or you can add a bread recipe with a POST request.

Finally if you access [127.0.0.1:9000/bread/<name>](127.0.0.1:9000/bread/<name>), a GET request will retrieve the bread by name, a PUT request will update any of the named bread's properties and finally a DELETE request will simply remove the type of bread from the database.


## The schema for the bread recipes is the following and it is strict

--name
--four_grams = <grams_of_wheat>
--water_grams = <grams_of_wheat>
--salt_grams = <grams_of_wheat>
--yeast_grams = <grams_of_wheat>
--starter_grams = <grams_of_wheat>
--servings_grams = <grams_of_wheat>

### Future Goals for the API include more fleshed out recieps
