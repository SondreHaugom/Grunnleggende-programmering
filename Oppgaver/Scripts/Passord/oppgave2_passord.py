import re
def er_gyldig_passord(passord: str) -> bool:
    if len(passord) < 10:
        return False    
    if not re.search(r'[A-Z]', passord):
        return False
    if not re.search(r'[a-z]', passord):
        return False
    if not re.search(r'[0-9]', passord):
        return False
    if not re.search(r'[t]', passord):
        return False
    if ' ' in passord:
        return False
    else:
        return True