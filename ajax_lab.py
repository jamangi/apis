#!/usr/bin/python3
from requests import get
from sys import argv

def ajax_call():
    url = "https://jsonplaceholder.typicode.com/{}"
    r = get(url.format(argv[1]))
    data = r.json()

    for i in data:
        print(i['name'])
    
if __name__ == '__main__':
    ajax_call()
