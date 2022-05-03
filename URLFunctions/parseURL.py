# Does the creation of a url that looks like
# https://google.com/Hi%20There%p=""
import requests

top_level_domains = [".com", ".edu", ".net", ".org"]

def parseURL(userinput):
    for domain in top_level_domains:
        if (domain not in userinput):
            continue
        
        else:
            if "http" not in userinput:
                userinput = "http://" + userinput
            return userinput

    search = 'https://www.google.com/search'
    usersearch = {"q": userinput}
    resp = requests.get(search, params=usersearch)
    final = str(resp.url)
    return final 
