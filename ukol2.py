from omw import *

def make_matrix_entry_field(row, col):
    label = Label().set_text(f"Element [{row + 1}, {col + 1}]:")
    entry = Entry().move(0, 20)
    return Group().set_items([label, entry])

def make_matrix_form(rows, cols):
    matrix_entries = [make_matrix_entry_field(i, j).move(j * 150, i * 50) for i in range(rows) for j in range(cols)]
    return Group().set_items(matrix_entries)

def get_matrix_data(form, rows, cols):
    items = form.get_items()
    matrix_data = [[get_entry_field_value(items[i * cols + j]) for j in range(cols)] for i in range(rows)]
    return matrix_data

# Okno
window = Window()

# Formulář pro zadávání matice
matrix_form = make_matrix_form(2, 3).move(20, 20)
window.set_widget(matrix_form)

# Tlačítko pro získání dat
get_matrix_button = Button().set_text("Get Matrix").move(0, 200)
get_matrix_button.set_delegate(window)

# Přidání události pro tlačítko
def button_clicked(sender):
    matrix_data = get_matrix_data(matrix_form, 2, 3)
    print(matrix_data)

get_matrix_button.set_delegate(window)
get_matrix_button.send_event("ev_button_clicked", get_matrix_button)
get_matrix_button.set_delegate(None)

window.main_loop()
