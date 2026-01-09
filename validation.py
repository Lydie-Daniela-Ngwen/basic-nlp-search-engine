def validate_name(name:str):
    if not isinstance(name,str):
        return False
    valides = ["BM25", "Modèle dense", "Modèle hybride"]
    if name not in valides:
        return False
    else:
        return  True