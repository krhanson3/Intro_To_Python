def print_menu():
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')

def get_num_of_non_WS_characters(text):
    non_whitespace = len(text) - text.count(' ')
    return non_whitespace

def execute_menu(choice, text):
    if choice == 'c':
        num_non_whitespace = get_num_of_non_WS_characters(text)
        print(f'Number of non-whitespace characters: {num_non_whitespace}')
    # elif choice == 'w':
        
    # elif choice == 'f':

    # elif choice == 'r':

    # elif choice == 's':

    # elif choice == 'q':
    #     print('Goodbye!')
    


if __name__ == '__main__':
    full_string = input('Enter a sample text:\n')
    print('\nYou entered:', full_string, '\n')
    print_menu()
    choice = input('\nChoose an option:\n')
    options = ['c', 'w', 'f', 'r', 's', 'q']
    
    while 1:
        if choice not in options:
            print('Invalid choice. Please try again.')
            choice = input('Choose an option:\n')

        elif choice in options:
            execute_menu(choice, full_string)
            print()
            print_menu()
            choice = input('\nChoose an option:\n')
    
    