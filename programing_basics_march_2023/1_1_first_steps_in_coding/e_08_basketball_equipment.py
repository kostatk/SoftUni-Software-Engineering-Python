fee_for_training_per_year = int(input())

shoes_expenses = fee_for_training_per_year - (fee_for_training_per_year * 0.4)
clothes_expenses = shoes_expenses - (shoes_expenses * 0.2)
ball_expenses = clothes_expenses / 4
accessories_expenses = ball_expenses / 5

total_expenses = fee_for_training_per_year + shoes_expenses + clothes_expenses + ball_expenses + accessories_expenses

print(total_expenses)