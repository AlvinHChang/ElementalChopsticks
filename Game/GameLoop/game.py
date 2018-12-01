
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
        self.current_player = self.game.get_current_player()
        self.begin_turn = True

    def game_turn_loop(self):
        if not self.begin_turn:
            print("not beginning of turn")
        self.begin_turn = False
        while not self.begin_turn:
            self.game.turn_continue()

    def game_loop(self):
        game = self.game
        game_end_flag = False
        while not game_end_flag:
            self.game_turn_loop()

    def turn_continue(self):
        self.current_phase()
    
    def turn_begin(self):
        print("turn begin")
        game.current_player.__turn_begin__()

        self.current_phase = self.turn_standby

    def turn_standby(self):
        print("turn standby")
        player_input = input()
        self.current_phase = self.turn_begin

    def turn_end(self):
        print("end turn")
        player_input = input()
        # flag for game turn loop to switch turn
        self.begin_turn = True
        self.current_phase = self.turn_begin



