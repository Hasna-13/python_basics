shopping_list = []

while True:
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Check item")
    print("5. Exit")

    choice = input("Choice: ").strip()
    print("DEBUG: you typed ->", repr(choice))   # shows hidden spaces

    if choice == "1":
        item = input("Enter item: ").strip()
        shopping_list.append(item)
        print(f"Added '{item}' to list")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed '{item}' from the list")
        else:
            print(f"{item} not found in list")

    elif choice == "3":
        print("Current list:", shopping_list)

    elif choice == "4":
        item = input("Enter item to check: ").strip()
        print("DEBUG: check item ->", repr(item))
        if item in shopping_list:
            print(f"{item} is in the list")
        else:
            print(f"{item} is not in the list")

    elif choice == "5":
        print("Goodbye! 🛒")
        break

    else:
        print("Invalid choice, try again")
