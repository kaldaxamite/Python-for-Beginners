command = ""
while command != "quit":
    command = input ("> "),()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("Sorry,I don't understand that")
