
def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if len(args[0]) == 1:
                return "Give me phone please."
            return "Give me name and phone please."
        except KeyError:
            return "Contact not find. Give me another name please."

    return inner


def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if len(args[0]) == 1:
                return "Give me phone please."
            return "Give me name and phone please."

    return inner


def input_error_find(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name please."
        except KeyError:
            return "Contact name not found."
        except IndexError:
            return "Give me name please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error_add
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error_find
def find_contact(args, contacts):
    name = args[0]
    return contacts[name]


@input_error_change
def change_contact(args, contacts):
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Contact change."


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
            print(find_contact(args, contacts))
        elif command == "all":
            print("Name   Phone")
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
