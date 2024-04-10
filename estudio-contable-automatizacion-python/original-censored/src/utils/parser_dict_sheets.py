def dict_sheets_to_list_customers(dict_sheets: dict) -> list:
    """
    Process a dictionary of sheets to create a list of clients with their corresponding information.

    Args:
        dict_sheets (dict): A dictionary containing sheets of data. Each sheet is represented as a list of dictionaries, where each dictionary represents a row of data.

    Returns:
        list: A list of dictionaries, where each dictionary represents a client with their corresponding information. Each dictionary contains the following keys: "Nombre" (client name), "Ingresos" (income), "Detalle" (income details), "Gastos_Operativos" (operating expenses), "Impuestos" (taxes), "Otros_Gastos" (other expenses), and "Emails" (email address).
    """
    # Create a dictionary to store the processed data for each client
    customers = {}

    # Process the data from the "Ingresos" sheet
    for income in dict_sheets["Ingresos"]:
        customer = income["Clientes"]
        if customer:
            if customer not in customers:
                customers[customer] = {}
            customers[customer].update(
                {"Ingresos": income["Ingresos"], "Detalle": income["Detalle"]}
            )

    # Process the data from the "Gastos" sheet
    for expense in dict_sheets["Gastos"]:
        customer = expense["Clientes"]
        if customer:
            if customer not in customers:
                customers[customer] = {}
            customers[customer].update(
                {
                    "Gastos_Operativos": expense["Gastos_Operativos"],
                    "Impuestos": expense["Impuestos"],
                    "Otros_Gastos": expense["Otros_Gastos"],
                }
            )

    # Process the data from the "Emails" sheet
    for email in dict_sheets["Emails"]:
        customer = email["Clientes"]
        if customer:
            if customer not in customers:
                customers[customer] = {}
            customers[customer].update({"Emails": email["Emails"]})

    # Create the list of customers that have values in all entries
    customer_list = []
    for customer, data in customers.items():
        if all(data.values()):
            customer_list.append(
                {
                    "Nombre": customer,
                    "Ingresos": data["Ingresos"],
                    "Detalle": data["Detalle"],
                    "Gastos_Operativos": data["Gastos_Operativos"],
                    "Impuestos": data["Impuestos"],
                    "Otros_Gastos": data["Otros_Gastos"],
                    "Emails": data["Emails"],
                }
            )
    return customer_list
