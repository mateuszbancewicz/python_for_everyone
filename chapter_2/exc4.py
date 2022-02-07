"""
Calculator for total cost of the car
"""


def car_salesman(price):
    tax = 0.02 * price
    dealer = 0.04 * price
    registration = 185
    delivery = 700
    result = price + tax + dealer + registration + delivery
    return f'Your total cost of the car: {result}'


if __name__ == '__main__':
    print('What is the price of the car?')
    print(car_salesman(price=float(input())))
