# Basic search engine

## Description
Ce projet présente un moteur de recherche, se servant de différentes techniques de recherche d'information pour indexer des résultats.
Le moteur de recherche concerne notamment le domaine du TAL. 

### Données utilisées
Les données utilisées sont un jeu de données présent sur HuggingFace contenant des articles du domaine du Traitement automatique des langues dans différentes langues.
Les données se trouvent à l'adresse https://huggingface.co/datasets/WINGNUS/ACL-OCL/resolve/main/acl-publication-info.74k.v3.full-sections-partial-topic-labels.pkl.

Les données sont récupérées puis filtrées afin de ne conserver que les documents en langue française. 
Pour ce faire, le module detect de la librairie langdetect a été utilisé sur les titres. A cela s'ajoute des regex pour obtenir des données ciblées, notamment pour des titres qui contenaient deux langues, l'anglais et le français.

## Prétraitements
Les données sont prétraités notamment par la tokenisation et la suppression de stop words. Le modèle utilisé pour la tokenisation est fr_core_news_sm de spacy.Les colonnes utilisées sont principalement les colonnes title et full_texte. 

### Systèmes de recherche
3 systèmes de RI sont utilisés:

## Modèle épars
Ce modèle est basé sur des scores d'occurrences des mots. Le modèle BM25 est utilisé pour cette recherche et les scores sont sauvegardés.

## Modèle dense 
Ce modèle est basé sur un sentence transformer, antoinelouis/biencoder-mMiniLMv2-L6-mmarcoFR.

## Modèle hybride
Un reclassement rrf pour les deux modèles mentionnés, avec un k de 60.

### Application Streamlit
Le tout est déployé sur une application construite avec streamlit. Le fichier appy.py contenant l'application est un fichier à part, qui peut être lancé à partir de toute interface exécutant ce type de fichier (Par exemple terminal pycharm avec la commande "streamlit run appy.py").
Les fichiers contenant les différents résultats sont également ajoutés dans le repo et peuvent simplement être téléchargés afin d'ouvrir l'application en local.
## L'interface
L'interface web permet à l'utilisateur de sélectionner une requête parmi les 5 proposées dans une liste déroulante. Les requêtes sont limitées à 5 car les scores ont été calculés 
avec les différents modèles pour ces requêtes. L'utilisateur peut entrer le nom du modèle qu'il souhaite utiliser. Des tests sont mis en place afin de s'assurer que l'utilisateur entre un nom
de modèle valide (BM25, Modèle dense, Modèle hybride). Les noms des modèles sont sensibles à la casse. L'utilisateur peut également choisir le nombre de résultats à afficher (entre 1 et 10). 
Les résultats obtenus des requêtes sont sous forme de dataframe pandas contenant l'id dans le dataframe d'origine, un score selon le modèle choisi, le titre, un extrait et l'url.

### Installation
```bash
pip install -r requirements.txt```


### Lancer l'application
```bash
streamlit run appy.py```

