baggage_fee_over_20 = float(input())
baggage_weight = float(input())
days_till_traveling = int(input())
baggage_number = int(input())

fee = 0

if baggage_weight < 10:
    fee += baggage_fee_over_20 * 0.2
elif 10 <= baggage_weight <= 20:
    fee += baggage_fee_over_20 * 0.5
elif baggage_weight > 20:
    fee += baggage_fee_over_20

if days_till_traveling > 30:
    fee *= 1.1
elif 7 <= days_till_traveling <= 30:
    fee *= 1.15
elif days_till_traveling < 7:
    fee *= 1.4

total_price = fee * baggage_number

print(f" The total price of bags is: {total_price:.2f} lv. ")
