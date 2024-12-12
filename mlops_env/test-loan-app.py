import pytest
from flask import Flask
from loan_app import app  # Assuming your Flask app is saved as `app.py`

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Loan Approval Application" in response.data

def test_predict_invalid_method(client):
    """Test the predict endpoint for GET request"""
    response = client.get('/predict')
    assert response.status_code == 200
    assert b"I will make the predictions" in response.data
