def counter(start, end, step):
    for i in range(start, end, step):
        print(f'{i} ', end="")


if __name__ == '__main__':
    s = int(input("Give me a start number: "))
    e = int(input("Now give me a finish number: "))
    st = int(input("Step size: "))

    counter(start=s, end=e + 1, step=st)
