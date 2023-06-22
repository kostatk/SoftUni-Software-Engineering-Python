airliner = input()
adult_tickets = int(input())
kids_tickets = int(input())
ticket_net_price = float(input())
servicing_fee = float(input())

final_ticket_price = ticket_net_price + servicing_fee

kids_price = (ticket_net_price * 0.3) + servicing_fee

total_tickets_price = (kids_price * kids_tickets) + (final_ticket_price * adult_tickets)
profit = total_tickets_price * 0.2

print(f"The profit of your agency from {airliner} tickets is {profit:.2f} lv.")
