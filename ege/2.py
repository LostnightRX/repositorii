for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(y <= x) or (z <= w) or not z)
                print([x, y, w, z] if not f else '')
