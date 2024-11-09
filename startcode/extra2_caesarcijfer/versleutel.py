def verschuif (tekst, verschuiving):
    verschoven_tekst = ""
    tekst = tekst.lower()
    for karakter in tekst:
        verschoven_tekst = verschoven_tekst + chr(ord(karakter) + verschuiving)
    return verschoven_tekst

def encrypteer (tekst, code):
    return verschuif(tekst, code)

def decrypteer  (tekst, code):
    return verschuif(tekst, -code)

