# importing the module
from bson import json_util
import json
import imdb

from pymongo import MongoClient

from flask import Flask, jsonify, request
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True

PORT = 3030
HOST = '0.0.0.0'

# creating instance of IMDb
ia = imdb.IMDb()

# getting top 250 movies
search = ia.get_top250_movies()
top25Movies = []
for i in range(25):
    top25Movies.append(search[i]['title'])

# connectiong to the DataBase
client = MongoClient(
    "mongodb+srv://sai:X977Y58d5QXE4EM&@cluster0.4eabc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client["assignment"]
BookingColl = db["bookings"]
latest_shows = db["latest_shows"]

post = {"_id": 0, "moviesList": top25Movies}

latest_shows.update_one({"_id": 0}, {"$set": {"moviesList": top25Movies}})


class List(Resource):
    def get(self):
        result = {}
        temp = latest_shows.find_one({"_id": 0})
        result["latest shows"] = temp["moviesList"]
        return jsonify(result)


class test(Resource):
    def get(self):
        return jsonify({'message': 'test'})


class Booking(Resource):
    def get(self):
        return jsonify({'message': 'Booking'})

    def post(self):
        data = request.get_json()
        post = {"user": data["user"],
                "show": data["show"], "status": "success"}
        BookingColl.insert_one(post)
        result = {}
        result["status"] = "Booking successful"
        return jsonify(result)


class latest_booking(Resource):
    def get(self):
        return jsonify({'message': 'test'})

    def post(self):
        data = request.get_json()
        DBdata = BookingColl.find({"user": data["user"],
                                   "show": data["show"]})
        latesShows = []
        for i in DBdata:
            latesShows.append(i)
        result = {}
        result["data"] = json.loads(json_util.dumps(latesShows))

        return jsonify(result)


api.add_resource(List, '/list')
api.add_resource(test, '/test')
api.add_resource(Booking, '/booking')

api.add_resource(latest_booking, '/get_latest_booking')


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=PORT, debug=True)
