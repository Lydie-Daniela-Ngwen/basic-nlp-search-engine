import streamlit as st
import pickle
import pandas as pd

st.title("Moteur de Recherche en TAL")
st.write("Bienvenue sur ce petit moteur de recherche pour articles en TAL")
nb_iter = st.number_input(
    "Veuillez choisir le nombre de résultats à afficher",
    min_value=1,
    max_value=10,
    value=10,
    step=1
)
# Requêtes
requests_options = (
    "Reconnaissance d'entités nommées",
    "Modélisation statistique en traduction automatique",
    "Enrichissement des systèmes de recherche d'information",
    "Biais de genre en traduction automatique",
    "Le tal et l'enseignement"
)

selected_request = st.selectbox(
    "Veuillez choisir une requête",
    requests_options
)

model_recherche = st.selectbox(
    "Veuillez choisir un système",
    ("BM25", "Modèle dense", "Modèle hybride")
)

recherche = st.button("Rechercher")

# Chargement des résultats BM25
with open("dfs_bm.pkl", "rb") as f:
    dfs_bm = pickle.load(f)
# Chargement des résultats modèle dense
with open("dfs_dense.pkl", "rb") as f:
    dfs_dense = pickle.load(f)
# Chargement des résultats modèle hybride
with open("dfs_hybrid.pkl", "rb") as f:
    dfs_hybrid = pickle.load(f)


if recherche:
    idx_req = requests_options.index(selected_request)

    if model_recherche == "BM25":
        df_bm_25 = dfs_bm[idx_req][:nb_iter]
        st.dataframe(df_bm_25)


    if model_recherche == "Modèle dense":
        df_dense_fin = dfs_dense[idx_req][:nb_iter]
        st.dataframe(df_dense_fin)


    if model_recherche == "Modèle hybride":
        df_hybrid_fin = dfs_hybrid[idx_req][:nb_iter]
        st.dataframe(df_hybrid_fin)
