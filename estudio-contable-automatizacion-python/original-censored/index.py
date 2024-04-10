import gspread as gs
from datetime import datetime
from src.utils.google_auth import oauth
from env import id_folder, list_sheets_required
from googleapiclient.discovery import build
from src.utils.email_sender import send_mail, create_mail
from src.utils.return_client_category import get_category_of_customer
from src.utils.parser_dict_sheets import dict_sheets_to_list_customers

# Authorize the Google Sheets sheet_service & mail_service
auth = oauth()
sheet_service = gs.authorize(auth)
mail_service = build("gmail", "v1", credentials=auth)

# Retrieve the list of spreadsheet files in the folder
list_sheets, response = sheet_service.list_spreadsheet_files(folder_id=id_folder)
sheets_names = [sheet["name"] for sheet in list_sheets]

# Check if the response is successful and the list of sheets is complete
if not set(list_sheets_required).issubset(set(sheets_names)):
    raise Exception("Error Missing files in this folder")

# Create a dictionary to store the data from the required sheets
dict_sheets = {}

for sheet in list_sheets:
    # Check if the sheet name is in the list of required sheets
    if sheet["name"] in list_sheets_required:
        # Retrieve all records from the last worksheet of the sheet
        records = (
            sheet_service.open_by_key(sheet["id"]).get_worksheet(-1).get_all_records()
        )
        dict_sheets[sheet["name"]] = records

# Transform the dictionary to a list of customers
list_customers = dict_sheets_to_list_customers(dict_sheets)

current_year = str(datetime.now().year)

# Attempt to open a Google Sheets document named "Monotributo Categorias"
# within a specified folder (id_folder) and select a worksheet for the current year.
try:
    # Try to open the worksheet for the current year.
    categories_sheet = sheet_service.open("Monotributo Categorias", id_folder)
    categories_sheet = categories_sheet.worksheet(current_year)

# Handle the case where the worksheet for the current year is not found.
except gs.exceptions.WorksheetNotFound:
    # If the worksheet doesn't exist, create a new one with the title as the current year,
    # and allocate space for 100 rows and 2 columns.
    categories_sheet = categories_sheet.add_worksheet(
        title=current_year, rows="100", cols="2"
    )

# Handle the case where the entire "Monotributo Categorias" spreadsheet is not found.
except gs.exceptions.SpreadsheetNotFound:
    # If the spreadsheet doesn't exist, create a new one with the name "Monotributo Categorias"
    # within the specified folder. Then, create a new worksheet for the current year with
    # the same title and dimensions (100 rows and 2 columns).
    categories_sheet = sheet_service.create("Monotributo Categorias", id_folder)
    categories_sheet = categories_sheet.add_worksheet(
        title=current_year, rows="100", cols="2"
    )


customers_category = [["Clientes", "Categorias"]]

for customer in list_customers:
    if (
        customer["Gastos_Operativos"] + customer["Impuestos"] + customer["Otros_Gastos"]
        > customer["Ingresos"]
    ):
        subject_mail = "Sus gastos superan sus ingresos"

        body_mail = f"""
        Estimado cliente {customer['Nombre']},

        Le escribimos desde el banco para informarle que, según nuestros registros, sus gastos mensuales superan sus ingresos. Esto puede afectar negativamente a su salud financiera y generarle intereses y comisiones.
        Le recomendamos que revise su presupuesto y ajuste sus hábitos de consumo para evitar problemas futuros. Si necesita ayuda o asesoramiento, puede contactar con nuestro servicio de atención al cliente.

        Gracias por confiar en nosotros.

        Atentamente,
        Estudio Grabina, Annaratone & Asoc.
        """
        message_mail = create_mail(
            customer["Email"],
            subject_mail,
            body_mail,
        )
        try:
            print(send_mail(mail_service, message_mail))
        except Exception as error:
            print(customer["Nombre"], ": ", error)
    customers_category.append([customer["Nombre"], get_category_of_customer(customer)])

categories_sheet.update(f"A1:B{len(customers_category)+1}", customers_category)
