from functions.functions import getTodos, addTodo, getWeather
from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

<<<<<<< HEAD
# weatherData = getWeather()
# desc = weatherData["data"][0]["weather"]["description"]
# temp = weatherData['data'][0]["temp"]
# dewPt = weatherData["data"][0]["dewpt"]
# precip = weatherData["data"][0]["precip"]
# sunrise = weatherData["data"][0]["sunrise"]
# sunset = weatherData["data"][0]["sunset"]
=======
'''
weatherData = getWeather()
desc = weatherData["data"][0]["weather"]["description"]
temp = weatherData['data'][0]["temp"]
dewPt = weatherData["data"][0]["dewpt"]
precip = weatherData["data"][0]["precip"]
sunrise = weatherData["data"][0]["sunrise"]
sunset = weatherData["data"][0]["sunset"]
'''
>>>>>>> 9a770f0bf85e35c5974c73fcf7eb66c0663ac29b

todos = [ "Check moodle", "Win the Expo", "Something" ]

@app.route('/')
def hello():
    return render_template("index.html", 
<<<<<<< HEAD
        len=len(todos), todos=todos, 
        # desc=desc, temp=temp, dewPt = dewPt, precip=precip, sunrise=sunrise, sunset=sunset
=======
        len=len(todoList), todos=todoList, 
        desc="desc", temp="temp", dewPt = "dewPt", precip="precip", sunrise="sunrise", sunset="sunset"
>>>>>>> 9a770f0bf85e35c5974c73fcf7eb66c0663ac29b
    )

@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return jsonify(todos)

@app.route('/todo/create',methods=['POST'])
def createTask():
    if request.method == "POST":
        todos.append(request.form.get("task"))
    return redirect(url_for("hello"))

@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    return 'Update Task'

@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    return 'Delete task'

@app.route("/weather")
def weather():
    return "weatherData"

if __name__ == '__main__':
    app.run(debug=True)