
def test_index_success(client):
    # page loads
    response = client.get("/")
    assert response.status_code == 200