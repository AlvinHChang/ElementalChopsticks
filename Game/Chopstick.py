class Chopstick:
    """
    The Chopstick object class, this will keep track of the players and its corresponding power
    and life
    """
    def __init__(self, life=4, power=Normal, name="default"):
        self.left_hand = life
        self.right_hand = life
        self.name = name
        self.power = power()

    def attack(self, other):
        pass
        
    def response(self):
        pass

    def get_power_name(self):
        return self.power.get_name()

    def get_name(self):
        return self.name

