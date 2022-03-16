CHILD_PARENT = {
    'Patricia': 'Violet',
    'Matthew': 'John',
    'John': 'John',
    'Aleksandra': 'Jola'
}


def parent_finder(child, child_parent):
    return child_parent[child]


if __name__ == '__main__':
    print(f'''
        Get to know parent of the person from the list:
        {CHILD_PARENT.keys()}
    ''')
    choice = input('Please choose someone: ')
    print(parent_finder(child=choice, child_parent=CHILD_PARENT))
