from os import getenv
from dotenv import load_dotenv
load_dotenv(".env")

id_folder = getenv("FOLDERID")
client_oauth = "client_secrets.json"
creds_file = "credentials.json"

list_sheets_required = ["Emails", "Ingresos", "Gastos"]

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://mail.google.com/",
]

monotribute = {
    "A": 1414762.58,
    "B": 2103025.45,
    "C": 2944235.60,
    "D": 3656604.33,
    "E": 4305799.15,
    "F": 5382248.94,
    "G": 6458698.71,
    "H": 7996484.12,
    "I": 8949911.06,
    "J": 10257028.68,
    "K": 11379612.01,
}
