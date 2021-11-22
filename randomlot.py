import random

your_ticket = [1, 37, 16, 28, 9, 11, 49]
lottery_arr = [random.randint(1, 50) for lottery in range(7)]

winner_binary = [1 if item in your_ticket else 0 for item in lottery_arr]

correct_numbers = sum(winner_binary)

if correct_numbers == 3:
    prize_money = 20
elif correct_numbers == 4:
    prize_money = 40
elif correct_numbers == 5:
    prize_money = 100
elif correct_numbers == 6:
    prize_money = 10000
elif correct_numbers == 7:
    prize_money = 100000
else:
    prize_money = 0

print(
    f'The winning numbers are {lottery_arr}.\nYou have {correct_numbers} matching numbers and your total winnings are £{prize_money}.')
