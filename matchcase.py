a = int(input("Enter number:"))

match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 13:
        print("case is 13")
    case 23:
        print("case is 23")
    case _:
        print("No match found")

