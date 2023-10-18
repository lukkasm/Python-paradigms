from omw import *

class Radiobutton:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = False

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_state(self):
        return self.state
    
    def set_x(self, x):
        if type(x) != int:
            raise TypeError("x coordinate of a point should be an integer")
        self.x = x
        return self.x
    
    def set_y(self, y):
        if type(y) != int:
            raise TypeError("y coordinate of a point should be an integer")
        self.y = y
        return self.y
    
    def set_state(self, state):
        if type(state) != bool:
            raise TypeError("Invalid value for state. Must be a boolean.")
        self.state = state
        return self.state
    
    def toggle(self):
        self.state = not self.state
        return self
    
    def move(self, dx, dy): 
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self
    
    def is_selected(self):
        return self.state

class RadiobuttonGroup:
    def __init__(self):
        self.items = []
        self.selected = None

    def get_items(self):
        return self.items

    def set_items(self, items):
        for item in items:
            if not isinstance(item, Radiobutton):
                raise TypeError("Each item in the RadiobuttonGroup should be a Radiobutton.")
        self.items = items[:]
        self.selected = None
        return self
    
    def set_selected(self, selected):
        if selected is not None and selected not in self.get_items():
            raise ValueError("Selected Radiobutton is not in the group.")
        
        self.selected = selected
        for radiobutton in self.get_items():
            radiobutton.set_state(radiobutton == selected)
        return self

    def move(self, dx, dy):
        for radiobutton in self.get_items():
            radiobutton.move(dx, dy)
        return self
    
# r = Radiobutton()
# print(r.toggle().get_state())
# r.move(20, 30)



# window = Window()
# window.set_widget()
# window.main_loop()

