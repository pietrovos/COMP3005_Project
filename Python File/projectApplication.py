

import psycopg2
from psycopg2 import sql



def connect_to_db():
    conn = psycopg2.connect( dbname="COMP3005_project", user="postgres", password="istanbul1958", host="localhost", port='5432' )
    return conn


def register_user(member_id, first_name, last_name, country, province, city, street_name, street_number, phone_number, email_address, date_of_birth):
    conn = connect_to_db()
    try:
        cursor = conn.cursor()
        insert_query = sql.SQL("INSERT INTO Members (memberID, firstName, lastName, Country, Province, City, streetName, streetNumber, phoneNumber, emailAddress, dateOfBirth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_query, (member_id, first_name, last_name, country, province, city, street_name, street_number, phone_number, email_address, date_of_birth))
        conn.commit()
        print("User " + first_name + " registered successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_member_profile(member_id, first_name, last_name, country, province, city, street_name, street_number, phone_number, email_address, date_of_birth):
    conn = connect_to_db()
    try:
        cursor = conn.cursor()


        query_parts = [
            ("firstName = %s", first_name),
            ("lastName = %s", last_name),
            ("Country = %s", country),
            ("Province = %s", province),
            ("City = %s", city),
            ("streetName = %s", street_name),
            ("streetNumber = %s", street_number),
            ("phoneNumber = %s", phone_number),
            ("emailAddress = %s", email_address),
            ("dateOfBirth = %s", date_of_birth),

        ]

        query = "UPDATE Members SET " + ", ".join([part[0] for part in query_parts if part[1] is not None]) + " WHERE memberID = %s"
        values = tuple([part[1] for part in query_parts if part[1] is not None] + [member_id])

        cursor.execute(query, values)
        conn.commit()
        print("Member's profile has been updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def display_member_dashboard(member_id):
    conn = connect_to_db()
    dashboard_data = {}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PersonalizedDashboards WHERE memberID = %s", (member_id,))
        dashboard_data['exercise_routines'] = cursor.fetchall()

        print("Dashboard Data:", dashboard_data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

    return dashboard_data

def schedule_training_session(session_id, member_id, trainer_id, session_time, duration):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PersonalTrainingSessions (sessionID, memberID, trainerID, sessionTime, duration) VALUES (%s, %s, %s, %s, %s)", (session_id, member_id, trainer_id, session_time, duration))
        conn.commit()
        print("Training session scheduled successfully.")
    except Exception as e:
        print(f"An error occurred while scheduling the session: {e}")
    finally:
        cursor.close()
        conn.close()

def set_trainer_availability(trainer_id, availability):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE Trainers SET availableTimeSlots = %s WHERE trainerID = %s", (availability, trainer_id))
        conn.commit()
        print("Trainer availability updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()



def view_member_profile(first_name, last_name):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Members WHERE firstName = %s AND lastName = %s", (first_name, last_name))
        member_profile = cursor.fetchall()

        for profile in member_profile:
            print(profile)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

    return member_profile


def add_room_booking(booking_id, room_id, booking_time, duration, staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO RoomBookings (bookingID, roomID, bookingTime, duration, staffID) VALUES (%s, %s, %s, %s, %s)", (booking_id, room_id, booking_time, duration, staffID))
        conn.commit()
        print("Room booking added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def update_room_booking(booking_id, new_room_id, new_booking_time, new_duration, new_staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE RoomBookings SET "
        query_params = []

        if new_room_id is not None:
            query += "roomID = %s,"
            query_params.append(new_room_id)

        if new_booking_time is not None:
            query += "bookingTime = %s,"
            query_params.append(new_booking_time)

        if new_duration is not None:
            query += "duration = %s,"
            query_params.append(new_duration)

        if new_staffID is not None:
            query += "staffID = %s,"
            query_params.append(new_staffID)

        query = query.rstrip(',')
        query += " WHERE bookingID = %s"
        query_params.append(booking_id)

        cursor.execute(query, query_params)
        conn.commit()
        print("Room booking updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def view_room_bookings():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM RoomBookings")
        bookings = cursor.fetchall()
        for booking in bookings:
            print(booking)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

    return bookings

def add_maintenance_record(maintenance_id, equipment_id, maintenance_date, details, staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO EquipmentMaintenance (maintenanceID, equipmentID, maintenanceDate, details, staffID) VALUES (%s, %s, %s, %s, %s)", (maintenance_id, equipment_id, maintenance_date, details, staffID))
        conn.commit()
        print("Maintenance record added.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def update_maintenance_record(maintenance_id, new_equipment_id, new_maintenance_date, new_details, new_staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = "UPDATE EquipmentMaintenance SET "
        query_params = []

        if new_equipment_id is not None:
            query += "equipmentID = %s,"
            query_params.append(new_equipment_id)

        if new_maintenance_date is not None:
            query += "maintenanceDate = %s,"
            query_params.append(new_maintenance_date)

        if new_details is not None:
            query += "details = %s,"
            query_params.append(new_details)

        if new_staffID is not None:
            query += "staffID = %s,"
            query_params.append(new_staffID)

        query = query.rstrip(',')
        query += " WHERE maintenanceID = %s"
        query_params.append(maintenance_id)

        cursor.execute(query, query_params)
        conn.commit()
        print("Maintenance record updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def add_class_schedule(class_id, class_name, trainer_id, class_time, duration, staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Classes (classID, className, trainerID, classTime, duration, staffID) VALUES (%s, %s, %s, %s, %s, %s)", (class_id, class_name, trainer_id, class_time, duration, staffID))
        conn.commit()
        print("Class schedule added.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def update_class_schedule(class_id, new_class_name, new_trainer_id, new_class_time, new_duration, new_staffID):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = "UPDATE Classes SET "
        query_params = []

        if new_class_name is not None:
            query += "className = %s,"
            query_params.append(new_class_name)

        if new_trainer_id is not None:
            query += "trainerID = %s,"
            query_params.append(new_trainer_id)

        if new_class_time is not None:
            query += "classTime = %s,"
            query_params.append(new_class_time)

        if new_duration is not None:
            query += "duration = %s,"
            query_params.append(new_duration)

        if new_staffID is not None:
            query += "staffID = %s,"
            query_params.append(new_staffID)

        query = query.rstrip(',')
        query += " WHERE classID = %s"
        query_params.append(class_id)

        cursor.execute(query, query_params)
        conn.commit()
        print("Class schedule updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def add_billing_record(bill_id, member_id, amount, bill_date):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Billing (billID, memberID, amount, billDate,  isPaid) VALUES (%s, %s, %s, %s, CAST(%s AS BIT))", (bill_id, member_id, amount, bill_date, 0))
        conn.commit()
        print("Billing record added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def process_payment(bill_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE Billing SET isPaid = CAST(%s AS BIT) WHERE billID = %s", (1, bill_id))
        conn.commit()
        print(f"Payment processed for bill ID {bill_id}.")
    except Exception as e:
        print(f"An error occurred during payment processing: {e}")
    finally:
        cursor.close()
        conn.close()

def view_bill_records():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Billing")
        bills = cursor.fetchall()
        for bill in bills:
            print(bill)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

    return bills


def main_menu():
    while True:
        print("\nHealth and Fitness Club Management System")
        print("Select an Option:")
        print("1. I am a Memeber")
        print("2. I am a Trainer")
        print("3. I am Administrative Staff")
        print("4. Exit")




        choice = input("Enter your choice: ")

        if choice == '1':
            print("1. Register User")
            print("2. Update Member Profile")
            print("3. Display Member Dashboard")
            print("4. Schedule Training Session")
            choice = input("Enter your choice: ")

            if choice == '1':
                member_id = int(input("Enter Member ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                country = input("Enter Country: ")
                province = input("Enter Province: ")
                city = input("Enter City: ")
                street_name = input("Enter Street Name: ")
                street_number = int(input("Enter Street Number: "))
                phone_number = input("Enter Phone Number: ")
                email_address = input("Enter Email Address: ")
                date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
                register_user(member_id, first_name, last_name, country, province, city, street_name, street_number,
                          phone_number, email_address, date_of_birth)

            elif choice == '2':
                member_id = int(input("Enter Member ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                country = input("Enter Country: ")
                province = input("Enter Province: ")
                city = input("Enter City: ")
                street_name = input("Enter Street Name: ")
                street_number = int(input("Enter Street Number: "))
                phone_number = input("Enter Phone Number: ")
                email_address = input("Enter Email Address: ")
                date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
                update_member_profile(member_id, first_name, last_name, country, province, city, street_name, street_number, phone_number, email_address, date_of_birth)

            elif choice == '3':
                member_id = int(input("Enter member ID: "))
                display_member_dashboard(member_id)
            elif choice == '4':
                session_id = int(input("Enter session ID: "))
                member_id = int(input("Enter Member ID: "))
                trainer_id = int(input("Enter Trainer ID: "))
                session_time = input("Enter Session Time (YYYY-MM-DD HH:MM): ")
                duration = int(input("Enter Duration (in minutes): "))

                schedule_training_session(session_id, member_id, trainer_id, session_time, duration)

        elif choice == '2':
            print("1. Set Trainer Availability")
            print("2. View Member Profile")


            choice = input("Enter your choice: ")

            if choice == '1':
                trainer_id = int(input("Enter trainer ID: "))
                availability = input("Enter availability: ")
                set_trainer_availability(trainer_id, availability)

            elif choice == '2':
                first_name = input("Enter member's first name: ")
                last_name = input("Enter member's last name: ")
                view_member_profile(first_name, last_name)

        elif choice == '3':

            print("1. Room Booking Management")
            print("2. Equipment Maintenance Management")
            print("3. Class Schedule Management")
            print("4. Billing and Payment Processing")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nRoom Booking Management System")
                print("1. Add Room Booking")
                print("2. Update Room Booking")
                print("3. View Room Booking Information")

                choice = input("Enter your choice: ")

                if choice == '1':
                    booking_id = int(input("Enter Booking ID: "))
                    room_id = int(input("Enter Room ID: "))
                    booking_time = input("Enter Booking Time (YYYY-MM-DD HH:MM): ")
                    duration = int(input("Enter Duration (in minutes): "))
                    staff_id = int(input("Enter Staff ID: "))

                    add_room_booking(booking_id, room_id, booking_time, duration, staff_id)

                elif choice == '2':
                    booking_id = int(input("Enter Booking ID: "))
                    new_room_id = int(input("Enter Room ID: "))
                    new_booking_time = input("Enter Booking Time (YYYY-MM-DD HH:MM): ")
                    new_duration = int(input("Enter Duration (in minutes): "))
                    new_staff_id = int(input("Enter Staff ID:"))
                    update_room_booking(booking_id, new_room_id, new_booking_time, new_duration, new_staff_id)

                elif choice == '3':
                    view_room_bookings()

            elif choice == '2':
                print("\nRoom Booking Management System")
                print("1. Add Maintenance Record")
                print("2. Update Maintenance Record")

                choice = input("Enter your choice: ")

                if choice == '1':
                    maintenance_id = int(input("Enter Maintenance ID: "))
                    equipment_id = int(input("Enter Equipment ID: "))
                    maintenance_date = input("Enter Maintenance Date (YYYY-MM-DD): ")
                    details = input("Enter Details: ")
                    staff_id = int(input("Enter Staff ID: "))

                    add_maintenance_record(maintenance_id, equipment_id, maintenance_date, details, staff_id)

                if choice == '2':
                    maintenance_id = int(input("Enter Maintenance ID: "))
                    new_equipment_id = int(input("Enter Equipment ID: "))
                    new_maintenance_date = input("Enter Maintenance Date (YYYY-MM-DD): ")
                    new_details = input("Enter Details: ")
                    new_staff_id = int(input("Enter Staff ID:"))

                    update_maintenance_record(maintenance_id, new_equipment_id, new_maintenance_date, new_details, new_staff_id)


            elif choice == '3':
                print("\nClass Schedule Management System")
                print("1. Add Class")
                print("2. Update Class Scheduling")

                choice = input("Enter your choice: ")

                if choice == '1':
                    class_id = int(input("Enter Class ID: "))
                    class_name = input("Enter Class Name: ")
                    trainer_id = int(input("Enter Trainer ID: "))
                    class_time = input("Enter Class Time (YYYY-MM-DD HH:MM): ")
                    duration = int(input("Enter Duration (in minutes): "))
                    staff_id = int(input("Enter Staff ID: "))

                    add_class_schedule(class_id, class_name, trainer_id, class_time, duration, staff_id)



                if choice == '2':
                    class_id = int(input("Enter Class ID: "))
                    new_class_name = input("Enter Class Name: ")
                    new_trainer_id = int(input("Enter Trainer ID: "))
                    new_class_time = input("Enter Class Time (YYYY-MM-DD HH:MM): ")
                    new_duration = int(input("Enter Duration (in minutes): "))
                    new_staff_id = int(input("Enter Staff ID: "))

                    update_class_schedule(class_id, new_class_name, new_trainer_id, new_class_time, new_duration, new_staff_id)

            elif choice == '4':
                print("\nClass Schedule Management System")
                print("1. Add Billing Record")
                print("2. Process Payment for a Billing Record")
                print("3. View All Billing Records")

                choice = input("Enter your choice: ")

                if choice == '1':
                    bill_id = int(input("Enter Bill ID: "))
                    member_id = int(input("Enter Member ID: "))
                    amount = float(input("Enter Amount: "))
                    bill_date = input("Enter Bill Date (YYYY-MM-DD): ")
                    add_billing_record(bill_id, member_id, amount, bill_date)

                elif choice == '2':
                    choice = input("Enter which billID you would like to process: ")
                    process_payment(choice)

                elif choice == '3':
                    view_bill_records()




        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
