from pytest import mark
from oppgave2_passord import er_gyldig_passord

@mark.parametrize("passord, forventet", [
    ("Sunny8Rain", True), # Gyldig passord
    ("sunny8rain", False), # Mangler stor bokstav
    ("SunnyRain", False), # Mangler tall
    ("Sunny8", False), # For kort passord
    ("Sunny 8Rain", False), # Inneholder mellomrom
    ("1234567890", False), # Mangler bokstaver
    ("SUNNY8RAIN", False), # Mangler små bokstaver
    ("Sunny8Rain!", True), # Gyldig passord med spesialtegn
])
def test_er_gyldig_passord(passord, forventet):
    assert er_gyldig_passord(passord) == forventet