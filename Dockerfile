FROM python:3.9

WORKDIR /fizzbuzzdirectory

COPY ./requirements.txt /fizzbuzzdirectory/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fizzbuzzdirectory/requirements.txt

COPY ./fizzbuzz_app /fizzbuzzdirectory/fizzbuzz_app

CMD ["uvicorn", "fizzbuzz_app.fizzbuzz_operation:fizzbuzz_app", "--host", "0.0.0.0", "--port", "80"]
