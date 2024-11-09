def ontcijfer(a, b):
    boodschap = ""
    for letter in a:
        if letter in b:
            boodschap = boodschap + letter
    return boodschap