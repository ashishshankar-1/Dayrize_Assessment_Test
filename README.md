# Implemented Fizzbuzz problem using FastApi.

This repo belongs to implementation of fizzbuzz application.
Directory hirerchy
1) fizzbuzz_app (folder) in this folder below is the list of files exists.
   a) __init__.py ---Empty file
   b) fizzbuzz_operation.py  ---This is the main file of fizzbuzz application where business logic for get operation performed.
2) data_to_check.py --- This file is used to store the static data which is used to compare in testing.
3) test_fizzbuzz_operation.py --- This file consists of testcase to validate the API's works as expected.
4) Dockerfile --- Its a file which can moved as a image to run the application. command is (docker build -t Dockerfile)
5) requirements.txt --- It is used to install all the dependent packages before running the aplication. command (pip install -r requirements.txt)

How to run the fizzbuzz application:
Once the once steps done.Go to fizzbuzz_app directory
Then run command: uvicorn fizzbuzz_app.fizzbuzz_operation:app --reload
It will run on 127.0.0.1:8000
Below is the screenshot

![image](https://user-images.githubusercontent.com/96417821/156951836-d7c21145-1952-456a-9ee5-501576a9b06c.png)

Next Open the browser:
And run the below
http://127.0.0.1:8000/docs

The below output will be displayed:

![image](https://user-images.githubusercontent.com/96417821/156952067-294e8092-4423-4e20-b154-831ad187314b.png)

Next scrrenshot for the two API's
1) After executing the below  API.
![image](https://user-images.githubusercontent.com/96417821/156952251-40a475b1-054e-4d19-b36a-f577d161cc29.png)
Response:
![image](https://user-images.githubusercontent.com/96417821/156952380-f23507a1-f05b-41e4-a2fc-3e7410fca021.png)

2) After executing the below API.
![image](https://user-images.githubusercontent.com/96417821/156952450-9681b8d4-3865-46d4-afcd-af8265976430.png)
Response:
![image](https://user-images.githubusercontent.com/96417821/156952511-cf96af55-1c4d-4c36-90c4-855854e38ed5.png)

Next Testing the application to validate the API's work as expected.
1) filename is test_fizzbuzz_operation.py
So run the command pytest -vv in the same path where test_fizzbuzz_operation.py resides.
Below is the output:
![image](https://user-images.githubusercontent.com/96417821/156952691-f0999f97-74b4-4fc4-889c-b3acc7713150.png)

-------------------------------------*****************************-------------------------------------------------





