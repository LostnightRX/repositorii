for A in range (2):
    for B in range (2):
        for C in range (2):
            if (((A and (not B))<= C) == A) == 0:
                print(A, B, C)
