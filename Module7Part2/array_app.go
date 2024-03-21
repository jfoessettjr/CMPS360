package main

import "fmt"

func main() {
	const conferenceTickets int = 50
	var remainingTickets uint = 50
	conferenceName := "Bison Up Conference"
	bookings := []string{}

	fmt.Printf("Welcome to %s booking application. \nWe have a total of %d are still available. \nGet your tickets here to attend\n", conferenceName, remainingTickets)

	// Declare Data Types
	var firstName string
	var lastName string
	var email string
	var userTickets uint

	// Collect the Data
	fmt.Println("Enter your First Name: ")
	fmt.Scanln(&firstName)

	fmt.Println("Enter your Last Name: ")
	fmt.Scanln(&lastName)

	fmt.Println("Enter your Email: ")
	fmt.Scanln(&email)

	fmt.Println("Enter number of Tickets: ")
	fmt.Scanln(&userTickets)

	// Logic for booking system
	remainingTickets = remainingTickets - userTickets
	bookings = append(bookings, firstName + " " + lastName)

	// Output
	fmt.Printf("Thanks %s %s for booking %d tickets. You will recieve a confirmation email at %s\n", firstName,
lastName, userTickets, email)

	fmt.Printf("%d tickets remaining for %s\n", remainingTickets, conferenceName)
	fmt.Printf("These are all of our bookings: %s %s with %d tickets\n", firstName, lastName, userTickets)
}
