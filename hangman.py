from random import choice  #funcka wyboru

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])   #1 funckcja, słowo do ogradniecia: typu string, ktore bedzie rowne choice i o insice coice , z lista slowwipsue te co chce zeby odgadł

    username: str = input('What is your name? >> ')   #nazwa uzytkownika
    print(f'Welcome to hangman, {username}!')

    # Setup
    guessed: str = ''  #''bedzie sie zapelniac naszymi literami odgadnietymi zmienna:
    tries: int = 3     # chcemy aby uzytkownik mial tylko trzy proby

    while tries > 0:
        blanks: int = 0    #zmienna   __

        print('Word: ', end='')   #punkt wyjscia slowo ktore zgaduje
        for char in word:
            if char in guessed:   # czy jest ta litera w srodku,wydrukuj jesli tak  , end bez niczego bo chcemy zeby sie laczyły
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1   #sledzimy puste miejsca, jak nie ma pustycvh to wygał
        print()   #dodaje pusty wiuersz, dodaje dla sformatowania

        if blanks == 0:        # czy uzytkwnik wygrał grę>
            print('You got it')
            break

        guess: str = input('Enter a letter: ')

        if guess in guessed:
            print(f' Yoy already used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining... You lose.')
                break

if __name__ == '__main__':
    run_game()

    # dodatkowo dodaj opcje zeby uzytkownik mogl dodac tylko 1 literke albo cale slowo, bo inaczej pokaze sie haslo jak wpiszemy wszystkie literkli