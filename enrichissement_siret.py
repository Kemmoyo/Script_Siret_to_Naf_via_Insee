import pandas as pd
import requests
from tqdm import tqdm

API_KEY = "82922cfe-d566-4dde-922c-fed566bdded1"

INPUT_FILE = "testGptB2B.xlsx"
OUTPUT_FILE = "siret_enrichi.xlsx"

data_url = "https://api.insee.fr/api-sirene/3.11/siret/"

headers = {
    "X-INSEE-Api-Key-Integration": API_KEY
}

df = pd.read_excel(INPUT_FILE)

codes = []
activites = []
sources = []

for siret in tqdm(df["Numero Siret"]):

    try:
        r = requests.get(data_url + str(siret), headers=headers)

        if r.status_code == 200:
            data = r.json()

            etab = data["etablissement"]

            code_naf = etab.get("activitePrincipaleNAF25Etablissement", "")

            codes.append(code_naf)
            activites.append(code_naf)
            sources.append("INSEE")

        elif r.status_code == 404:

            codes.append("Introuvable")
            activites.append("")
            sources.append("")

        else:

            codes.append("")
            activites.append("")
            sources.append("")

    except Exception as e:

        print("Erreur :", siret, e)

        codes.append("")
        activites.append("")
        sources.append("")

df["Code Naf"] = codes
df["Activité"] = activites
df["Source"] = sources

df.to_excel(OUTPUT_FILE, index=False)

print("Fichier terminé :", OUTPUT_FILE)