using System;

namespace ThreeLetterWordGame
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = { "cat", "dog", "hat", "pen", "cup", "car", "box", "map" };
            Random random = new Random();
            string wordToGuess = words[random.Next(0, words.Length)];

            Console.WriteLine("Welcome to the Three Letter Word Game!");
            Console.WriteLine("Try to guess the 3-letter word.");
            Console.WriteLine("These are the words you can guess from: cat, dog, hat, pen, cup, car, box.");

            bool wordGuessed = false;
            int attempts = 0;

            while (!wordGuessed)
            {
                Console.Write("Enter your guess: ");
                string guess = Console.ReadLine().ToLower();

                if (guess.Length != 3)
                {
                    Console.WriteLine("Please enter a 3-letter word.");
                    continue;
                }

                attempts++;

                if (guess == wordToGuess)
                {
                    Console.WriteLine($"Congratulations! You guessed the word '{wordToGuess}' in {attempts} attempts.");
                    wordGuessed = true;
                }
                else
                {
                    Console.WriteLine("Incorrect guess. Try again.");

                    // Provide some hints
                    for (int i = 0; i < 3; i++)
                    {
                        if (guess[i] == wordToGuess[i])
                        {
                            Console.WriteLine($"Letter '{guess[i]}' is in the correct position.");
                        }
                        else if (wordToGuess.Contains(guess[i]))
                        {
                            Console.WriteLine($"Letter '{guess[i]}' is in the word but in the wrong position.");
                        }
                        else
                        {
                            Console.WriteLine($"Letter '{guess[i]}' is not in the word.");
                        }
                    }
                }
            }
        }
    }
}
