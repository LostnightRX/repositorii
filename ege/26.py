with open('26.txt') as f:
    s = [int(x) for x in f]
    s = sorted(s[1:], reverse = True)
    n, mini = 1, s[0]
    for i in range(1, len(s)):
        if s[i] + 3 <= mini:
            mini = s[i]
            n += 1
    print(n , mini)
