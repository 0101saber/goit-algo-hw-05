def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def is_contact(name, contacts) -> bool:
    if contacts.get(name):
        return True
    else:
        return False


@input_error
def find_contact(args, contacts):
    name = args
    if is_contact(name, contacts):
        return contacts[name]
    else:
        return 'Contact name not found.'


@input_error
def change_contact(args, contacts):
    name, phone = args
    if is_contact(name, contacts):
        contacts[name] = phone
        return "Contact change."
    return 'Contact not change.'


def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        command, *args = parse_input(input("Enter a command: "))

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args[0], contacts))
        elif command == "all":
            print("Name   Phone")
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
