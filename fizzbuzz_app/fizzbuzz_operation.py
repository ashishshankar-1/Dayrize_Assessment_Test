import requests
from fastapi import FastAPI

app = FastAPI()

def fetch_details_from_jsonplaceholder():
    # Fetch the details from url https://jsonplaceholder.typicode.com/posts/1
    try:
        title, body, err = None, None, None
        reqObj=requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=3)
    except requests.exceptions.RequestException as err:
        err = f"OOps: Something Else {err}"
    except requests.exceptions.HTTPError as err:
        err = f"Http Error:, {err}"
    except requests.exceptions.ConnectionError as err:
        err = f"Error Connecting: {err}"
    except requests.exceptions.Timeout as err:
        err = f"OOps: Something Else {err}"
    else:     
        jsonFormat = reqObj.json()
        title = jsonFormat.get('title').strip()
        body = jsonFormat.get('body').strip()
    return title, body

@app.get('/')
def get_first_ten_fizzbuzz():
    # get operation to fetch the details from range 1-10
    tempList = list()
    title , body = fetch_details_from_jsonplaceholder()
    for index in list(range(1,11)):
        if index % 3 == 0 and index % 5 == 0:
            fizzbuzz = 'FizzBuzz'
        elif index % 3 == 0:
            fizzbuzz = 'Fizz'
        elif index % 5 == 0:
            fizzbuzz = 'Buzz'
        else:
            fizzbuzz = None
        tempList.append({"number": index, "fizzbuzz": fizzbuzz,  "placeholder_post": {"title": title, 'body': body}})
    return tempList

@app.get('/fizzbuzz/{id}')
def fetch_fizzbuzz_by_id(id:int):
    # Fetch the details on the basis of particular id (int)
    title , body = fetch_details_from_jsonplaceholder()
    if id % 3 == 0 and id % 5 == 0:
        fizzbuzz = 'FizzBuzz'
    elif id % 3 == 0:
        fizzbuzz = 'Fizz'
    elif id % 5 == 0:
        fizzbuzz = 'Buzz'
    else:
        fizzbuzz = None
    return {"number": id, "fizzbuzz": fizzbuzz,  "placeholder_post": {"title": title, 'body': body}}

