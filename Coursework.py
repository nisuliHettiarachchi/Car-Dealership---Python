
def system():
    print("\nThere are four roles for logging in:\n 1.Admin\n 2.Customer\n 3.Owner\n 4.Technician")
    user = int(input("Out of the above four, enter the number of your role! : "))
    if user == 1:
       admin_login()
    elif user == 2:
       customer_login()
    elif user == 3:
       owner_login()
    elif user == 4:
       technician_login()


def admin_login():
    print("\nHave a good day, Admin!")
    admin_password = 1234
    try:
        password_1 = int(input("\nEnter the admin password!"))
    except:
        print("Invalid Password")
    if password_1 == admin_password:
        remain_in_admin = 1
        while remain_in_admin == 1:
            car_sold_function()
            new_customer_function()
            new_car_function()
            cust_request()
            appointments()
            remain_in_admin = int(input("Do you want to remain as admin (1 = Yes or 2 = No): "))



def car_sold_function():
    car_sold = int(input("Was a car sold?(1=yes or 2=no): "))
    if car_sold == 1:
        sales_details = input("Enter the following car details in order with a blankspace to separate them; car_asking_price,carID,car_year,car_make,car_model: ")
        F = open("sold_car_details.txt", "a")
        F.writelines("%s\n" % sales_details)
        F.close()
        sales_price_details = input("Enter the following car details in order with a blankspace to separate them; carID,car_new_owner_name,car_new_owner_number,car_new_owner_city,car_selling_price: ")
        F = open("sold_car_owner_details.txt", "a")
        F.writelines("%s\n" % sales_price_details)
        F.close()



def new_customer_function():
    new_customer = int(input("Is there a new customer?(1=yes or 2=no): "))
    if new_customer == 1:
        information = input("Enter the following customer details in order with a blankspace to separate them; customer_name,car_ID_no,customer_DOB,customer_permanent_state,customer_phone_number: ")
        F = open("customer_details.txt", "a")
        F.writelines("%s\n" % information)
        F.close()

def new_car_function():
    new_car = int(input("Is there a new car for sale?(1=yes or 2=no): "))
    if new_car == 1:
        sale_car_data = input("Enter the following car details in order with a blankspace to separate them; car_mileage,carID,car_make,car_model,car_year,car_asking_price: ")
        F = open("cars_for_sale_mileage.txt", "a")
        F.writelines("%s\n" % sale_car_data)
        F.close()
        sale_car_data_2 = input("Enter the following car details in order with a blankspace to separate them; car_asking_price,car_mileage,carID,car_make,car_model,car_year: ")
        F = open("cars_for_sale_asking_price.txt", "a")
        F.writelines("%s\n" % sale_car_data_2)
        F.close()


def cust_request():
    print("\nLook if there are any new customer requests!")
    F = open("customer_requests.txt", "r")
    print(F.read())


def appointments():
    schedule = int(input("Do you need to schedule an appointment?(1=yes or 2=no): "))
    if schedule == 1:
        request_appointment = input("Enter the following details of the scheduled appointment in order with a blankspace to separate them; car_ID_no,date_of_appointment,time_of_appointment: ")
        F = open("appointment_schedule.txt", "a")
        F.writelines("%s\n" % request_appointment)
        F.close()



def customer_login():
    print("\nGood Day, Dear Customer!")
    remain_in_customer = 1
    while remain_in_customer == 1:
        print("\n1:Look at cars for sale in order of mileage \n2:Look at cars for sale in order of asking price \n3:Place a request \n4:Check for status of your appointment ")
        open_file = int(input("\nOut of the above options, input the index of your purpose: "))
        if open_file == 1:
            cars = []
            with open("cars_for_sale_mileage.txt") as readfile:
                for line in readfile:
                    cars.append(line.strip() + "\n")
            cars.sort()
            with open("sorted_cars.txt", "w") as newfile:
                for car in cars:
                    newfile.write(car)
            F = open("sorted_cars.txt", "r")
            print(F.read())
        elif open_file == 2:
            cars = []
            with open("cars_for_sale_asking_price.txt") as readfile2:
                for line in readfile2:
                    cars.append(line.strip() + "\n")
            cars.sort()
            with open("sorted_cars.txt", "w") as newfile:
                for car in cars:
                    newfile.write(car)
            F = open("sorted_cars.txt", "r")
            print(F.read())
        elif open_file == 3:
            print("21/03/2022 213451 I am in need of a car service")
            request = input("Mention your request after the date your car_ID and use a blankspace to separate them like shown above: ")
            F = open("customer_requests.txt", "a")
            F.writelines("%s\n" % request)
            F.close()
        else:
            print("This is the current scheduled list of appointments. Please give us 1 to 2 working days to schedule your appointment if not visible.")
            F = open("appointment_schedule.txt", "r")
            print(F.read())
        remain_in_customer = int(input("Do you still wish to continue as a customer (1 = Yes or 2 = No): "))


def report():
    print("\nThese are the details of our current customers!;")
    print("Each line consists of: customer's name, carID, customer's DOB, customer's permanent state, customer's phone number")
    F = open("customer_details.txt", "r")
    print(F.read())
    print("\nThese are the details of the cars we have sold so far;")
    print("Each line consists of: price the car was sold for,carID,car_year,car_make,car_model")
    F = open("sold_car_details.txt", "r")
    print(F.read())
    print("\nThese are the details of the services and maintenance jobs carried out so far!;")
    print("Each line consists of: date of service, carID, time of service, duration of service, technician_ID, price charged for service if any")
    F = open("service_details.txt", "r")
    print(F.read())
    profit_for_a_month()
    print("\nThe following graph shows the cumulative profit made in the previous months.")
    F = open("profit.txt", "r")
    read = F.readlines()
    profit_for_graph = []

    for line in read:
        if line[-1] == "\n":
            new = int(line[:-1])
            new_2 = new // 1000
            profit_for_graph.append(new_2)
        else:
            new = int(line[0:])
            new_2 = new // 1000
            profit_for_graph.append(new_2)
    num = 1
    print("\nY-axis/Month")
    print("    ^")
    for x in range(0, len(profit_for_graph)):
        if num == 1:
            month = "Jan"
        elif num == 2:
            month = "Feb"
        elif num == 3:
            month = "Mar"
        elif num == 4:
            month = "Apr"
        elif num == 5:
            month = "May"
        elif num == 6:
            month = "Jun"
        elif num == 7:
            month = "Jul"
        elif num == 8:
            month = "Aug"
        elif num == 9:
            month = "Sep"
        elif num == 10:
            month = "Oct"
        elif num == 11:
            month = "Nov"
        else:
            month = "Dec"
        print(month, "|", "*" * int(profit_for_graph[x]))
        num += 1
    print("   ", "0", "-" * 20, ">", "X-axis/Profit (1 * = $1000)")

    F = open("service_details.txt", "r")
    read = F.readlines()
    service_for_graph = []

    for line in read:
        if line[-1] == "\n":
            new = int(line[-3:-1])
            new_2 = new // 10
            service_for_graph.append(new_2)
        else:
            new = int(line[-2:])
            new_2 = new // 10
            service_for_graph.append(new_2)
    print("\nThe following graph shows the income made by the maintenance jobs in the previous months.")
    num = 1
    print("\nY-axis/Month")
    print("    ^")
    for x in range(0, len(service_for_graph)):
        if num == 1:
            month = "Jan"
        elif num == 2:
            month = "Feb"
        elif num == 3:
            month = "Mar"
        elif num == 4:
            month = "Apr"
        elif num == 5:
            month = "May"
        elif num == 6:
            month = "Jun"
        elif num == 7:
            month = "Jul"
        elif num == 8:
            month = "Aug"
        elif num == 9:
            month = "Sep"
        elif num == 10:
            month = "Oct"
        elif num == 11:
            month = "Nov"
        else:
            month = "Dec"
        print(month, "|", "*" * int(service_for_graph[x]))
        num += 1
    print("   ", "0", "-" * 20, ">", "X-axis/Income from maintenance jobs (1 * = $10)")



def profit_for_a_month():
    F = open("sold_car_details.txt", "r")
    read = F.readlines()
    selling_price = []

    for line in read:
        selling_price.append(line[:5])

    F = open("sold_car_owner_details.txt", "r")
    read = F.readlines()
    asking_price = []

    for line in read:
        if line[-1] == "\n":
            asking_price.append(line[-6:-1])
        else:
            asking_price.append(line[-5:])


    F = open("service_details.txt", "r")
    read = F.readlines()
    service_dets = []

    for line in read:
        if line[-1] == "\n":
            service_dets.append(line[-3:-1])
        else:
            service_dets.append(line[-2:])


    total_service_income = 0
    for i in range(0, len(service_dets)):
        total_service_income = int(total_service_income) + int(service_dets[i])
    # print(total_service_income)

    total_selling_price = 0
    for i in range(0, len(selling_price)):
        total_selling_price = int(total_selling_price) + int(selling_price[i])
    # print(total_selling_price)

    total_asking_price = 0
    for i in range(0, len(asking_price)):
        total_asking_price = int(total_asking_price) + int(asking_price[i])
    # print(total_asking_price)

    profit = total_selling_price - total_asking_price
    print("\nThe total profit made for this month is ",profit)

    F = open("profit.txt", "a")
    F.writelines("%s\n" % profit)
    F.close()

    income = profit + total_service_income
    print("The total income made for this month is ",income)

    F = open("income.txt", "a")
    F.writelines("%s\n" % income)
    F.close()



def owner_login():
    print("\nGood Day, Sir!")
    owner_password = 4567
    try:
        password_2 = int(input("\nEnter the owner password!"))
    except:
        print("Invalid Password")
    if password_2 == owner_password:  # owner can only view the car details
        remain_in_owner = 1
        while remain_in_owner == 1:
            print("1:Customer Details \n2:Sold Cars Details \n3:Car Service Details \n4:Monthly Report")
            open_file = int(input("Out of the above,input the index of the file you want to view: "))
            if open_file == 1:
                F = open("customer_details.txt", "r")
                print(F.read())
            elif open_file == 2:
                F = open("sold_car_details.txt", "r")
                print(F.read())
            elif open_file == 3:
                F = open("service_details.txt", "r")
                print(F.read())
            else:
                print_report = int(input("\nIs it the end of the month? (1=Yes or 2=No): "))
                if print_report == 1:
                    report()
            remain_in_owner = int(input("Do you still want to continue as the owner (1 = Yes or 2 = No): "))


def technician_login():
    print("\nHave a good day!")
    technician_password = 8910
    try:
        password_3 = int(input("Enter the technician's password!"))
    except:
        print("Invalid Password")
    if password_3 == technician_password:  # technician can enter the car service details
        remain_as_tech = 1
        while remain_as_tech == 1:
            maintenance_job = int(input("Did a vehicle come in for service?(1=yes or 2=no): "))
            if maintenance_job == 1:
                work_done = input("Enter the following vehicle service details in order with a blankspace to separate them; service_date,carID,service_time,service_duration,technician_ID,price: ")
                F = open("service_details.txt", "a")
                F.writelines("%s\n" % work_done)
                F.close()
            remain_as_tech = int(input("Do you wish to continue as the technician? (1 = Yes or 2 = No): "))



print("Hello Stakeholder!")
open_application = int(input("Do you want to log in to the system? (1=Yes or 2=No): "))
while open_application == 1:
    system()
    open_application = int(input("\nDo you want to remain in the system? (1=Yes or 2=No): "))

