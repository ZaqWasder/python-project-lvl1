from random import randint

import prompt

from brain_games.cli import welcome_user


def print_rules():
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    print(rules)


def start_stage_of_game(user_name: str) -> bool:
    is_winning = False
    random_number = randint(0, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"

    print(f"Question: {random_number}")
    answer = prompt.string("Your answer: ")

    if answer == correct_answer:
        print("Correct!")
        is_winning = True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")

    return is_winning


def start_game(user_name: str, answers_for_win: int):
    wins_counter = 0

    while wins_counter < answers_for_win:
        is_winning = start_stage_of_game(user_name)
        
        if not is_winning:
            break

        wins_counter += 1

    if wins_counter == answers_for_win:
        print(f"Congratulations, {user_name}!")


def main():
    user_name = welcome_user()
    print_rules()
    start_game(user_name, 3)


if __name__ == "__main__":
    main()
