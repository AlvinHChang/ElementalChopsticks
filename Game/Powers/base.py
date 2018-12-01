class Power:
    def __init__(self):
        self.name = ""
    
    def __begin_phase__(self):
        pass

    def __begin_phase__(self):
        pass
    
    def get_name(self):
        return self.name

class Normal(Power):
    def __init__(self):
        self.name = "Normal"        

class Lightning(Power):
    def __init__(self):
        self.name = "Normal"        

    def __begin_phase__(self):
        player_input = input()

