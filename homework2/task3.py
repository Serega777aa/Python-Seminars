n = int(input("n = "))
col = []
sum = 0
for i in range(1, n + 1):
    seq = round((1 + 1 / i) ** i, 2)
    sum += seq
    col.append(seq)
print(f"{col} Cумма = {(sum)}")
