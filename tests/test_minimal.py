def test_request_example(client):
    response = client.get("/")
    assert b"<p>Hello, WorlD!</p>" in response.data