import streamlit as st
import pickle
import pandas as pd
from validation import validate_name

#Application streamlit pour un moteur de recherche d'articles en TAL.
#Contient des scores des différents modèles utilisés (BM25, KeyBERT et RRF), respectivement pour les modèles épars, denses et hybrides.
#Les articles pertinents et correspondants aux requêtes, obtenus selon les scores, sont récupérés sous forme de data frame dénommés dfs_bm25, dfs_dense et dfs_hybrid.
#Le notebook contenant des calculs des différents scores est présent dans ce projet. Les données sont récupérées sur la plateforme hugging face
#et sont composées des articles en TAL avec leurs métadonnées (titre,extrait, texte complet, url, éditeurs etc). Les données sont ensuite prétraitées
#(tokenisées, mis en minuscules, stopwords supprimés) et des scores sont calculés pour chaque système de recherche d'information. Les résultats (articles pertinents
#selon les requêtes) sont récupérés sous forme de dataframe pandas, puis, mis sous format csv.


st.title("Moteur de Recherche en TAL")
st.write("Bienvenue sur ce petit moteur de recherche pour articles en TAL")
#L'utilisateur peut choisir le nombre de résultats qu'il souhaite afficher. Le nombre maximum de résultats qu'il peut afficher est fixé à 10
nb_iter = st.number_input(
    "Veuillez choisir le nombre de résultats à afficher",
    min_value=1,
    max_value=10,
    value=10,
    step=1
)
# Requêtes

#5 requêtes sont prédéfinies pour la recherche. C'est sur la base de ces requêtes que les scores ont été calculés avec différents modèles de recherche d'information (modèles dense, hybrid, épars)

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


#L'utilisateur peut sélectionner pour quel modèle il souhaite afficher des résultat et peut ainsi comparer la pertinence des modèles selon les résultats affichés pour chaque requête.
model_recherche=st.text_input("Veuillez choisir un model")
recherche = st.button("Rechercher")

if model_recherche:
    if validate_name(model_recherche):
        st.write("👍Modèle valide")
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

    else:
        st.write("Modèle invalide 👎: Veuillez choisir un modèle parmi 'BM25','Modèle hybride','Modèle dense'")





