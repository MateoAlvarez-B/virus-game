def test_motor_inicia():
    from src.motor import MotorJuego
    juego = MotorJuego()
    assert juego.jugador is not None
    assert juego.ia is not None
