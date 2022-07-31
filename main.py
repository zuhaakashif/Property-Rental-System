import PySimpleGUI as pg
from data import ticket_details, customer_info_list, rec_list, duration_and_facilities_list, add_costs, normal_bill, budget_and_guest_list                
from random import randint
from abc import ABC, abstractmethod

                                                     #list to store the user's budget and number of guests


#abstract class to handle errors using GUI
class ErrorClass(ABC):

    @abstractmethod
    def popup_method1(self):
        pass

    @abstractmethod
    def popup_method2(self):
        pass

#class that contains methods which calculates the total cost and displays the final window
class Bill:

    #method to calculate the bill before discount
    def total_bill(self):

        global total_reciept
        total_reciept = sum(add_costs) + sum(normal_bill) * int(duration_of_stay)
        return total_reciept

    #method to calculate the discounted bill
    def discounted_bill(self):

        global discount_var
        discount_var = 0
        if 0 < total_reciept <= 5000:
            discount_var = 0.95

        elif 5000 < total_reciept <= 10000:
            discount_var = 0.90

        elif total_reciept > 10000:
            discount_var = 0.85

        discounted_variable = int(total_reciept * discount_var)

        return discounted_variable

    #method to show the user the details of their booking
    def final_screen(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("    BOOKING INFORMATION -", size = (25, 3), font = ("MonoLisa"))
            ],
            [
                pg.Text("{}".format(customer_info_list[0]), font = ("MonoLisa"))
            ],
            [
                pg.Text("{}".format(customer_info_list[3]), font = ("MonoLisa"))
            ],
            [
                pg.Text("{}".format(customer_info_list[4]), font = ("MonoLisa"))
            ],
            [
                pg.Text("Type:", font = ("MonoLisa")),
                pg.Text("{}".format(rec_list[0]), font = ("MonoLisa")),
                pg.Text(" {}".format(rec_list[1]), font = ("MonoLisa")),

            ],
            [
                pg.Text("Booking No: ",font = ("MonoLisa")),
                pg.Text(randint(1,1000), font = ("MonoLisa"))
            ],
            [
                pg.Text("Additional Costs: ",font = ("MonoLisa")),
                pg.Text(sum(add_costs), font = ("MonoLisa")),pg.Text("Rs",font = ("MonoLisa"))
            ],
            [
                pg.Text("Total Bill: ", font = ("MonoLisa")),
                pg.Text(objBill.total_bill(), font = ("MonoLisa")),pg.Text("Rs",font = ("MonoLisa"))
            ],
            [
                pg.Text("Discounted Bill: ",font = ("MonoLisa")),
                pg.Text(objBill.discounted_bill(),font = ("MonoLisa")),pg.Text("Rs",font = ("MonoLisa"))
            ],
            [
                pg.Text("THANK YOU!",font = ("MonoLisa"))
            ],
            [
                pg.Button("EXIT")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Customer Information", layout, size=(550, 400))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED or event == "EXIT":
                customer_info_list.clear()
                duration_and_facilities_list.clear()  # clearing all the lists after the booking is done so the new user can use the program
                add_costs.clear()
                normal_bill.clear()
                budget_and_guest_list.clear()
                window.close()
                break


#class that contains important features of the program
#using mulitlevel inheritance to inherit the error handling and cost calculation classes
class A(Bill, ErrorClass):

    def budget_and_guest(self):

        pg.theme("SandyBeach")

        budget_and_guest_column = [
            [
                pg.Text("What is your budget? : ", size=(17, 1), font = ("MonoLisa")),
            ],
            [
                pg.Radio("0-5000Rs", "group 1", font = ("MonoLisa")),
                pg.Radio("5-10,000Rs", "group 1", font = ("MonoLisa")),
                pg.Radio("10-15,000Rs", "group 1", font = ("MonoLisa")),
            ],
            [
                pg.Text("No of Guests : ", size=(11, 1), font = ("MonoLisa")),
            ],
            [
                pg.Radio("1", "group 2", font = ("MonoLisa")),
                pg.Radio("2", "group 2", font = ("MonoLisa")),
                pg.Radio("3+", "group 2", font = ("MonoLisa")),

            ],
            [
                pg.Button("OK")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(budget_and_guest_column, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Customer Information", layout, size=(500, 300))


        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break

            elif event == "OK":
                window.close()

                if customer_info_list[4]== "Choice of accomodation: Hotel":
                    if values[0] == True:
                        choice = "0-5000Rs"
                        budget_and_guest_list.append(f"Budget: {choice}")

                    if values[1] == True:
                        choice = "5-10,000Rs"
                        budget_and_guest_list.append(f"Budget: {choice}")

                    if values[2] == True:
                        choice = "10-15,000Rs"
                        budget_and_guest_list.append(f"Budget: {choice}")

                    if values[3] == True:
                        choice = "1"
                        budget_and_guest_list.append(f"Guest: {choice}")

                    if values[4] == True:
                        choice = "2"
                        budget_and_guest_list.append(f"Guest: {choice}")

                    if values[5] == True:
                        choice = "3+"
                        budget_and_guest_list.append(f"Guest: {choice}")

                    elif (values[0] == False and values[1] == False and values[2] == False) or (
                            values[3] == False and values[4] == False and values[5] == False):
                        objA.popup_method1()


                    if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 1":
                        rec_list.append("3 Star Hotel")
                        rec_list.append("1-room")
                        normal_bill.append(4000)

                    if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 2":
                        rec_list.append("3 Star Hotel")
                        rec_list.append("2-room")
                        normal_bill.append(4500)

                    if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                        rec_list.append("3 Star Hotel")
                        rec_list.append("Suite")
                        normal_bill.append(50000)

                    if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                        rec_list.append("4 Star Hotel")
                        rec_list.append("1-room")
                        normal_bill.append(8000)

                    if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                        rec_list.append("4 Star Hotel")
                        rec_list.append("2-room")
                        normal_bill.append(9000)

                    if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                        rec_list.append("4 Star Hotel")
                        rec_list.append("Suite")
                        normal_bill.append(10000)

                    if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                        rec_list.append("5 Star Hotel")
                        rec_list.append("1-room")
                        normal_bill.append(13000)

                    if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                        rec_list.append("5 Star Hotel")
                        rec_list.append("2-room")
                        normal_bill.append(14000)

                    if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                        rec_list.append("5 Star Hotel")
                        rec_list.append("Suite")
                        normal_bill.append(15000)



                if customer_info_list[4] == "Choice of accomodation: Villa":
                        if values[0] == True:
                            choice = "0-5000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[1] == True:
                            choice = "5-10,000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[2] == True:
                            choice = "10-15,000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[3] == True:
                            choice = "1"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        if values[4] == True:
                            choice = "2"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        if values[5] == True:
                            choice = "3+"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        elif (values[0] == False and values[1] == False and values[2] == False) or (
                                values[3] == False and values[4] == False and values[5] == False):
                            objA.popup_method1()

                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Single Villa")
                            rec_list.append("1-room")
                            normal_bill.append(4000)

                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Single Villa")
                            rec_list.append("2-room")
                            normal_bill.append(4500)

                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Single Villa")
                            rec_list.append("3-room")
                            normal_bill.append(5000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Garden Villa")
                            rec_list.append("1-room")
                            normal_bill.append(8000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Garden Villa")
                            rec_list.append("2-room")
                            normal_bill.append(9000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Garden Villa")
                            rec_list.append("3-room")
                            normal_bill.append(10000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Luxury Villa")
                            rec_list.append("1-room")
                            normal_bill.append(13000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Luxury Villa")
                            rec_list.append("2-room")
                            normal_bill.append(14000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Luxury Villa")
                            rec_list.append("3-room")
                            normal_bill.append(15000)


                if customer_info_list[4] == "Choice of accomodation: Apartment":
                        if values[0] == True:
                            choice = "0-5000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[1] == True:
                            choice = "5-10,000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[2] == True:
                            choice = "10-15,000Rs"
                            budget_and_guest_list.append(f"Budget: {choice}")

                        if values[3] == True:
                            choice = "1"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        if values[4] == True:
                            choice = "2"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        if values[5] == True:
                            choice = "3+"
                            budget_and_guest_list.append(f"Guest: {choice}")

                        elif (values[0] == False and values[1] == False and values[2] == False) or (
                                values[3] == False and values[4] == False and values[5] == False):
                            objA.popup_method1()


                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Basic Apartment")
                            rec_list.append("1-room")
                            normal_bill.append(4000)

                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Basic Apartment")
                            rec_list.append("2-room")
                            normal_bill.append(4500)

                        if budget_and_guest_list[0] == "Budget: 0-5000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Basic Apartment")
                            rec_list.append("3-room")
                            normal_bill.append(5000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Deluxe Apartment")
                            rec_list.append("1-room")
                            normal_bill.append(8000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Deluxe Apartment")
                            rec_list.append("2-room")
                            normal_bill.append(9000)

                        if budget_and_guest_list[0] == "Budget: 5-10,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Deluxe Apartment")
                            rec_list.append("3-room")
                            normal_bill.append(10000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 1":
                            rec_list.append("Executive Apartment")
                            rec_list.append("1-room")
                            normal_bill.append(13000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 2":
                            rec_list.append("Executive Apartment")
                            rec_list.append("2-room")
                            normal_bill.append(14000)

                        if budget_and_guest_list[0] == "Budget: 10-15,000Rs" and budget_and_guest_list[1] == "Guest: 3+":
                            rec_list.append("Executive Apartment")
                            rec_list.append("3-room")
                            normal_bill.append(15000)


                objA.recommend()

    #method that recommends the user a suitable accommodation
    def recommend(self):

        pg.theme("SandyBeach")
        screen_to_be_centered = [
            [pg.Text("    WE RECOMMEND YOU -", size = (25, 2), font = ("MonoLisa"))],

            [pg.Text("{}".format(rec_list[0]), font = ("MonoLisa"))],
            [pg.Text("{}".format(rec_list[1]),font = ("MonoLisa"))],
            [pg.Text("Are you happy with our recommendation?", font = ("MonoLisa"))],
            [pg.Button("YES"), pg.Button("NO")]

        ]
        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(screen_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]
        window = pg.Window("Customer Information", layout, size=(500, 300))
        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break

            if event == "YES":
                window.close()
                objA.duration_and_facilites()
            if event == "NO":
                budget_and_guest_list.clear()
                rec_list.clear()
                window.close()
                objA.budget_and_guest()

    #method to ask the user the duration of stay and what additional facilites they'll be using
    def duration_and_facilites(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("How many nights would you like to stay with us? (Enter Number) : ", font = ("MonoLisa")),
            ],
            [
                pg.InputText(size = (14,2))
            ],
            [
                pg.Text("ADDITIONAL FACILITIES : ", font = ("MonoLisa"))
            ],
            [
                pg.Text("Wi-Fi (500Rs) : ", font = ("MonoLisa")),
                pg.Radio("Yes", "group 1", font = ("MonoLisa")),
                pg.Radio("No", "group 1", font = ("MonoLisa"))
            ],
            [
                pg.Text("Car Parking (200Rs) : ", font = ("MonoLisa")),
                pg.Radio("Yes", "group 2", font = ("MonoLisa")),
                pg.Radio("No", "group 2", font = ("MonoLisa"))
            ],
            [
                pg.Text("Room Service (500Rs) : ", font = ("MonoLisa")),
                pg.Radio("Yes", "group 3", font = ("MonoLisa")),
                pg.Radio("No", "group 3", font = ("MonoLisa"))
            ],
            [
                pg.Text("What Check-In option would you prefer? : ", font = ("MonoLisa"))
            ],
            [
                pg.Radio("Regular Check-In (No Cost)", "group 4", font = ("MonoLisa")),
                pg.Radio("Instant Check-In (350 Rs)", "group 4", font = ("MonoLisa"))
            ],
            [
                pg.Button("NEXT"),
                pg.Button("BACK")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Customer Information", layout, size=(500, 300))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break
            if event == "NEXT":

                duration_and_facilities_list2 = []

                window.close()
                duration_and_facilities_list.append(values[0])
                duration_and_facilities_list2.append(f"{values[0]}")
                global duration_of_stay
                duration_of_stay = duration_and_facilities_list[0]
                if values[0] == "":
                    duration_of_stay = 0

                if values[1] == True:
                    choice = "Yes"
                    duration_and_facilities_list.append(f"Wi-Fi: {choice}")
                    add_costs.append(500)

                if values[2] == True:
                    choice = "No"
                    duration_and_facilities_list.append(f"Wi-Fi: {choice}")

                if values[3] == True:
                    choice = "Yes"
                    duration_and_facilities_list.append(f"Car Parking: {choice}")
                    add_costs.append(200)

                if values[4] == True:
                    choice = "No"
                    duration_and_facilities_list.append(f"Car Parking: {choice}")

                if values[5] == True:
                    choice = "Yes"
                    duration_and_facilities_list.append(f"Room Service: {choice}")
                    add_costs.append(500)

                if values[6] == True:
                    choice = "No"
                    duration_and_facilities_list.append(f"Room Service: {choice}")

                if values[7] == True:
                    choice = "Regular Check-In"
                    duration_and_facilities_list.append(f"Check-In Option: {choice}")

                if values[8] == True:
                    choice = "Instant Check-In"
                    duration_and_facilities_list.append(f"Check-In Option: {choice}")
                    add_costs.append(350)

                #implemting error handling with a popup
                if values[0] == "" or (values[1] == False and values[2] == False) or (
                        values[3] == False and values[4] == False) or (values[5] == False and values[6] == False) or (
                        values[7] == False and values[8] == False):
                    objA.popup_method2()

                if values[0] == "" and values[1] == False and values[2] == False and values[3] == False and values[
                    4] == False and values[5] == False and values[6] == False and values[7] == False and values[
                    8] == False:
                    objA.popup_method2()

                objA.final_screen()

            if event == "BACK":
                window.close()
                objA.recommend()

    def popup_method1(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("Please fill out all checkboxes!")
            ],
            [
                pg.Button("Ok")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Error Message!", layout, size=(250, 100))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
            if event == "Ok":
                window.close()
                objA.budget_and_guest()


    def popup_method2(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("Please fill out all checkboxes and columns correctly!")
            ],
            [
                pg.Button("Ok")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Error Message!", layout, size=(250, 100))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
            if event == "Ok":
                window.close()
                objA.duration_and_facilites()

#class for the main menu and pre-booking feature
class B(A, ErrorClass):

    def print_ticket_screen1(self):
        pg.theme("SandyBeach")
        screen_to_be_centred = [

            [pg.Text("BOOKING DETAILS - ")],
            [pg.Text("NAME : {}".format(ticket_details[0]))],
            [pg.Text("CONTACT NO : {}".format(ticket_details[2]))],

            [pg.Text("CHOICE OF ACCOMMODATION : {}".format(ticket_details[4]))],
            [pg.Text("TYPE : {}".format(ticket_details[6]))],

            [pg.Text("BOOKING NO : {}".format(ticket_details[8]))],
            [pg.Text("ADDITIONAL COSTS : {}".format(ticket_details[10]))],
            [pg.Text("BILL BEFORE DISCOUNT : {}".format(ticket_details[14]))],
            [pg.Text("BILL AFTER DISCOUNT : {}".format(ticket_details[12]))],
            [pg.Button("BACK TO MAIN MENU")]

        ]
        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(screen_to_be_centred, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Ticket Display", layout, size=(500, 300))

        while True:
            event, values = window.read()

            if event == "OK":
                window.close()

            elif event == pg.WIN_CLOSED:
                window.close()
                break

            elif event == "BACK TO MAIN MENU":
                window.close()
                objB.main_screen()

    # method to display pre_booked booking details
    def print_ticket_screen2(self):
        pg.theme("SandyBeach")
        screen_to_be_centred = [

            [pg.Text("BOOKING DETAILS - ", font = ("MonoLisa"), size = (60, 1))],
            [pg.Text("NAME : {}".format(ticket_details[1]))],
            [pg.Text("CONTACT NO : {}".format(ticket_details[3]))],

            [pg.Text("CHOICE OF ACCOMMODATION : {}".format(ticket_details[5]))],
            [pg.Text("TYPE : {}".format(ticket_details[7]))],

            [pg.Text("BOOKING NO : {}".format(ticket_details[9]))],
            [pg.Text("ADDITIONAL COSTS : {}".format(ticket_details[11]))],
            [pg.Text("BILL BEFORE DISCOUNT : {}".format(ticket_details[15]))],
            [pg.Text("BILL AFTER DISCOUNT : {}".format(ticket_details[13]))],
            [pg.Button("BACK TO MAIN MENU")]

        ]
        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(screen_to_be_centred, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Ticket Display", layout, size=(500, 300))

        while True:
            event, values = window.read()

            if event == "OK":
                window.close()

            elif event == pg.WIN_CLOSED:
                window.close()
                break

            elif event == "BACK TO MAIN MENU":
                window.close()
                objB.main_screen()

    #method that shows the pre-booking screen and asks user for their booking number
    def pre_booking(self):
        pg.theme("SandyBeach")

        pre_booking_column =[
            [pg.Text("Enter your ticket number:", justification='center', size = (40,1), font = ("MonoLisa"))],
            [pg.InputText(justification='center', size = (40,1))],
            [pg.Button("OK", size = (40,1))],
            [pg.Button("BACK", size = (40,1))]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(pre_booking_column, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Pre-Booking", layout, size=(500, 300))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break

            elif event == "OK":
                window.close()

                if values[0] == "123":
                    objB.print_ticket_screen1()
                elif values[0] == "1234":
                    objB.print_ticket_screen2()
                elif values[0] != "123" or values[0] != "1234":
                    objB.popup_method2()


            elif event =="BACK":
                window.close()
                objB.main_screen()

    def make_reservation(self):

        pg.theme("SandyBeach")

        make_reservation_column = [
            [
                pg.Text("    CUSTOMER INFORMATION -", size = (25, 3), font = ("MonoLisa"))
            ],
            [
                pg.Text("Enter name: ", size = (14, 1), font = ("MonoLisa")),
                pg.InputText()
            ],
        [
                pg.Text("Enter age: ", size = (14, 1),font = ("MonoLisa")),
                pg.InputText()
            ],
        [
                pg.Text("Enter E-mail ID: ", size = (14, 1), font = ("MonoLisa")),
                pg.InputText()
            ],
        [
                pg.Text("Enter Contact No: ", size = (14, 1), font = ("MonoLisa")),
                pg.InputText()
            ],
            [
                pg.Text("Type of accommodation: ", font = ("MonoLisa")),
                pg.Radio("Apartment", "group 1", font = ("MonoLisa")),
                pg.Radio("Villa", "group 1", font = ("MonoLisa")),
                pg.Radio("Hotel", "group 1", font = ("MonoLisa")),
            ],
            [
                pg.Button("OK"),
                pg.Button("BACK")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(make_reservation_column, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Customer Information", layout, size = (500, 300))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break

            elif event == "BACK":
                window.close()
                objB.main_screen()

            elif event == "OK":
                customer_info_list2 = []

                window.close()
                customer_info_list.append(f"Name: {values[0]}")
                customer_info_list.append(f"Age: {values[1]}")
                customer_info_list.append(f"E-mail ID: {values[2]}")
                customer_info_list.append(f"Contact No: {values[3]}")
                customer_info_list2.append(f"{values[0]}")
                customer_info_list2.append(f"{values[1]}")
                customer_info_list2.append(f"{values[2]}")
                customer_info_list2.append(f"{values[3]}")
                customer_info_list3 = [i for i in customer_info_list2 if len(i)>1]


                if values[4] == True:
                    choice = "Apartment"
                    customer_info_list.append(f"Choice of accomodation: {choice}")

                if values[5] == True:
                    choice = "Villa"
                    customer_info_list.append(f"Choice of accomodation: {choice}")

                if values[6] == True:
                    choice = "Hotel"
                    customer_info_list.append(f"Choice of accomodation: {choice}")

                if len(customer_info_list3) < 4 or (values[4] == False and values[5] == False and values[6] == False):
                    objB.popup_method1()

                objB.budget_and_guest()

    def main_screen(self):
        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("WELCOME TO THE PROPERTY RENTAL SYSTEM!", justification='center', size = (50,3), font = ("MonoLisa"))
            ],
            [
                pg.Text("Choose an option - \n", justification='center', size = (40,1), font = ("MonoLisa"))
            ],
            [
                pg.Button("PRE-BOOKINGS",size=(40,1))
            ],
            [
                pg.Button("MAKE A RESERVATION", size=(40,1))
            ],
            [
                pg.Button("EXIT", size=(40,1))
            ]
        ]


        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Property Rental System", layout, size = (500,300))

        while True:
            event, values = window.read()
            if event == "EXIT" or event == pg.WIN_CLOSED:
                break
            elif event == "PRE-BOOKINGS":
                window.close()
                objB.pre_booking()
            elif event == "MAKE A RESERVATION":
                window.close()
                objB.make_reservation()

    def popup_method1(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("Please fill out all the columns!")
            ],
            [
                pg.Button("Ok")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Error Message!", layout, size=(250, 100))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break
            if event == "Ok":
                window.close()
                objB.make_reservation()

    def popup_method2(self):

        pg.theme("SandyBeach")

        column_to_be_centered = [
            [
                pg.Text("Please enter correct ticket number!")
            ],
            [
                pg.Button("Ok")
            ]
        ]

        layout = [[pg.VPush()],
                  [pg.Push(), pg.Column(column_to_be_centered, element_justification='c'), pg.Push()],
                  [pg.VPush()]]

        window = pg.Window("Error Message!", layout, size=(250, 100))

        while True:
            event, values = window.read()

            if event == pg.WIN_CLOSED:
                window.close()
                break
            if event == "Ok":
                window.close()
                objB.pre_booking()





objA = A()
objB = B()
objBill = Bill()
objB.main_screen()                                               #calling the main screen method to initiate the program
