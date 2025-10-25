import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
from fastapi.testclient import TestClient
from app.main import app   # 👈 ahora sí funciona

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

