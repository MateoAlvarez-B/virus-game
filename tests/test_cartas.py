def test_crear_carta():
    from src.cartas import Carta
    c = Carta("organo", "corazon")
    assert c.tipo == "organo"
    assert c.subtipo == "corazon"
