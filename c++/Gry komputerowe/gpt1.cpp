/*
Number Guessing Game
User
In c++ create a simple console game that involves the user guessing a number. The computer generates a random number and the user tries to guess it in as few attempts as possible. The program should provide clues as to whether the given number is greater or less than the number drawn.
ChatGPT
Sure, here's a simple console game in C++ where the user guesses a randomly generated number:

```cpp
*/
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(time(0)); // Seed the random number generator

    int secretNumber = rand() % 100 + 1; // Generate a random number between 1 and 100
    int guess;
    int attempts = 0;

    std::cout << "Welcome to the Number Guessing Game!\n";
    std::cout << "I have chosen a number between 1 and 100. Try to guess it!\n";

    do {
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;

        if (guess < secretNumber) {
            std::cout << "Too low! Try again.\n";
        } else if (guess > secretNumber) {
            std::cout << "Too high! Try again.\n";
        } else {
            std::cout << "Congratulations! You guessed the number in " << attempts << " attempts!\n";
        }
    } while (guess != secretNumber);

    return 0;
}
/*
```

In this game:

1. The program generates a random number between 1 and 100.
2. The user repeatedly guesses the number.
3. After each guess, the program provides feedback if the guessed number is too high or too low.
4. The game continues until the user guesses the correct number.

Compile and run this code, and you'll have your simple number guessing game in C++!
*/
