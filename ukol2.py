import micro_widget as mw

def check_password_match():
    heslo1 = mw.get_entry_text(entry_heslo)
    heslo2 = mw.get_entry_text(entry_heslo2)
    
    if heslo1 == heslo2:
        mw.set_label_text(label_shoda_hesel, "Hesla se shodují.")
    else:
        mw.set_label_text(label_shoda_hesel, "Hesla se neshodují.")

w = mw.display_window()

label_heslo = mw.make_label(w)
mw.set_label_text(label_heslo, "Zadejte heslo:")
mw.set_widget_x(label_heslo, 20)
mw.set_widget_y(label_heslo, 10)

entry_heslo = mw.make_entry(w)
mw.set_widget_x(entry_heslo, 20)
mw.set_widget_y(entry_heslo, 30)
mw.set_entry_command(entry_heslo, check_password_match)

label_heslo2 = mw.make_label(w)
mw.set_label_text(label_heslo2, "Znovu zadejte heslo:")
mw.set_widget_x(label_heslo2, 20)
mw.set_widget_y(label_heslo2, 60)

entry_heslo2 = mw.make_entry(w)
mw.set_widget_x(entry_heslo2, 20)
mw.set_widget_y(entry_heslo2, 80)
mw.set_entry_command(entry_heslo2, check_password_match)

label_shoda_hesel = mw.make_label(w)
mw.set_label_text(label_shoda_hesel, "")
mw.set_widget_x(label_shoda_hesel, 20)
mw.set_widget_y(label_shoda_hesel, 100)

mw.main_loop(w)
