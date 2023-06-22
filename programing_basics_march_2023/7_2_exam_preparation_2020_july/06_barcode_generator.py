beginning_number = int(input())
end_number = int(input())

beginning_text = str(beginning_number)
a_beg = int(beginning_text[0])
b_beg = int(beginning_text[1])
c_beg = int(beginning_text[2])
d_beg = int(beginning_text[3])

ending_text = str(end_number)
a_end = int(ending_text[0])
b_end = int(ending_text[1])
c_end = int(ending_text[2])
d_end = int(ending_text[3])

for a in range(a_beg, a_end + 1):
    if a % 2 == 0:
        continue
    for b in range(b_beg, b_end + 1):
        if b % 2 == 0:
            continue
        for c in range(c_beg, c_end + 1):
            if c % 2 == 0:
                continue
            for d in range(d_beg, d_end + 1):
                if d % 2 == 0:
                    continue
                print(f"{a}{b}{c}{d}", end=" ")



# beginning_number = int(input())
# end_number = int(input())
#
# for barcode in range(beginning_number, end_number + 1):
#     cur_barcode = str(barcode)
#     MAGIC = True
#     for i in range(0, len(cur_barcode)):
#         check = int(cur_barcode[i])
#         if check % 2 == 0:
#             MAGIC = False
#             continue
#     if MAGIC:
#         print(f"{cur_barcode}", end=" ")
