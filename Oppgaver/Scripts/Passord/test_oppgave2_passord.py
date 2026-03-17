from pytest import mark
from oppgave2_passord import er_gyldig_passord

@mark.parametrize("passord, forventet", [
    ("123456789", False),  
    ("1234567890", True),  
    ("passord123", True),  
    ("kort", False),        
    ("littlengre", True),
])
def test_er_gyldig_passord(passord, forventet):
    assert er_gyldig_passord(passord) == forventet

 