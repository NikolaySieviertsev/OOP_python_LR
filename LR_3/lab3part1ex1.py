"""
Task 1.
Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types of
 tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer
  than 10 days before the event) and student ticket.
Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the regular ticket price.
All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String.
"""

import json
import datetime

ADVANCE_DAYS_COUNTER = 60
LATE_DAYS_COUNTER = 10
NULL_DAYS_COUNTER = 0
COEFFICIENT_FOR_ADVANCE_TICKET = 0.6
COEFFICIENT_FOR_STUDENT_TICKET = 0.5
COEFFICIENT_FOR_LATE_TICKET = 1.1
LACK_OF_TICKETS = 0


class Ticket:
    id_generator = 0

    def __init__(self):
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        self.price = event['event']['price']
        Ticket.id_generator = event['event']['number_of_tickets']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID have to be integer type!")
        if value > Ticket.id_generator:
            raise ValueError("ID generation failure!")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price have to be numeric type!")
        if value <= 0:
            raise ValueError("Price have to be larger than 0!")
        self.__price = value

    def __str__(self):
        return f'{self.__class__.__name__} {self.price} {self.id}'


class AdvanceTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
            self.price = event['event']['price'] * COEFFICIENT_FOR_ADVANCE_TICKET


class LateTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
            self.price = event['event']['price'] * COEFFICIENT_FOR_LATE_TICKET


class StudentTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
            self.price = event['event']['price'] * COEFFICIENT_FOR_STUDENT_TICKET


class Event:
    def __init__(self):
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        self.date = datetime.datetime(*list(event["event"]["date"]))
        self.regular = Ticket()
        self.student = StudentTicket()
        self.advanced = AdvanceTicket()
        self.late = LateTicket()

    def show_tickets(self):
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < NULL_DAYS_COUNTER:
            return f"Oh no, you`re too late!"
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        if not event['event']['number_of_tickets']:
            return f"Oh no, you`re too late!"
        if date_dif > ADVANCE_DAYS_COUNTER:
            return f"Ticket price: {self.advanced.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        elif NULL_DAYS_COUNTER <= date_dif < LATE_DAYS_COUNTER:
            return f"Ticket price: {self.late.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        else:
            return f"Ticket price: {self.regular.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"

    def buy_ticket(self, is_student):
        date = datetime.datetime.now()
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        if event["event"]["number_of_tickets"] <= LACK_OF_TICKETS:
            raise ValueError("Tickets sold out!")
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < NULL_DAYS_COUNTER:
            raise TimeoutError("Time to buy tickets is up. Event ended.")
        event["event"]["number_of_tickets"] -= 1
        with open("IT-event.json", 'w') as f:
            json.dump(event, f)
        if is_student:
            ticket = self.student
        elif date_dif > ADVANCE_DAYS_COUNTER:
            ticket = self.advanced
        elif NULL_DAYS_COUNTER <= date_dif < LATE_DAYS_COUNTER:
            ticket = self.late
        else:
            ticket = self.regular
        ticket.id = Ticket.id_generator
        Ticket.id_generator -= 1
        with open("data.json", 'r') as f:
            data = json.load(f)
        if 'event' not in data:
            data['event'] = {}
        if not str(ticket.id) in data['event']:
            data['event'][str(ticket.id)] = {}
            data['event'][str(ticket.id)]['price'] = ticket.price
            data['event'][str(ticket.id)]['purchase_date'] = str(date)
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return f"You successfully bought your ticket for {ticket.price}!\n" \
               f"Id:{ticket.id}\n\n"

    @staticmethod
    def search_ticket(ticket_id):
        with open("data.json", 'r') as f:
            data = json.load(f)
        if "event" not in data:
            raise KeyError("There is no events in data")
        if ticket_id not in data["event"]:
            raise KeyError("There is no tickets in data")
        price = data["event"][ticket_id]["price"]
        date = data["event"][ticket_id]["purchase_date"]
        return f"YOUR TICKET:\nTicket id: {ticket_id}\n" \
               f"Price: {price}\nPurchase date: {date}"


response = ""
id = ""
occurrence = Event()
print(occurrence.show_tickets())
print(occurrence.date)
while not response.upper() == "Q":
    response = input("Do you want to search or buy tickets? S/B\nq - to quit\n")
    if response.upper() == "S":
        try:
            id = input("Enter id ")
            print(occurrence.search_ticket(id))
        except KeyError:
            print("Wrong ticket name, restarting...\n")
    elif response.upper() == "B":
        response = input("Are you a student? Y/N\n")
        try:
            if response.upper() == "Y":
                st = True
            elif response.upper() == "N":
                st = False
            else:
                raise TypeError("Incorrect data")
            print(occurrence.buy_ticket(st))
        except TypeError:
            print("Something went wrong, try again")
    else:
        print("Oops, try again")
    print(occurrence.show_tickets())
