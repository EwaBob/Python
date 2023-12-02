import random
import sys   # korzystanie z systemu

class RPS:
    def __init__(self):   #inicjator z atrybutami self
        print('Welcome to RPS 9000')

        self.moves: dict = {'rock': '@', 'paper': '%', 'scissors': '&'}  #tu powinny bez emotiony, \\slownik ruchów
        self.valid_moves: list[str] = list(self.moves.keys())   #po to zeby nie wpisac nic inego poza tymi 3. tworze liste z tego sliwnija i cchem aby ta lusta zawierala klucze
# tworze 3 metody , 1 do grania w gre , drugawyswietlanie , sprawdzanie czy wygralismy m spr ruchow
    def play_game(self):
        user_move: str = input('Rock, paper, or scissors? >> ').lower()   #uzyskuje dane od usera, dodaje lower aby python nie patrzyl czy z duzej czy z malej , sam sobie skaluje

        if user_move == 'exit':   # jak chce user przewac to pisze exit
            print('thanks for playing')
            sys.exit()  #systemowe wyjscie koncowe to wychodzi z programu
        if user_move not in self.valid_moves:
            print('Invalid move...')  #jak zrobi ruch co nie instnieje trafia na szczyt funkcji
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)   #wybieramy losowy ruch z listy

        self.display_moves(user_move, ai_move)  # wyswietlanie ruchow uzytkownikowi, rychy ktore musi wykonasc
        self.check_move(user_move, ai_move)


    def display_moves(self, user_move: str, ai_move:str):  #
        print('------------------')    #separator
        print(f'You: {self.moves[user_move]}')   #zastepowanie na emotiony
        print(f'AI: {self.moves[ai_move]}')   #to co komputer
        print('------------------')


    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a tie!')     #remisy itp.gra
        elif user_move == "rock" and ai_move == 'scissors':
            print("You win!")
        elif user_move == "scissors" and ai_move == 'paper':
            print("You win!")
        elif user_move =='paper' and ai_move == 'rock':
            print('You win!')
        else:
            print('Al wins...')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()