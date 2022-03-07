# Dayrize_Assessment_Test
Assessment Test For Dayrize

This repo belongs to implementation of fizzbuzz application.
Directory hirerchy
1) fizzbuzz_app (folder) in this folder below is the list of files exists.
   a) __init__.py ---Empty file
   b) fizzbuzz_operation.py  ---This is the main file of fizzbuzz application where business logic for get operation performed.
2) data_to_check.py --- This file is used to store the static data which is used to compare in testing.
3) test_fizzbuzz_operation.py --- This file consists of testcase to validate the API's works as expected.
4) Dockerfile --- Its a file which can moved as a image to run the application. command is (docker build -t Dockerfile)
5) requirements.txt --- It is used to install all the dependent packages before running the aplication.

How to run the fizzbuzz application:
Once the once steps done.Go to fizzbuzz_app directory
Then run command: uvicorn fizzbuzz_app.fizzbuzz_operation:app --reload
It will run on 127.0.0.1:8000
Below is the screenshot

![image](https://user-images.githubusercontent.com/96417821/156951836-d7c21145-1952-456a-9ee5-501576a9b06c.png)

