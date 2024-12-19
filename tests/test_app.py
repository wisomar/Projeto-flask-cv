import pytest
from app.meu_site import app


@pytest.fixture
def client():
    """Cria um cliente de teste para o Flask."""
    with app.test_client() as client:
        yield client

def test_homepage_status_code(client):
    """Testa se a página inicial retorna status 200."""
    response = client.get("/")
    assert response.status_code == 200

def test_homepage_content(client):
    """Testa se a página inicial contém texto esperado."""
    response = client.get("/")
    assert b"Nome Completo" in response.data  # Altere "Bem-vindo" para algo do seu template.
