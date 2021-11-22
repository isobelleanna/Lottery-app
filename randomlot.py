import random

your_ticket = [1, 37, 16, 28, 9, 11, 49]
lottery_arr = [random.randint(1, 50) for lottery in range(7)]

winner_binary = [1 if item in your_ticket else 0 for item in lottery_arr]

correct_numbers = sum(winner_binary)
