from typing import Callable, Dict, List, Tuple


def input_error(func: Callable) -> Callable:
    """Декоратор для обробки помилок"""

    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the correct arguments."

    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """parse input"""
    parts = user_input.split()
    cmd = parts[0].strip().lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    return cmd, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """add contact"""
    if len(args) < 2:
        raise ValueError("Not enough arguments provided.")

    name = " ".join(args[:-1]).strip()
    phone = args[-1].strip()
    contacts[name] = phone
    return f"Contact '{name}' added with phone number {phone}."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """edit contact"""
    if len(args) < 2:
        raise ValueError("Not enough arguments provided.")

    name = " ".join(args[:-1]).strip()
    phone = args[-1].strip()

    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated to phone number {phone}."
    else:
        raise KeyError(f"Contact '{name}' not found.")


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """show contact"""
    if len(args) == 0:
        raise IndexError("No contact name provided.")

    name = " ".join(args).strip()
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        raise KeyError(f"Contact '{name}' not found.")


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """show all contacts"""
    if not contacts:
        return "No contacts found."

    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def show_help() -> str:
    """print help"""
    help_text = """
    Available commands:
    - hello: Greet the bot.
    - add <name> <phone>: Add a new contact.
    - change <name> <new_phone>: Change an existing contact's phone number.
    - phone <name>: Show the phone number of a contact.
    - all: Show all contacts.
    - close or exit: Exit the bot.
    - help: Show this help message.
    """
    return help_text.strip()


def main() -> None:
    """main"""
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hello! How can I assist you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
