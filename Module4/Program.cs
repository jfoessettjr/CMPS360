using System.Diagnostics;
using System.Numerics;

namespace Module4;

class Program
{
    static void Main(string[] args)
    {
       /* int number = 23;

       // if(number == 23){
           Console.WriteLine("The number of Jordan 23"); 
       // } else {
            Console.WriteLine("The number is incorrect");
        } */

       Console.WriteLine("Welcome to the House of Pain");

       Random random = new Random();
       int targetNumber = random.Next(1,10);

        int attempts = 0;
        bool hasGuessedCorrectly = false;

        Console.WriteLine("Try to guess the number between 1 and 10");

        while(!hasGuessedCorrectly){
            Console.Write("Input your guess: ");
            string userInput = Console.ReadLine();

            if(int.TryParse(userInput, out int UserGuess))
            {
               attempts++;
               if(UserGuess == targetNumber){
                    hasGuessedCorrectly = true;
                    Console.WriteLine("Congrats you guessed it");
               } else {
                    string hint = (UserGuess < targetNumber) ? "Too low, try again!" : "Too high, try again";
                    Console.WriteLine(hint);
               }
            }
            else
            {
                Console.WriteLine("Invalid Input, Please enter a valid number");
            }
        }
            Console.WriteLine("Thank you for playing House of Pain");
    }

}
