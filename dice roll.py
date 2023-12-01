import random

#funkcja o nazwie roll dice i tworze parametr o nazwie amount, ktory jest typu liczba calkowita 2 (jesli nie zdefiniuje i tak rzuci dwiema koscmi)

def roll_dice(amount: int = 2)  -> list[int]:    # poniewaz chcemy uzyskac te wartosc z powrotem na liscie i chcemy sie upewnic ze sa l.calkowitymi
    if amount <= 0:                                                    # sprawdzam czy kwota jest mniejsza lub rowna od 0
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)      # to funkcja do rzucania koscmi
        rolls.append(random_roll)

    return rolls

def main():       #funkacj gówna
    while True:
        try:
            user_input: str = input('How many dice would you like to roll?')

            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            print(*roll_dice(int(user_input)), sep=', ')    # * rozpakuje liste ktora mam, zeby nie bylo w nawiasach napisane tylko tak jak chce
        except ValueError:
            print('(Please enter a valid number)')

if __name__ == '__main__':
    main()

