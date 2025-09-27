# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------
import random

# ---------------- CLASS DEFINITIONS ---------------- #

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats
        self.available_seats = [(i, self.assign_berth(i)) for i in range(1, seats + 1)]  # (seat_no, berth)

    def assign_berth(self, seat_no):
        """Assign berth type based on seat number"""
        berth_types = ["Lower Berth", "Middle Berth", "Upper Berth"]
        return berth_types[(seat_no - 1) % 3]  # Cycle through L, M, U

    def display_info(self):
        print(f"Train Number   : {self.train_num}")
        print(f"Source         : {self.source}")
        print(f"Destination    : {self.destination}")
        print(f"Available Seats: {len(self.available_seats)}")
        print("-" * 40)

    def book_tickets(self, num_tickets):
        if num_tickets > len(self.available_seats):
            return None

        # Assign seats & generate PNR
        assigned = self.available_seats[:num_tickets]
        self.available_seats = self.available_seats[num_tickets:]  # update availability
        pnr_list = [random.randint(100000, 999999) for _ in range(num_tickets)]

        # return list of (PNR, seat_no, berth)
        return [(pnr_list[i], assigned[i][0], assigned[i][1]) for i in range(num_tickets)]


class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Passenger Name : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Gender         : {self.gender}")
        print(f"Phone Number   : {self.phone}")


class Ticket:
    def __init__(self, train, passenger, pnr, seat_no, berth):
        self.train = train
        self.passenger = passenger
        self.pnr = pnr
        self.seat_no = seat_no
        self.berth = berth

    def display_info(self):
        print(f"\n--- Ticket Details ---")
        print(f"Train Number   : {self.train.train_num}")
        print(f"Source         : {self.train.source}")
        print(f"Destination    : {self.train.destination}")
        print(f"PNR Number     : {self.pnr}")
        print(f"Seat Number    : {self.seat_no}")
        print(f"Berth Type     : {self.berth}")
        self.passenger.display_info()
        print("-" * 40)


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# ---------------- MAIN PROGRAM ---------------- #

class RailwaySystem:
    def __init__(self):
        self.accounts = [Account("user1", "password1"), Account("user2", "password2")]
        self.trains = [
            Train("12764", "Secunderabad", "Tirupati", 40),
            Train("12728", "Secunderabad", "Visakhapatnam", 50),
            Train("12744", "Vijayawada", "Gudur", 15),
            Train("12760", "Secunderabad", "Nellore", 8),
            Train("12709", "Nellore", "Secunderabad", 10),
        ]
        self.logged_in_account = None

    def create_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.accounts.append(Account(username, password))
        print("✅ Account created successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in self.accounts:
            if account.username == username and account.check_password(password):
                self.logged_in_account = account
                print(f"\n✅ Login successful. Welcome, {username}!\n")
                return True
        print("❌ Invalid username or password.")
        return False

    def show_trains(self):
        print("\nAvailable Trains:")
        print("-" * 40)
        for train in self.trains:
            train.display_info()

    def book_ticket(self):
        self.show_trains()
        train_num = input("\nEnter Train Number: ")
        num_tickets = int(input("Enter Number of Tickets: "))

        train = next((t for t in self.trains if t.train_num == train_num), None)

        if not train:
            print("❌ Invalid Train Number.")
            return

        booking_info = train.book_tickets(num_tickets)
        if booking_info is None:
            print("❌ Not enough seats available.")
            return

        passengers = []
        for i in range(num_tickets):
            print(f"\nEnter details for Passenger {i+1}:")
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            phone = input("Phone Number: ")
            passengers.append(Passenger(name, age, gender, phone))

        print("\n--- ✅ Booking Successful! ---")
        for i in range(num_tickets):
            pnr, seat_no, berth = booking_info[i]
            ticket = Ticket(train, passengers[i], pnr, seat_no, berth)
            ticket.display_info()

    def run(self):
        while True:
            print("\n===== RAILWAY SYSTEM =====")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                if self.login():
                    while True:
                        print("\n===== MENU =====")
                        print("1. Show Trains")
                        print("2. Book Ticket")
                        print("3. Logout")
                        choice = input("Enter choice: ")

                        if choice == "1":
                            self.show_trains()
                        elif choice == "2":
                            self.book_ticket()
                        elif choice == "3":
                            print("👋 Logged out successfully!")
                            break
                        else:
                            print("⚠ Invalid choice.")
            elif choice == "3":
                print("🙏 Thank you! Visit Again.")
                break
            else:
                print("⚠ Invalid choice.")


# ---------------- RUN PROGRAM ---------------- #
if __name__ == "__main__":
    RailwaySystem().run()

