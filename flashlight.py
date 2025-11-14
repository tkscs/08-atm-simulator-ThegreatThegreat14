Current_State = "Off"
Current_Input = "N"

while True:
    if Current_State == "Off":
        print("The flashlight is off.")
    elif Current_State == "Red":
        print("The flashlight is red.")
    elif Current_State == "White":
        print("The flashlight is white.")

    Current_Input = input("You can click the button by entering C, hold the button by entering H, do nothing by entering N, or put the flashlight away by entering E. ")
   
    if Current_Input == "E":
        print("You have put the flashlight away.")
        break

    if Current_State == "Off":
        if Current_Input == "C":
            Current_State = "White"
        elif Current_Input == "H":
            Current_State = "Red"
        elif Current_Input == "N":
            Current_State = "Off"
        else:
            print("Please enter a valid input.")
    elif Current_State == "Red":
        if Current_Input == "C":
            Current_State = "Off"
        elif Current_Input == "H":
            Current_Input == "White"
        elif Current_Input == "N":
            Current_State = "Off"
        else:
            print("Please enter a valid input.")
    elif Current_State == "White":
        if Current_Input == "C":
            Current_State = "Off"
        elif Current_Input == "H":
            Current_State = "red"
        elif Current_Input == "N":
            Current_State = "Red"
        else:
            print("Please enter a valid input.")