deposit_amount = float(input())
term_in_months = int(input())
annual_interest_rate = float(input())

interest_per_year = deposit_amount * annual_interest_rate / 100
interest_accrued = interest_per_year / 12 * term_in_months
final_amount = deposit_amount + interest_accrued

print(final_amount)


# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)