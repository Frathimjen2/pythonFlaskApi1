from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Empliados(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("Elegir * de los empliados)")
        return {'empliados': [i[0] for i in query.cursor.fetchall()]}


class Pistas(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("Elegir pistaid, nombre, compositor, precioUnidad del la pista;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Empliados_Nom(Resource):
    def get(self, empliados_id):
        conn = db_connect.connect()
        query = conn.execute("Elegir * de donde vendrian emplaidosId =%d " % int(empliados_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(Empliados, '/empliados')
api.add_resource(Pistas, '/pistas')
api.add_resource(Empliados_Nom, '/empliados/<empliados_id>')

if __name__ == '__main__':
    app.run(port=5002)