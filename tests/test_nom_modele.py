from validation import validate_name


def test_name_str():
    assert validate_name(2485)  is False

def test_nom_mod_hybrid():
    assert validate_name("modèle hybride") is False

def test_nom_mode_bm():
    assert validate_name("bm25") is False

