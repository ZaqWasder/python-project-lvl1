from random import randint

import brain_games.cli as cli
import brain_games.utils as utils


def print_rules():
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    print(rules)


def run_stage_of_game(user_name: str) -> bool:
    is_winning = False
    random_number = randint(0, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"

    print(f"Question: {random_number}")
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

    while wins_counter < answers_for_win:
        is_winning = run_stage_of_game(user_name)
        
        if not is_winning:
            break

        wins_counter += 1

    if wins_counter == answers_for_win:
        print(f"Congratulations, {user_name}!")


def main():
    user_name = cli.welcome_user()
    print_rules()
    run_game(user_name, utils.GAMES_COUNT)


if __name__ == "__main__":
    main()
