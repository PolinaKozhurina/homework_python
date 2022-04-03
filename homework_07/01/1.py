in_amount = 100
month = 4
k = 0
lst = []
for i in range(in_amount, 0, -month):
    in_amount = in_amount - 4
    # print(k, ":", "You need", in_amount, "kgs the next month.")
    k += 1
    lst.append(in_amount)
print("Kgs for every month:", lst)
