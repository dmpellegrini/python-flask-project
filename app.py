from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('bread_recipes', user='danielepellegrini', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Bread(BaseModel):
  name = CharField()
  flour_grams = IntegerField()
  water_grams = IntegerField()
  yeast_grams = IntegerField()
  starter_grams = IntegerField()
  salt_grams = IntegerField()
  servings = IntegerField()

db.connect()
db.drop_tables([Bread])
db.create_tables([Bread])

Bread(name='Sourdough', flour_grams=1000, water_grams=700, yeast_grams=0, starter_grams=200, salt_grams=20, servings=2 ).save()
Bread(name='Baguette', flour_grams=1200, water_grams=700, yeast_grams=3, starter_grams=40, salt_grams=24, servings=3 ).save()
Bread(name='Ciabatta', flour_grams=1030, water_grams=900, yeast_grams=2, starter_grams=120, salt_grams=20, servings=2 ).save()

app = Flask(__name__)

@app.route('/bread/', methods=['GET', 'POST'])
@app.route('/bread/<name>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(name=None):
  if request.method == 'GET':
    if name:
        return jsonify(model_to_dict(Bread.get(Bread.name == name)))
    else:
        breads_recipes_list = []
        for bread in Bread.select():
            breads_recipes_list.append(model_to_dict(bread))
        return jsonify(breads_recipes_list)

  if request.method =='PUT':
    body = request.get_json()
    Bread.update(body).where(Bread.id == id).execute()
    return "Bread " + str(id) + " has been updated."

  if request.method == 'POST':
    new_bread = dict_to_model(Bread, request.get_json())
    new_bread.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Bread.delete().where(Bread.id == id).execute()
    return "Bread " + str(id) + " deleted."

app.run(debug=True, port=9000)

