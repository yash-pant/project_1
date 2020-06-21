#import requests
#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "FpgFJS5m78WDgqumLl2Q", "isbns": "9781632168146"})
#print(res.json())
print("Welcome to your hotel bookings service!")
print()
("Please sign up to begin your journey to paradise: ")
sorn = input("Please enter a username: ")
sorn2 = input("Please enter a password: ")
print()
print("Now you will be sent back to the sign in page...")

name = input("Please sign in with your username: ")
psrd = input(" Please enter in your password: ")
if name == sorn and psrd == sorn2:
    print("Congratualtions you have signed in")
    print("Welcome to your hotel bookings service!")
    while True:
        x = int(input("How many days will you be staying at your hotel for? "))
        print("You have stated that you will be staying at your hotel for " + str(x) + " days. ")
        print()
        y = int(input("How many people will stay with you? "))
        print("You have stated that " + str(y) + " people will be staying with you.")
        print()
        if y == 1:
            print("Your total will be $250 per night")
        elif y == 2:
            print("Your total wil be $300 per night")
        elif y > 2 and y < 5:
            print("Your total will be $400 per night")
        else:
            print("Your toal will be $500 per night")
        print()
        print("a) New York")
        print("b) London")
        print("c) Amsterdam")
        print("d) Addis Ababa")
        z = input("Which of the above cities would you like to stay in? ")
        if z == "a" or z == "A":
            print()
            print("You have chosen the destination as New York")
        elif z == "b" or z == "B":
            print()
            print("You have chosen the destination as London")
        elif z == "c" or z == "C":
            print()
            print("You have chosen the destination as Amsterdam")
        elif z == "d" or z == "D":
            print()
            print("You have chosen the desitination as Addis Ababa")
        print()
        print("Please continue to the next page for your flight bookings.")
        print("We have found the ideal flight for you. ")
        print()
        print("This is your ideal flight and all of your information in it pre-prepared.")
        print()
        class Flight:   

            counter = 1

            def __init__(self, origin, destination, duration):

                # Keep track of id number.
                self.id = Flight.counter
                Flight.counter += 1

                # Keep track of passengers.
                self.passengers = []

                # Details about flight.
                self.origin = origin
                self.destination = destination
                self.duration = duration

            def print_info(self):
                print(f"Flight origin: {self.origin}")
                print(f"Flight destination: {self.destination}")
                print(f"Flight duration: {self.duration}")

                print()
                print("Passengers:")
                for passenger in self.passengers:
                    print(f"{passenger.name}")

            def delay(self, amount):
                self.duration += amount

            def add_passenger(self, p):
                self.passengers.append(p)
                p.flight_id = self.id


        class Passenger:

            def __init__(self, name):
                self.name = name


        def main():

            # Create flight.
            f1 = Flight(origin="New York", destination="Paris", duration=540)

            # Create passengers.
            alice = Passenger(name="Alice")
            bob = Passenger(name="Bob")

            # Add passengers.
            f1.add_passenger(alice)
            f1.add_passenger(bob)

            f1.print_info()


        if __name__ == "__main__":
            main()
        break
else:
    print("Wrong username and password please try again.")
