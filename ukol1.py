import micro_widget as mw

def print_name_surname():
    jmeno = mw.get_entry_text(entry_jmeno)
    prijmeni = mw.get_entry_text(entry_prijmeni)
    print("Jméno a příjmení:", jmeno, prijmeni)

w = mw.display_window()

label_jmeno = mw.make_label(w)
mw.set_label_text(label_jmeno, "Zadejte jméno:")
mw.set_widget_x(label_jmeno, 20)
mw.set_widget_y(label_jmeno, 10)

entry_jmeno = mw.make_entry(w)
mw.set_widget_x(entry_jmeno, 20)
mw.set_widget_y(entry_jmeno, 30)

label_prijmeni = mw.make_label(w)
mw.set_label_text(label_prijmeni, "Zadejte příjmení:")
mw.set_widget_x(label_prijmeni, 20)
mw.set_widget_y(label_prijmeni, 60)

entry_prijmeni = mw.make_entry(w)
mw.set_widget_x(entry_prijmeni, 20)
mw.set_widget_y(entry_prijmeni, 80)

button_odeslat = mw.make_button(w)
mw.set_button_text(button_odeslat, "Odeslat")
mw.set_widget_x(button_odeslat, 20)
mw.set_widget_y(button_odeslat, 110)
mw.set_button_command(button_odeslat, print_name_surname)

mw.main_loop(w)
