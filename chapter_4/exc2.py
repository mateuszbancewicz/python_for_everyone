def reverser(text: str):
    temp = text.replace(',', ' ,').replace('.', ' .').replace('-', ' - ').split(' ')
    result = ''
    dot = ''
    for word in range(len(temp) - 1, -1, -1):
        if temp[word] == ',':
            result += temp[word] + ' '
        elif temp[word] == '.':
            dot += temp[word]
        else:
            result += temp[word] + ' '
    result += dot
    return result


if __name__ == '__main__':
    print(reverser(input("Print something: ")))
