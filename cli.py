import funcsions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action=input("Type add,show,edit,complete or exit:\n>>>")
    user_action=user_action.strip()

    if user_action.startwith("add"):
        todo=user_action[4:] + "\n"

        todos = funcsions.get_todos()

        if todo in todos:
            print("This todo already added!!!")
            continue

        todos.append(todo+"\n")

        funcsions.write_todos(todos)

    elif user_action.startswith("show"):

        todos=funcsions.get_todos()

        new_todos=[item.strip("\n") for item in todos]

        for index,item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)
            number=number-1

            todos= funcsions.get_todos()

            new_todo=input("Enter a new todo: ")
            todos[number]=new_todo+"\n"

            funcsions.write_todos(todos)
        except ValueError:
            print("Your Command is not a valid")

            continue
    elif user_action.startswith("complete"):
        try:
                number=int(user_action[9:])

                todos= funcsions.get_todos()
                index=number-1
                todo_to_remove=todos[index].strip('\n')
                todos.pop(index)

                funcsions.write_todos(todos)
                message=f"Todo {todo_to_remove} was removed from the list."
                print(message)
        except IndexError:
            print("There is no item with that number")
            continue



    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!!!")

print('Bye!')
















