shirt_price = float(input())
win_ball_amount = float(input())

shorts = shirt_price * 0.75
socks = shorts * 0.2
shoes = 2 * (shirt_price + shorts)

total_spent = (shirt_price + shorts + socks + shoes) * 0.85

if total_spent >= win_ball_amount:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_spent:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {win_ball_amount - total_spent:.2f} lv. more.")
