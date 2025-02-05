from random import randint, choice

import brain_games.cli as cli
import brain_games.utils as utils


operators = ["+", "-", "*"]

def run_stage_of_game(user_name: str) -> bool:
    is_winning = False
    operand_one = randint(0, 100)
    operand_two = randint(0, 100)
    operator = choice(operators)

    match operator:
        case "+":
            correct_answer = str(operand_one + operand_two)
        case "-":
            correct_answer = str(operand_one - operand_two)
        case "*":
            correct_answer = str(operand_one * operand_two)

    print(f"Question: {operand_one} {operator} {operand_two}")
    answer = utils.get_user_answer()

    if answer == correct_answer:
        print("Correct!")
        is_winning = True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")

    return is_winning


def run_game(user_name: str, answers_for_win: int):
    wins_counter = 0

    print("What is the result of the expression?")

    while wins_counter < answers_for_win:
        is_winning = run_stage_of_game(user_name)
        
        if not is_winning:
            break

        wins_counter += 1

    if wins_counter == answers_for_win:
        print(f"Congratulations, {user_name}!")


def main():
    user_name = cli.welcome_user()
    run_game(user_name, utils.GAMES_COUNT)


if __name__ == "__main__":
    main()
