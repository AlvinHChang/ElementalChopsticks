
class Game:
    def __init__(self, num_players=2):
        self.name = "item"
        # handles players
        self.num_players = num_players
        self.player_array = []
        for i in range(num_players):
            self.player_array.append(Chopstick())
        self.current_player_index = 0
        # handles game
        self.current_phase = self.turn_begin
        self.turn_begin_flag = True
    
    def switch_turn(self):
        self.current_player_index += 1
        self.current_player_index %= self.num_players
        self.current_phase = self.turn_begin

    def get_current_player(self):
        return self.player_array[self.current_player]

    def game_turn_loop(self):
        if not self.begin_turn:
            print("not beginning of turn")
        self.turn_begin_flag= False
        while not self.begin_turn:
            self.turn_continue()
    
    def turn_continue(self):
        self.current_phase()
    
    def turn_begin(self):
        print("turn begin")
        self.get_current_player().turn_begin()

        self.current_phase = self.turn_standby

    def turn_standby(self):
        print("turn standby")
        player_input = input()
        self.current_phase = self.turn_begin

    def turn_end(self):
        print("end turn")
        player_input = input()
        # flag for game turn loop to switch turn
        self.turn_begin_flag = True
        self.switch_turn()



        

class Game_Loop:
    def __init__(self):
        self.game = Game()
        self.begin_turn = True


    def game_loop(self):
        game = self.game
        game_end_flag = False
        while not game_end_flag:
            game.game_turn_loop()

