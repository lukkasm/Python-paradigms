import micro_widget as mw

def otoc():
    slovo1 = mw.get_entry_text(entry_slovo)
    slovo2 = slovo1[::-1] 
    
    mw.set_entry_text(entry_slovo2, slovo2)

w = mw.display_window()

label_slovo = mw.make_label(w)
mw.set_label_text(label_slovo, "Zadejte slovo:")
mw.set_widget_x(label_slovo, 20)
mw.set_widget_y(label_slovo, 10)

entry_slovo = mw.make_entry(w)
mw.set_widget_x(entry_slovo, 20)
mw.set_widget_y(entry_slovo, 30)

label_slovo2 = mw.make_label(w)
mw.set_label_text(label_slovo2, "Obrácené slovo:")
mw.set_widget_x(label_slovo2, 20)
mw.set_widget_y(label_slovo2, 60)

entry_slovo2 = mw.make_entry(w)
mw.set_widget_x(entry_slovo2, 20)
mw.set_widget_y(entry_slovo2, 80)
mw.set_entry_command(entry_slovo2, otoc) 

button_odeslat = mw.make_button(w)
mw.set_button_text(button_odeslat, "Odeslat")
mw.set_widget_x(button_odeslat, 20)
mw.set_widget_y(button_odeslat, 110)
mw.set_button_command(button_odeslat, otoc)

mw.main_loop(w)
