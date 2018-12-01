class Power:
    def __init__(self):
        self.name = ""
    
    def turn_end(self):
        pass

    def turn_begin(self):
        pass
    
    def get_name(self):
        return self.name

class Normal(Power):
    def __init__(self):
        self.name = "Normal"        

class Lightning(Power):
    def __init__(self):
        self.name = "Normal"        

    def turn_begin(self):
        player_input = input()

