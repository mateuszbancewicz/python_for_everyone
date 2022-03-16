ATTRIBUTE_POINTS = 30
STRENGTH = 1
HEALTH = 10
WISDOM = 1
DEXTERITY = 1

ATTRIBUTE = {
    '1': 'STRENGTH',
    '2': 'HEALTH',
    '3': 'WISDOM',
    '4': 'DEXTERITY'
}


def attribute_check(quantity, attribute):
    if quantity + attribute < 1:
        return "You can't have stats below 1"
    attribute = attribute + quantity
    return attribute


def attribute_manager(attribute, attribute_points, character_attribute):
    print(f'You choose {ATTRIBUTE[attribute]}')
    quantity = int(input('''You can add or remove point. Enter a number + or -\n'''))
    attribute_points -= quantity
    if attribute_points < 0:
        print('Not enough points')
        return None, None

    if attribute == '2':
        quantity *= 10

    result = attribute_check(quantity=quantity, attribute=character_attribute)
    if isinstance(result, str):
        return None, None
    return result, attribute_points


def character_creator():
    attribute_points = ATTRIBUTE_POINTS
    character = {
        ATTRIBUTE['1']: STRENGTH,
        ATTRIBUTE['2']: HEALTH,
        ATTRIBUTE['3']: WISDOM,
        ATTRIBUTE['4']: DEXTERITY
    }

    while attribute_points != 0:
        choice = input(f'''
        You have {attribute_points} attribute points to distribute
        Choose attribute to add or withdraw points:
        1. STRENGTH: {character['STRENGTH']}
        2. HEALTH: {character['HEALTH']}
        3. WISDOM: {character['WISDOM']}
        4. DEXTERITY: {character['DEXTERITY']}
        
        My choice:\n 
        ''')
        if choice in ['1', '2', '3', '4']:
            result, attribute_points = attribute_manager(
                attribute=choice,
                attribute_points=attribute_points,
                character_attribute=character[ATTRIBUTE[choice]]
            )
            if not result and not attribute_points:
                continue
            if result:
                character[ATTRIBUTE[choice]] = result

        else:
            print('Wrong number')

    return character


if __name__ == '__main__':
    print(character_creator())
