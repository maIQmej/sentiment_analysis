# tests/test_api.py
import pytest

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_get_analyze_basic(client):
    r = client.get("/analyze", params={"text": "Odio los lunes"})
    assert r.status_code == 200
    data = r.json()
    assert data["text"] == "Odio los lunes"
    assert data["output"] in {"POS", "NEG", "NEU"}
    assert isinstance(data["probas"], dict)

def test_get_analyze_unicode(client):
    r = client.get("/analyze", params={"text": "Hoy es un gran día ☀️"})
    assert r.status_code == 200
    data = r.json()
    assert data["text"].startswith("Hoy es un gran día")

def test_get_analyze_missing_param(client):
    r = client.get("/analyze")  # falta 'text'
    assert r.status_code == 422  # FastAPI valida el query param

def test_post_analyze_basic(client):
    payload = {"text": "Me encanta programar en Python"}
    r = client.post("/analyze", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["text"] == payload["text"]
    assert data["output"] in {"POS", "NEG", "NEU"}
    assert "probas" in data and isinstance(data["probas"], dict)

def test_post_analyze_invalid_body(client):
    # cuerpo inválido → debe fallar validación Pydantic
    r = client.post("/analyze", json={})
    assert r.status_code == 422

def test_batch_basic(client):
    payload = {"texts": ["Me encanta Python", "La app es muy lenta"]}
    r = client.post("/analyze_batch", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "results" in data and isinstance(data["results"], list)
    assert len(data["results"]) == 2
    for item in data["results"]:
        assert "text" in item and "output" in item and "probas" in item

def test_batch_missing_texts(client):
    r = client.post("/analyze_batch", json={})
    assert r.status_code == 422

@pytest.mark.parametrize("texto", [
    "Excelente servicio",
    "La experiencia fue normal",
    "Pésimo rendimiento del sistema",
])
def test_parametrized_get(client, texto):
    r = client.get("/analyze", params={"text": texto})
    assert r.status_code == 200
    assert r.json()["text"] == texto
