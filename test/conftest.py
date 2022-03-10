from flask import Flask
from pytest import fail, fixture

@fixture
def app():
    return __import__("app").app

@fixture
def client(app: Flask):
    with app.test_client() as client:
        return client

