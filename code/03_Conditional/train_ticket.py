# You're building a ticket info system for a reailway app.
# Based on seat type, show its features.

# Task:
#     * Input: "sleeper", "AC", "general", "luxury"
#     * Match using match-case
#     * Unknown -> show: "Invalid seat type"

user_ticket = input("Enter your ticket type (sleeper/AC/general/luxury): ").lower()

def ticket_system(user_ticket):
    match user_ticket:
        case "sleeper":
            print(f"Sleeper Seating")
        case "ac":
            print(f"AC Seating")
        case "general":
            print("General Seating")
        case "luxury":
            print("Luxury Seating")
        case _:
            print(f"Invalid seat type")
        
ticket_system(user_ticket)