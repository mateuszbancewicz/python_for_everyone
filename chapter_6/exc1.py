def ask_number(question, low, high, step=1):
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response
