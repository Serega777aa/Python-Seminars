f = open('input_data_RLE.txt', 'r', encoding='utf-8')
s = f.readline() + ' '
f.close()

encode = ''
count = 1
print(s)
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        count += 1
    elif count == 1:
        encode += s[i - 1]
    else:
        encode += str(count) + s[i - 1]
        count = 1
print(encode)

decode = ''
for i in range(len(encode)):
    if encode[i].isdigit():
        decode += (int(encode[i]) - 1) * encode[i + 1]
    else:
        decode += encode[i]
print(decode)



    

    