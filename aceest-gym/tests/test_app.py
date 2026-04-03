def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_member_valid(client):
    response = client.post("/members", json={"name": "John"})
    assert response.status_code == 201
    data = response.get_json()
    assert data is not None
    assert "message" in data


def test_get_members_contains_inserted_member(client):
    client.post("/members", json={"name": "John"})
    response = client.get("/members")
    assert response.status_code == 200
    members = response.get_json()
    assert isinstance(members, list)
    assert {"name": "John"} in members


def test_add_member_empty_body(client):
    response = client.post("/members")
    assert response.status_code == 400


def test_add_member_invalid_json(client):
    response = client.post(
        "/members",
        data=b"{not valid json",
        content_type="application/json",
    )
    assert response.status_code == 400
