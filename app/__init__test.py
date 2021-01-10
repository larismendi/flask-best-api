from app.test.fixtures import app, client


def test_app_creates(app):
    assert app


def test_app_healthy(app, client):
    with client:
        resp = client.get("/hello")
        assert resp.status_code == 200
        assert resp.is_json
        assert resp.json == "Hello!"