# Define some colors:
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

# User's input parser:
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Error handling decorator:
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f'{RED}Give me name and phone please{RESET}.'
        except KeyError:
            return f'{RED}There is no such contact{RESET}.'
        except IndexError:
            return f'{RED}Gve me a name please{RESET}.'
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return f'{RED}Contact already exists{RESET}. \
{BLUE}Please use "change" command instead{RESET}.'
    else:
        contacts[name] = phone
        return f'{GREEN}Contact added{RESET}.'

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        return f'{RED}There is no such contact{RESET}. \
{BLUE}Please use "add" command instead{RESET}.'
    contacts[name] = phone
    return 'Contact updated.'

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f'{GREEN}{contacts[name]}{RESET}'

def show_all(contacts):
    contacts_list = []
    for name, contact in contacts.items():
        contacts_list.append(f'{GREEN}{name}{RESET} - {BLUE}{contact}{RESET}')
    return contacts_list

# ===================== Main ========================
def main():
    contacts = {
        'Leo': '123',
        'Mike': '456',
        'Donny': '789',
        'Raf': 'not-at-home'
    }
    print(f'{GREEN}Welcome to the assistant bot{RESET}!')
    while True:
        user_input = input('Enter a command: ')

        if not user_input:
            print(f'{RED}Expecting a command{RESET}.')
            print(f'Available commands are: \
{BLUE}hello, add, change, phone, all, close, exit{RESET}.')
            continue

        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print(f'{GREEN}Good bye{RESET}!')
            break
        elif command == 'hello':
            print(f'{GREEN}How can I help you{RESET}?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))     
        elif command == 'all':
            for line in show_all(contacts):
                print(line)             
        else:
            print(f'{RED}Invalid command{RESET}.')
            print(f'Available commands are: \
{BLUE}hello, add, change, phone, all, close, exit{RESET}.')

if __name__ == '__main__':
    main()
