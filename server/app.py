from functions.functions import getTodos, addTodo, getWeather
from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

'''
weatherData = getWeather()
desc = weatherData["data"][0]["weather"]["description"]
temp = weatherData['data'][0]["temp"]
dewPt = weatherData["data"][0]["dewpt"]
precip = weatherData["data"][0]["precip"]
sunrise = weatherData["data"][0]["sunrise"]
sunset = weatherData["data"][0]["sunset"]
'''

with open('todos.json', 'r') as myfile:
    data=myfile.read()
# parse file
todoObj = json.loads(data)

@app.route('/')
def hello():
    todoList = requests.get("http://localhost:5000/todo/getall").json()
    print(todoList)
    return render_template("index.html", 
        len=len(todoList), todos=todoList, 
        desc="desc", temp="temp", dewPt = "dewPt", precip="precip", sunrise="sunrise", sunset="sunset"
    )

@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return jsonify(todoObj)

@app.route('/todo/create',methods=['POST'])
def createTask():
    return 'Create new task'

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