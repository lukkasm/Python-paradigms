import micro_widget as mw

w = mw.display_window()

l1 = mw.make_label(w)
mw.set_widget_x(l1, 20)
mw.set_widget_y(l1, 20)

b1_1 = mw.make_button(w)
mw.set_widget_x(b1_1, 20)
mw.set_widget_y(b1_1, 40)
mw.set_button_text(b1_1, "+")

b1_2 = mw.make_button(w)
mw.set_widget_x(b1_2, 20)
mw.set_widget_y(b1_2, 80)
mw.set_button_text(b1_2, "-")

COUNTER1_INDEX = 0
state1 = [None]

def set_counter1(val):
    state1[COUNTER1_INDEX] = val
    mw.set_label_text(l1, str(val))

def get_counter1():
    return state1[COUNTER1_INDEX]

def inc_counter1():
    set_counter1(get_counter1() + 1)
   
def dec_counter1():
    set_counter1(get_counter1() - 1)    
    
set_counter1(0)
mw.set_button_command(b1_1, inc_counter1)
mw.set_button_command(b1_2, dec_counter1)

# Druhé počítadlo
l2 = mw.make_label(w)
mw.set_widget_x(l2, 120)
mw.set_widget_y(l2, 20)

b2_1 = mw.make_button(w)
mw.set_widget_x(b2_1, 120)
mw.set_widget_y(b2_1, 40)
mw.set_button_text(b2_1, "+")

b2_2 = mw.make_button(w)
mw.set_widget_x(b2_2, 120)
mw.set_widget_y(b2_2, 80)
mw.set_button_text(b2_2, "-")

COUNTER2_INDEX = 0
state2 = [None]

def set_counter2(val):
    state2[COUNTER2_INDEX] = val
    mw.set_label_text(l2, str(val))

def get_counter2():
    return state2[COUNTER2_INDEX]

def inc_counter2():
    set_counter2(get_counter2() + 1)
   
def dec_counter2():
    set_counter2(get_counter2() - 1)    
    
set_counter2(0)
mw.set_button_command(b2_1, inc_counter2)
mw.set_button_command(b2_2, dec_counter2)

mw.main_loop(w)
