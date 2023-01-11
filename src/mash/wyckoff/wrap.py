def toCell(data):
    wrapped = []
    for pos in data:
        if pos >= 1.0:
            wrapped.append(pos - 1.0)
        elif pos < 0.0:
            wrapped.append(pos + 1.0)
        else:
            wrapped.append(pos)
    return wrapped
