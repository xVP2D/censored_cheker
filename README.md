# Détection de Domaines Censurés

Ce projet Python permet de détecter les domaines potentiellement censurés en comparant les réponses DNS de différents résolveurs. Le script analyse une liste de domaines, interroge des résolveurs DNS de FAI et alternatifs, et identifie ceux qui peuvent être censurés.

## Fonctionnalités

- Chargement d'une liste de domaines à partir d'un fichier CSV.
- Requête DNS auprès de résolveurs spécifiques.
- Détection des domaines censurés en comparant les réponses DNS des résolveurs FAI et alternatifs.
- Génération d'un fichier CSV listant les domaines censurés.

## Prérequis

- Python 3.7 ou supérieur.
- Bibliothèques Python suivantes :
  - `pandas`
  - `dnspython`

Pour installer les dépendances, exécutez :
```bash
pip install pandas dnspython
Utilisation
Préparez le fichier d'entrée
Créez un fichier CSV nommé domains_fr.csv avec une colonne domain_nom contenant les noms de domaines à analyser.

Exemple de fichier domains_fr.csv :

csv
Copier le code
domain_nom
exemple.com
test.fr
domaine.net
Exécutez le script
Lancez le script Python :

bash
Copier le code
python script.py
Le script :

Interroge les résolveurs DNS des FAI spécifiés et des résolveurs alternatifs.
Identifie les domaines censurés et les enregistre dans un fichier censored_domains.csv.
Consultez le résultat
Les domaines identifiés comme censurés seront listés dans le fichier censored_domains.csv.

Configuration
Résolveurs FAI
Modifiez la liste fai_resolvers pour inclure les IP des résolveurs DNS des FAI à analyser :

python
Copier le code
fai_resolvers = ['194.2.0.50', '194.2.0.20']
Résolveurs alternatifs
Modifiez la liste alt_resolvers pour inclure les IP des résolveurs DNS alternatifs à comparer :

python
Copier le code
alt_resolvers = ['8.8.8.8', '1.1.1.1']
Structure du projet
script.py : Script principal pour l'analyse DNS.
domains_fr.csv : Fichier CSV d'entrée contenant les domaines.
censored_domains.csv : Fichier de sortie listant les domaines censurés.
Avertissements
Les résultats peuvent dépendre de la configuration réseau et des spécificités des résolveurs interrogés.
Ce script est destiné à des fins éducatives et d'analyse. Assurez-vous de respecter les lois et réglementations en vigueur lors de son utilisation.
Contributeurs
Ce projet est maintenu par [Votre Nom]. N'hésitez pas à contribuer en ouvrant une issue ou une pull request.
