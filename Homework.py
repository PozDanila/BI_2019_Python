empty = []
    for b in data:
        if data.count(b) == 1:
            empty.append(b)
    for e in empty:
        data.remove(e)