log_data = []
file = open('txt.txt', 'r')
for line in file:
    log_data.append(float(line.replace("\n", "")))

numb, amount = log_data, 42
for i in numb:
    amount += 1/i
print(amount)
