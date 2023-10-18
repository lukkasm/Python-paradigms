# Jednoduchý formulář
# Kombinujeme objektový a procedurální styl.

from omw import *

# textové pole s popiskem
def make_entry_field(text):
    label = Label().set_text(text)
    entry = Entry().move(0, 20)
    return Group().set_items([label, entry])

def get_entry_field_value(entry_field):
    entry = entry_field.get_items()[1]
    return entry.get_text()

# formulář
def make_form():
    name_field = make_entry_field("hostname:")
    surname_field = make_entry_field("nickname:").move(0, 50)
    return Group().set_items([name_field, surname_field])
    
def get_form_data(form):
    items = form.get_items()
    name = get_entry_field_value(items[0])
    surname = get_entry_field_value(items[1])
    return [name, surname]

# okno
window = Window()
form = make_form().move(20, 20)
window.set_widget(form)



window.main_loop()
