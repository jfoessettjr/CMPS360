package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    // Create a new scanner to read input from the user
    scanner := bufio.NewScanner(os.Stdin)

    // Prompt the user to enter their name
    fmt.Println("Who is your favorite Pittsburgh Steeler?")
    scanner.Scan()
    name := scanner.Text()

    // Prompt the user to enter their age
    fmt.Println("Who is your favorite Pittsburgh Penguin?")
    scanner.Scan()
    age := scanner.Text()

    // Prompt the user to enter their favorite color
    fmt.Println("What other major sport did you wish had a team in Pittsburgh?")
    scanner.Scan()
    color := scanner.Text()

    // Print out a personalized message with the user's information
    fmt.Printf("\nI like %s as well Go Steelers!\n", name)
    fmt.Printf("%s is awesome! Lets Go Pens! \n%s is a cool sport.", age, color)
}
