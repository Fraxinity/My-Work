import array as wah
def arrays():
    tako = int(input("Enter 1 to input a number or 0 to terminate: "))
    wah = []
    while tako == 1:
        Ina = int(input("Enter input: "))
        wah.append(Ina)
        tako = int(input("Enter 1 to input a number or 0 to terminate: "))
        if tako == 0:
            break
    print(wah)
arrays()