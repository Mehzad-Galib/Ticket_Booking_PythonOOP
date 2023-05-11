class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}  # dictionary of seats info
        self.show_list = []  # list of tuples

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        arr = []
        # converting row col nums to A1 B2 type
        for i in range(self.rows):
            col = []
            string = chr(i+65)
            temp = 1
            for j in range(self.cols):
                col.append(string+str(temp))
                temp += 1
            arr.append(col)

        self.seats[show_id] = arr

    def book_seats(self, customer_name, customer_phn, show_id_given, list_tup):
        check = False
        for show_id, show_seats in self.seats.items():
            if show_id == show_id_given:
                check = True
                a, b = list_tup[0], list_tup[1]

                row = chr(a+65-1)
                col = str(b)
                seat_letter_lst = list()
                seat_letter_lst.append(row)
                seat_letter_lst.append(col)
                # converting (2,3) to B3
                seat_letter = ''.join(seat_letter_lst)

                try:

                    if show_seats[a-1][b-1] != 'XX':

                        show_seats[a-1][b-1] = 'XX'
                        self.seats[show_id] = show_seats
                        print(f'{seat_letter} BOOKED SUCCESSFULLY')
                        return seat_letter

                    else:
                        # SEAT WAS ALREADY BOOKED
                        print(f'{seat_letter} IS ALREADY BOOKED\n')
                        seat_letter = ''
                        # return seat_letter
                except IndexError:
                    print('Invalid Row Column\n')
                    seat_letter = ''

                except NameError:
                    print('Invalid Seat Chosen\n')
                    seat_letter = ''

                except ValueError:
                    print('Invalid input given\n')
                    seat_letter = ''

                finally:

                    return seat_letter

            # if show id is not correct

        if check:
            pass
        else:
            print('SHOW ID NOT FOUND')

    def view_show_list(self) -> None:
        print('SHOW ID'+' '*30 + 'SHOW NAME' + ' '*30
              + 'SHOW TIME\n' + '-'*85)
        for (show_id, show_name, show_time) in self.show_list:
            print(show_id+' '*32+show_name + ' '*30 + show_time)

        print('-'*85)

    def customer_show(self, show_id):
        for (a, b, c) in self.show_list:
            if a == show_id:
                print(f'SHOW NAME: {b}'+' '*25 + f'TIME: {c}')

        print('HALL NO: ' + self.hall_no)

    def id_validation(self, show_id):
        check = False
        for (a, b, c) in self.show_list:
            if a == show_id:
                check = True
                print(f'SHOW NAME: {b}'+' '*25 + f'TIME: {c}')

        return check

    def view_available_seats(self, show_id):
        check = False
        for key, value in self.seats.items():
            if key == show_id:
                check = True
                print(
                    '\nAVAILABLE SEATS ARE SHOWN BELOW\n[N.B: XX MEANS ALREADY BOOKED SEAT(S)]\n')
                for (a, b, c) in self.show_list:
                    if a == show_id:
                        print(
                            f'SHOW ID: {show_id}     ||     SHOW NAME: {b}     || TIME: {c}')
                        break

                print('-'*70)
                for i in value:
                    for j in i:
                        print(j, end=" "*15)
                    print()

                print('-'*70)
        if check:
            return ''
        else:
            print('WRONG ID FOR SHOW, PLEASE TRY AGAIN')
            return ''


class Star_Cinema(Hall):
    def __init__(self) -> None:
        self.hall_list = []

    def entry_hall(self, value):
        self.hall_list.append(value)


# initialized an object of class Hall
hall_one = Hall(5, 5, 'A10')

star_sineplex = Star_Cinema()

star_sineplex.entry_hall(hall_one)

hall_one.entry_show('ae123', 'BLACK ADAM', '12:00 AM')
hall_one.entry_show('bc245', 'SPIDER-MAN', '03:00 PM')
hall_one.entry_show('zp785', 'INCEPTION ', '06:00 PM')

print("WELCOME TO STAR SINEPLEX, RAJSHAHI-----------")

while True:
    print("1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKETS\n4. EXIT")
    option = int(input("ENTER OPTION: "))

    if option == 1:
        print(hall_one.view_show_list())

    if option == 2:
        id_show = input('ENTER SHOW ID: ')
        hall_one.view_available_seats(id_show)

    if option == 3:

        id_show = input('ENTER SHOW ID: ')
        id_check = hall_one.id_validation(id_show)

        if id_check == False:
            print('SHOW ID NOT MATCHED, PLEASE TRY AGAIN!!!')
            continue

        name = input("ENTER YOUR NAME: ")
        phone_num = input("ENTER YOUR PHONE NUMBER: ")
        hall_one.view_available_seats(id_show)
        total_seats = int(input('HOW MANY SEATS: '))
        seat_lst = list()

        for i in range(total_seats):
            flag = True
            while flag:

                seat_no = input('CHOOSE YOUR SEAT:')
                row = ord(seat_no[0]) - 65 + 1
                try:

                    col = int(seat_no[1])

                except ValueError:
                    print('Invalid input given')
                    continue
                seat_letter = hall_one.book_seats(
                    name, phone_num, id_show, (row, col))  # RETURNED SEAT LETTER ,either B3 or ''

                if seat_letter == '':
                    print('PLEASE CHOOSE YOUR SEAT AGAIN')
                    continue

                else:
                    seat_lst.append(seat_letter)
                    flag = False

        seat_lst_set = set(seat_lst)
        print('\n')
        # print(len(seat_lst_set))
        if len(seat_lst_set) != 0:

            print('-'*20 + 'PURCHASE INFORMATION' + '-'*25)

            print(f'CUSTOMER NAME: {name}' + ' ' *
                  25 + f'PHONE NUMBER: {phone_num}')
            hall_one.customer_show(id_show)
            print(f'{len(seat_lst_set)} BOOKED SEATS ARE: ' +
                  ' '.join(map(str, seat_lst_set)))

        else:
            print('NO TICKET BOOKED')

    if option == 4:
        break
