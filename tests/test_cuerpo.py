def test_cuerpo_inicial():
    from src.cuerpo import Cuerpo
    c = Cuerpo()
    assert c.estado("corazon") is None
