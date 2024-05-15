import json

with open("training_logs.json", "r") as f:
    database = json.load(f)

level = -1


def elem_list(data):
    for element in data:
        global level
        level += 1
        print(f'{"  " * level}- {element["type"]}')
        if "activities" in element:
            elem_list(element["activities"])
        level -= 1


instructions = "List of commands:\n" \
               "- 'list'- shows list of activities\n" \
               "- 'help' - shows the full list of possible commands\n" \
               "- 'exit' - exit from this program\n" \
               "-  any other command not listed above error message."



def start(arg):
    while True:
        command = str(input("\nCommand: "))
        if command == "list":
            elem_list(arg)
        elif command == "help":
            print(instructions)
        elif command == "exit":
            print("Exiting from this program")
            break
        else:
            print("Such command does not exist. Type 'help' and press 'enter' to see relevant commands.")

print("Welcome to 'BeSportive Py' ver. 0.0.1")
print(instructions)
start(database)
