def er_gyldig_passord(passord: str) -> bool:
    if len(passord) < 10:
        return False
    if not any(char.isupper() for char in passord):
        return False
    
    if not any(char.islower() for char in passord):
        return False
    
    if not any(char.isdigit() for char in passord):
        return False
    
    if ' ' in passord:
        return False
        
    
    return True