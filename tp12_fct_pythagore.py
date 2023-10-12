def test_pythagore(a: int, b: int, c: int) -> bool:
    # Programmation défensive : Vérifier si les paramètres sont positifs
    assert a > 0, "La longueur 'a' doit être positive."
    assert b > 0, "La longueur 'b' doit être positive."
    assert c > 0, "La longueur 'c' doit être positive."

    return a**2 + b**2 == c**2

# Test avec les valeurs 8, 6 et 10
assert test_pythagore(8, 6, 10) == True