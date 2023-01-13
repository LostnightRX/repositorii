#    for n in range(1,100):      решение из демо 2023
#        s = bin(n)[2:]
#        if s.count('1') % 2 == 0:
#            s = '10' + s[2:] + '0'
#        else:
#            s = '11' + s[2:] + '1'
#        if int(s,2) > 40:
#            print(n)
#            break

    for n in range(1, 100000):          #решение досрочного 2022
        val = f'{n}'
        if n % 2 == 0:
            val += '10'
        else:
            val = '1' + val + '01'
        if int(val, 2) > 516:
            print(n)
            break
