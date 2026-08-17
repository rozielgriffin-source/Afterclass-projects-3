
passenger_name = "Roziel"
destination = "Atlanta"
ticket_price = 1250.99
ticket_counter = 4
is_available = False
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", ticket_counter)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(ticket_counter))
print(type(is_available))

total_cost = ticket_price * ticket_counter
discount = 150.00
final_cost = total_cost - discount
 
print("\nTotal Cost: $", total_cost)
print("Discount: $", discount)
print("Final Cost: $", final_cost)
 
print("Triple Ticket Price: $", ticket_price * 3)
print("Ticket Price After $125 Increase: $", ticket_price + 125)
print("Half Ticket Price: $", ticket_price / 2)

print("\nIs ticket price under $1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", ticket_counter > 2)
print("Is destination Atlanta?", destination == "Atlanta")
print("Is final cost more than $2000?", final_cost > 6000)

travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("Third letter of destination:", destination[2])
print("Length of passenger name:", len(passenger_name))
 
before_ticket_price = 1400.00
after_ticket_price = 1100.00
 
print("\nBefore Swapping:")
print("Morning Ticket Price: $", before_ticket_price)
print("Evening Ticket Price: $", after_ticket_price)

before_ticket_price, after_ticket_price = after_ticket_price, before_ticket_price

print("\nAfter Swapping:")
print("Morning Ticket Price: $", before_ticket_price)
print("Evening Ticket Price: $", after_ticket_price)
 
print("\n--------------------------------")
print("TRAVEL TICKET SUMMARY")
print("\n--------------------------------")

print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked: ", ticket_counter)
print("Final Amount to Pay: $", final_cost)
print("Booking Confirmed?", is_available)
