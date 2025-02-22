import prompt

import brain_games.cli as cli

GAMES_COUNT = 3


def get_user_answer():
    return int(prompt.string('Your answer: '))


def print_question(question: str):
    print(f'Question: {question}')


def print_lose_message(user_name, user_answer, correct_answer):
    print(f'\'{user_answer}\' is wrong answer ;(.', end=' ')
    print(f'Correct answer was \'{correct_answer}\'.')
    print(f'Let\'s try again, {user_name}!')


def is_user_answer_correct(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer


def run_game(game):
    user_name = cli.welcome_user()
    print(game.RULES)

    for step in range(GAMES_COUNT):
        question, answer = game.get_challenge()
        print_question(question)
        user_answer = get_user_answer()

        if not is_user_answer_correct(user_answer, answer):
            print_lose_message(user_name, user_answer, answer)
            return
        
        print('Correct!')

    print(f'Congratulations, {user_name}!')


