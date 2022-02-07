"""
Tip calculator
"""


def tip_calculator(bill):
    fifteen_percent = bill * 0.15
    twenty_percent = bill * 0.2
    return f'15% tip = {fifteen_percent}\n20% tip = {twenty_percent}'


if __name__ == '__main__':
    print('How much you will pay?')
    print(tip_calculator(bill=float(input())))

