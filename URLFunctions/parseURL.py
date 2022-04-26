# Does the creation of a url that looks like
# https://google.com/Hi%20There%p=""
<<<<<<< HEAD
import requests


userinputtest = 'spiders bugs'

#console.log("hi")
def createurl(userinput):
    search = 'https://www.google.com/search'
    usersearch = {"q": userinput}
    resp = requests.get(search, params=usersearch)
    final = str(resp.url)
    return final 

t1 = createurl(userinputtest)
print(t1)
=======
from PyQt5.QtCore import *

def parseURL(userInput):
    print("This would be a url, " + userInput)

    return userInput
>>>>>>> 3ecf938721900848e720385d27bf69810c95bae4
