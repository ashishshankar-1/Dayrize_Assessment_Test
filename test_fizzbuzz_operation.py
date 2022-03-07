from fastapi.testclient import TestClient
import fizzbuzz_app.fizzbuzz_operation as ops
from data_to_check import data

client = TestClient(ops.app)

def test_read_fizzbuzzdata():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == data

def test_read_id():
    response = client.get("/fizzbuzz/15")
    assert response.status_code == 200
    assert response.json() == {"number": 15,
                               "fizzbuzz": "FizzBuzz",
                               "placeholder_post": {"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                                                    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
                                                    }}

