from app.services import EnsemblService

def test_valid_rsid():
    # Testa um RSID conhecido por existir
    result = EnsemblService.get_variant_data("rs7142")
    assert "rsid" in result
    assert result["rsid"] == "rs7142"
    assert "chromosome" in result

def test_invalid_rsid():
    # Testa um formato inválido
    result = EnsemblService.get_variant_data("invalid_id_123")
    assert "error" in result