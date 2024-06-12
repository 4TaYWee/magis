//Here's a C++ code for a simple number guessing game:

#include <iostream>
#include <random>

using namespace std;

int main() {
  // Generate a random number between 1 and 100 (inclusive)
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<int> dis(1, 100);
  int secretNumber = dis(gen);

  int guess, numTries = 0;

  cout << "Welcome to the Number Guessing Game!" << endl;
  cout << "I'm thinking of a number between 1 and 100. Try to guess it!" << endl;

  // Loop until the user guesses the number
  do {
    cout << "Enter your guess: ";
    cin >> guess;
    numTries++;

    if (guess > secretNumber) {
      cout << "Your guess is too high. Try again." << endl;
    } else if (guess < secretNumber) {
      cout << "Your guess is too low. Try again." << endl;
    }
  } while (guess != secretNumber);

  cout << "Congratulations! You guessed the number in " << numTries << " tries." << endl;

  return 0;
}

/*
This code explains each step:

Includes necessary libraries: <iostream> for input/output and <random> for generating random numbers.
Uses random_device, mt19937, and uniform_int_distribution to generate a random number between 1 and 100.
Declares variables: secretNumber to store the random number, guess to store the user's guess, and numTries to count the number of attempts.
Welcomes the user and explains the game.
Uses a do-while loop to keep prompting for guesses until the user gets it right.
Inside the loop:
Prompts the user for a guess.
Increments numTries for each attempt.
Checks if the guess is higher or lower than the secret number and provides a clue accordingly.
When the guess is correct, congratulates the user and displays the number of tries taken.
This is a basic example. You can extend it further by:

Changing the guessing range.
Limiting the number of allowed tries.
Keeping track of high scores.
*/
