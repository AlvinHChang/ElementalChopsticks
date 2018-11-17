class Power:
    def __init__(self):
        self.name = ""
    
    def __begin_phase__(self):
        pass
    
    def get_name(self):
        return self.name


class Normal(Power):
    def __init__(self):
        self.name = "Normal"        

class Chopstick:
    def __init__(self, life=4, power=Normal, name="default"):
        self.left_hand = life
        self.left_hand = life
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

class Game:
    def __init__(self, num_players=2):
        self.name = "item"
        self.num_players = num_players
        self.player_array = []
        for i in range(num_players):
            self.player_array.append(Chopstick())
        self.current_player_index = 0
    
    def switch_turn(self):
        self.current_player_index += 1
        self.current_player_index %= self.num_players

    def get_current_player(self):
        return self.player_array[self.current_player]
    
    def turn_begin(self):
        pass
        

class Game_API:
    def __init__(self):
        self.game = Game()
        self.current_phase = self.turn_begin

    def game_loop(self):
        game = self.game
        game.turn_begin()
        game.get_current_player()
        player_input = input()
        game.switch_turn()

    def turn_continue(self):
        self.current_phase()
    
    def turn_begin(self):
        print("turn begin")
        self.current_phase = self.turn_standby

    def turn_standby(self):
        print("turn standby")
        self.current_phase = self.turn_begin


                
        
    
