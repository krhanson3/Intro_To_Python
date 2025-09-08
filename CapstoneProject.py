def print_menu():
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')

def get_num_of_non_WS_characters(text):
    non_whitespace = 0
    for i in text:
        if i != ' ' and i != '\n' and i != '\t':
            non_whitespace += 1
    return non_whitespace

def get_num_of_words(text):
    new_string = text.split()
    #split returns a list of words ignoring spaces and punctuation
    return len(new_string)

def fix_capitalization(text):
    num_fixed = 0
    need_to_capitalize = True
    new_string = ''

    for char in text: 
        if need_to_capitalize and char.islower():
            new_string += char.upper()
            num_fixed += 1
            need_to_capitalize = False
        else:
            new_string += char
            if char.isalpha():
                need_to_capitalize = False
        if char in ['.', '!', '?']:
            need_to_capitalize = True

    return new_string, num_fixed
   
def replace_punctuation(text):
    exclamation_count = 0
    semicolon_count = 0
    new_string = ''
    for i in text:
        if i == '!':
            exclamation_count += 1
            new_string += '.'
        elif i == ';':
            semicolon_count += 1 
            new_string += ','
        else: 
            new_string += i 
    return new_string, exclamation_count, semicolon_count

def shorten_space(text):
    new_string = ''
    prev_char = ''
    for i in text:
        if i == ' ' and prev_char == ' ':
            prev_char = i
            continue
        new_string += i
        prev_char = i
    return new_string      

def execute_menu(choice, text):
    if choice == 'c':
        num_non_whitespace = get_num_of_non_WS_characters(text)
        print(f'Number of non-whitespace characters: {num_non_whitespace}')
    elif choice == 'w':
        num_words = get_num_of_words(text)
        print(f'Number of words: {num_words}')   
    elif choice == 'f':
        new_string, num_fixed = fix_capitalization(text)
        print(f'Number of letters capitalized: {num_fixed}')
        print(f'Edited text: {new_string}')
    elif choice == 'r':
        new_string, exclamation_count, semicolon_count = replace_punctuation(text)
        print('Punctuation replaced')
        print(f'exclamation_count: {exclamation_count}')
        print(f'semicolon_count: {semicolon_count}')
        print(f'Edited text: {new_string}')
    elif choice == 's':
        new_string = shorten_space(text)
        print(f'Edited text: {new_string}')
    elif choice == 'q':
        quit()

if __name__ == '__main__':
    full_string = input('Enter a sample text:\n')
    print('\nYou entered:', full_string)
    print_menu()
    choice = input('Choose an option:\n')
    options = ['c', 'w', 'f', 'r', 's', 'q']
    
    while 1:
        if choice not in options:
            print('Invalid choice. Please try again.\n')
            choice = input('Choose an option:\n')

        elif choice in options:
            execute_menu(choice, full_string)
            print()
            print_menu()
            choice = input('\nChoose an option:\n')
    
    