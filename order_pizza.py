def get_size():
    while True: 
        size = input('What size would you like? S/M/L: ').upper()
        if size in ['S', 'M', 'L']:
            return size
        print('Invalid input. Please enter S, M, or L: ')

def calc_base_cost(size):
    bill = 0
    if size == 'S':
        bill += 15
    elif size == 'M':
        bill += 20
    elif size == 'L':
        bill += 25
    return bill

def add_pepperoni(size, bill):
    while True:
        user_input = input('Would you like to add pepperoni Y/N?: ').upper()
        if user_input == 'Y':
            return bill + 2 if size == 'S' else bill + 3
        elif user_input == 'N':
            return bill
        print('Invalid input. Please enter Y or N: ')    

def add_cheese(bill):
    while True:
        user_input = input('Would you like to add cheese Y/N?: ').upper()
        if user_input == 'Y':
            return bill + 2
        elif user_input == 'N':
            return bill
        print('Invalid input. Please enter Y or N: ')    

def main():
    print('Welcome to Barraka Pizza!')
    pizza_size = get_size()
    bill = calc_base_cost(pizza_size)
    bill = add_pepperoni(pizza_size, bill)
    bill = add_cheese(bill)
    print(f"Your total bill is ${bill}.")

if __name__ == '__main__':
    main()