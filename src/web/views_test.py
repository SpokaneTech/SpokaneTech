from django.urls import reverse
from django.test.client import Client as TestClient

def test_index(client: TestClient):
    response = client.get(reverse("web:index"))
    assert response.status_code == 200
    assert response.content == b"Hello, Spokane Python User Group"
