def counter(start, end, step):
    for i in range(start, end, step):
        print(f'{i} ', end="")


if __name__ == '__main__':
    start = int(input("Give me a start number: "))
    end = int(input("Now give me a finish number: "))
    step = int(input("Step size: "))

    counter(start=start, end=end + 1, step=step)
