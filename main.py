from classes import AddressBook
from parsing import parse_input
from functions import (
    command_add,
    command_change,
    command_phone,
    command_all,
    command_add_birthday,
    command_show_birthday,
    birthdays,
)
from saving import save_data, load_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(command_add(args, book))

        elif command == "change":
            print(
                command_change(args, book)
            )  # Зробив шо потрібно вказувати старий номер так як він може бути не один

        elif command == "phone":
            print(command_phone(args, book))

        elif command == "all":
            print(command_all(book))

        elif command == "add-birthday":
            print(command_add_birthday(args, book))

        elif command == "show-birthday":
            print(command_show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
