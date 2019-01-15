def best_stock(data):
    max = bool(0)
    best_position = ' '
    for i in data:
        if data[i] > max:
            max = data[i]
            best_position = i

    print(best_position)


best_stock({'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2})== 'ATX', "First"
