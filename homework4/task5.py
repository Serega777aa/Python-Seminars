def read_file(path,):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

p1 = read_file('myfile_1.txt').split()
p2 = read_file('myfile_2.txt').split()

def get_sum_poly(p1, p2): 
    a1 = int(p1[0][:-3])
    a2 = int(p2[0][:-3])
    b1 = int(p1[1] + p1[2][:-1])
    b2 = int(p1[1] + p2[2][:-1])
    c1 = int(p1[3] + p1[4])
    c2 = int(p1[3] + p2[4])
    a = str(a1 + a2) 
    b = str(b1 + b2)
    if int(b) > 0:
        b = ' + ' + b
    else:
        b = ' - ' + b[1:]
    c = str(c1 + c2)
    if int(c) > 0:
        c = ' + ' + c
    else:
        c = ' - ' + c[1:]
    sum = a + 'x^2' + b + 'x' + c + ' = 0' 
    return sum

f = open('myfile_3.txt', 'w')
f.write(get_sum_poly(p1, p2))
f.close()

