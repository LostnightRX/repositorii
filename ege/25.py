for i in range(2023, 10**10, 2023):
    num = str(i)
    if num[0] == '1' and num[2:6] == '2139' and num[-1] == '4':
        print(i, i//2023)
