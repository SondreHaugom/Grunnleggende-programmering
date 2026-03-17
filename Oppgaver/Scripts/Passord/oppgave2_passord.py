def er_gyldig_passord(passord: str) -> bool:
    if len(passord) < 10:
        return False