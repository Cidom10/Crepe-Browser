from os import getcwd
import requests

def getTodos():
    lines = []
    pwd = getcwd()
    with open(pwd + "/todos.txt") as f:
        lines = f.readlines()
    return lines

def addTodo(todo):
    pwd = getcwd()
    with open(pwd +"/todos.txt", "a") as f: 
        f.write(todo)
        f.write('\n')
    return "Added todo"

def getWeather():
    # lat = "32.5232"
    # lon = "-92.6379"
    # base = "https://api.weatherbit.io/v2.0/current"
    # apiKey = "a7d56065c38e49de91817bee23408dd5"
    # res = requests.get(f"{base}?lat={lat}&lon={lon}&key={apiKey}&units=I")
    # return res.json()
    print("get weather")
