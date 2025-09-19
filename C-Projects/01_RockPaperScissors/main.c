#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int game(char you, char computer) {
    if (you == computer) return -1; // Draw
    if ((you == 's' && computer == 'z') ||
        (you == 'p' && computer == 's') ||
        (you == 'z' && computer == 'p'))
        return 1; // You win
    return 0; // Computer wins
}

int main() {
    char you, computer, playAgain;
    int n;
    int userScore = 0, compScore = 0, round = 0;

    srand(time(NULL));

    do {
        round++;
        // Computer randomly chooses
        n = rand() % 100;
        if (n < 33)
            computer = 's';
        else if (n < 66)
            computer = 'p';
        else
            computer = 'z';

        // Get valid user input
        do {
            printf("\nRound %d\n", round);
            printf("Enter s for STONE, p for PAPER, z for SCISSOR: ");
            scanf(" %c", &you);

            if (you != 's' && you != 'p' && you != 'z') {
                printf("Invalid input! Please enter only 's', 'p', or 'z'.\n");
            }
        } while (you != 's' && you != 'p' && you != 'z');

        int result = game(you, computer);

        if (result == -1) {
            printf("\nGame Draw!\n");
        } else if (result == 1) {
            printf("\nWow! You have won this round!\n");
            userScore++;
        } else {
            printf("\nOh! You have lost this round!\n");
            compScore++;
        }

        printf("You chose: %c | Computer chose: %c\n", you, computer);
        printf("Score -> You: %d | Computer: %d\n", userScore, compScore);

        // Horizontal line after each round
        printf("----------------------------------------\n");

        // Ask user if they want to play again
        do {
            printf("Do you want to play again? (y/n): ");
            scanf(" %c", &playAgain);
            if (playAgain != 'y' && playAgain != 'Y' && playAgain != 'n' && playAgain != 'N') {
                printf("Invalid input! Please enter 'y' or 'n'.\n");
            }
        } while (playAgain != 'y' && playAgain != 'Y' && playAgain != 'n' && playAgain != 'N');

    } while (playAgain == 'y' || playAgain == 'Y');

    printf("\nFinal Score -> You: %d | Computer: %d\n", userScore, compScore);

    if (userScore > compScore)
        printf("Congratulations! You won the game!\n");
    else if (userScore < compScore)
        printf("Oh! You lost the game. Better luck next time!\n");
    else
        printf("The game ended in a draw!\n");

    printf("Thanks for playing! Goodbye.\n");

    return 0;
}
