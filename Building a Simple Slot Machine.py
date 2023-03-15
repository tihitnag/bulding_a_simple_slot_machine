import random

MAX_NUM = 3
MAX_BET = 100
MIN_BET = 1
row = 3
col = 3
symobl_count = {
    'a': 2,
    'b': 4,
    'c': 5,
    'd': 6

}
symobl_val = {
    'a': 4,
    'b': 2,
    'c': 2,
    'd': 3

}


def deposit():
    while True:
        amount = input('inter the amount: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('enter a number greater than zero')
        else:
            print('u should enter a number')
    return amount


# deposit()
# after this collect the beat amount  and if they win multiply the beat to line
# how much they wanna bet per line
def get_line():
    while True:
        lines = input('enter the amount ine to bet on : 1-' + str(MAX_NUM) + " ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_NUM:
                break
            else:
                print('enter a number valid number')
        else:
            print('the string shoud be number')
    return lines


def get_bet():
    while True:
        bet = input('enter the amount to bet: $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'enter a number greater than zero{MIN_BET}-{MAX_BET}')
        else:
            print('u should enter a number')
    return bet


def winning_game(colomns , lines,bet, val):
    winng = 0
    winning_line = []
    for line in range(lines):
        print(line)
        symbol = colomns[0][line]
        # check evey symbol in the first colomn and every line
        for colomn in colomns:
            symbol_check = colomn[line]
            # check cjeck at row 0 check the 1st symbol then row 1 2nd symbol
            if symbol_check != symbol:
                break
        else:
            winng += val[symbol] * bet
            winning_line.appeend(line + 1)
    return winng,winning_line

# generate symbols ,randomly pick each row inside of col
# for every col we have to genetrate certain amount of rows

# ones we uses the the symbol we shouldnt use it agin so we have to remove it from the list
def get_slot_machine(row, col, symbols):
    # since we use dictonary we use .item for the key and value
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    colomns = []
    for _ in range(col):

        copyed_symbol = all_symbol[:]
        colomun1 = []
        for _ in range(row):
            val = random.choice(copyed_symbol)
            copyed_symbol.remove(val)
            colomun1.append(val)

        colomns.append(colomun1)
    return colomns


# since colomuns are like [1,2,3]3col and one row to play our sgame we have to transpose it
def print_slot(colomns):
    for row in range(len(colomns[0])):
        for i, colomn2 in enumerate(colomns):
            if i != colomns - 1:

                print(colomn2[row], end='|')
            else:
                print(colomn2[row], end=' `')
        print()


def winning_game(bet, lines, val, colomns):
    winng = 0
    winning_line = []
    for line in range(lines):
        symbols = colomns[0][line]
        # check evey symbol in the first colomn and every line
        for colomn in colomns:
            symbol_check = colomn[line]
            # check cjeck at row 0 check the 1st symbol then row 1 2nd symbol
            if symbol_check != symbols:
                break
        else:
            winng += val[symbols] * bet
            winning_line.appeend(line + 1)
    return winng


def spin_again(balance):
    lines = get_line()
    bet = get_bet()
    total = bet * lines
    if total > balance:
        print(f'u dont have enough money {balance}')
    else:

        print(f'you are betting {bet} on {lines} lines.in total bet is equal to ${total}45')
    slot = get_slot_machine(row, col, symobl_count)
    print(slot)
    winng,winning_line= winning_game(slot, lines, bet, symobl_val)
    print(f'you won ${winng}')
    print(f'you won lines:', *winning_line)
    return winng - total


def main():
    balance = deposit()
    while True:
        print(f'current balance is {balance} ')
        ans = input('press any key to spin(q to quit)')
        if ans == 'q':
            break

        balance += spin_again(balance)
    print(f'here is the ur balance{balance}')


main()
