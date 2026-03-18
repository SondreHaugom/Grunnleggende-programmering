from pytest import mark
from oppgave2_passord import er_gyldig_passord

@mark.parametrize("passord, forventet", [
    ("Winter2024", True), # Gyldig passord med 't'
    ("winter2024", False), # Mangler stor bokstav
    ("WinterRain", False), # Mangler tall
    ("Winter8", False), # For kort passord
    ("Winter 2024", False), # Inneholder mellomrom
    ("1234567890", False), # Mangler bokstaver og 't'
    ("WINTER2024", False), # Mangler små bokstaver
    ("Controller5", True), # Gyldig passord med 't'
])
# Testfunksjon som sjekker om passordet er gyldig i henhold til kravene
def test_er_gyldig_passord(passord, forventet):
    assert er_gyldig_passord(passord) == forventet