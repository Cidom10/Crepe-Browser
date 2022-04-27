# Does the creation of a url that looks like
# https://google.com/Hi%20There%p=""
import requests

#console.log("hi")
def parseURL(userinput):
    search = 'https://www.google.com/search'
    usersearch = {"q": userinput}
    resp = requests.get(search, params=usersearch)
    final = str(resp.url)
    return final 
