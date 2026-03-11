import requests

API_KEY = "82922cfe-d566-4dde-922c-fed566bdded1"
url = "https://api.insee.fr/api-sirene/3.11/siret/39314710300013"

headers = {
    "X-INSEE-Api-Key-Integration": API_KEY
}

r = requests.get(url, headers=headers)

print("Status:", r.status_code)
print(r.text[:1000])