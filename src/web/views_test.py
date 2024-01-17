from django.urls import reverse

def test_index(client):
    response = client.get(reverse("web:index"))
    assert response.status_code == 200
    assert response.content == "Hello, Spokane Python User Group"
