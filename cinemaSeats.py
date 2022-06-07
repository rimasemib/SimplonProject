x = 3

seats = []
seats.append(["vacant", "booked", "vacant", "vacant", "booked", "vacant", "vacant", "vacant"])
seats.append(["vacant", "vacant", "booked", "vacant", "vacant", "booked", "vacant", "vacant"])
seats.append(["booked", "vacant", "vacant", "booked", "vacant", "vacant", "vacant", "vacant"])
seats.append(["vacant", "vacant", "vacant", "vacant", "vacant", "vacant", "booked", "booked"])
seats.append(["booked", "vacant", "booked", "vacant", "vacant", "vacant", "vacant", "vacant"])
seats.append(["vacant", "booked", "vacant", "booked", "vacant", "vacant", "vacant", "vacant"])


while x != 0:
    print('1 for Show the seats')
    print('2 for Buy a Ticket')

    x = int(input('Select Option - '))
    if x == 1:
        print("")
        print("======================================")
        print("")
        for row in seats:
            print(row)
        print("")
        print("======================================")

        print()

    elif x == 2:
        row = int(input("Enter a row number (between 0 and 5)"))
        column = int(input("Enter a column number (between 0 and 7)"))

        if seats[row][column] == "booked":
            print("This seat is already booked.")
        else:
            print("This seat is vacant.")
