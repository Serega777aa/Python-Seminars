for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not(x or y or z) == (not bool(x) and not y and not z)   
            print(f'x = {(x)}   y = {(y)}   z = {z}  result = {int(result)}')