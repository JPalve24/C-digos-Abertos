carros = ["HRV","Polo","Jetta","Cruze","Fusion"]

itcarros = iter(carros)
while itcarros:
    try:
        print(next(itcarros))
    except StopIteration:
        break