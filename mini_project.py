print("Shopping List Manager")

shopping_list = []

while True:
    print("\nSelect what you want to do:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear all")
    print("5. Exit")

    choice = input("Choose option (1-5): ")

    if choice == "1":
        item = input("What item do you want to add? ")
        shopping_list.append(item)
        print(item, "added to the list!")

    elif choice == "2":
        item = input("What item do you want to remove? ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from the list!")
        else:
            print("Item not found!")

    elif choice == "3":
        print("Your list:")
        for i, item in enumerate(shopping_list, start=1):
            print(i, item)

    elif choice == "4":
        confirm = input("Are you sure? (y/n): ")
        if confirm == "y":
            shopping_list.clear()
            print("List cleared!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")