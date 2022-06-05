x = 10
Booked_seat = 0
Row = 8
Seats = 9
Total_seat = Row * Seats

class chart:

    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j + 1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart



class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('1 for Show the seats')
    print('2 for Buy a Ticket')
    print('0 for Exit')
    x = int(input('Select Option - '))
    if x == 1:
        for seat in range(Seats):
            print(seat, end='  ')
        print(Seats)

        if Seats == 9:
            for num in table_of_chart.keys():
                print(int(num) + 1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()

        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif x == 2:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        conform = input('yes for booking and no for Stop booking - ')

        if conform == 'yes':
            table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
            Booked_seat += 1

        else:

            print('This seat already booked by some one')
    else:

            print('***  Invalid Input  ***')
            print()
