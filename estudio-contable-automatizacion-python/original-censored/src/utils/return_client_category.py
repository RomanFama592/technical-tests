from env import monotribute

# Sort the 'monotribute' dictionary by its values in ascending order
category_sorted = sorted(monotribute.items(), key=lambda x: x[1])

def get_category_of_customer(customer):
    income = customer["Ingresos"]
    category = category_sorted[0][0]

    for current_index, (letter, limit) in enumerate(category_sorted):
        # If it exceeds the limit I add the letter that follows it
        if income > limit:
            try:
                category = category_sorted[current_index + 1][0]
            except IndexError:
                # If it passes the limit of the last category, a plus is added at the end to indicate it.
                category = letter + " +"
                break
        else:
            break

    return category
