bitcoins = int(input())
china_iuan = float(input())
commission_percent = float(input())

bitcoins_in_leva = bitcoins * 1168
china_iuan_in_dolar = china_iuan * 0.15
china_iuan_in_leva = china_iuan_in_dolar * 1.76

total_in_leva = bitcoins_in_leva + china_iuan_in_leva
total_in_eur = total_in_leva / 1.95

total_remaining = total_in_eur - (total_in_eur * commission_percent / 100)

print(f"{total_remaining:.2f}")






# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.
