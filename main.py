from ui import UI
from word import Word
from word_list import WordList
import copy
import random

words_list: WordList = WordList([])
unshown_words_list: WordList = WordList([])
score: int = 0
possible_score: int = 0
streak: int = 0


def read_file(file_name: str = "words.txt") -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def parse_file_to_words_list(file_name: str = "words.txt") -> WordList:
    return WordList(WordList.parse_file_to_words(read_file(file_name)))


def start(file_name: str = "words.txt") -> None:
    global words_list; words_list = parse_file_to_words_list(file_name)


def pick_word() -> Word:
    choice: Word = random.choice(unshown_words_list.word_list)
    unshown_words_list.word_list.remove(choice)
    return choice


def play() -> None:
    global unshown_words_list; unshown_words_list = copy.deepcopy(words_list)
    while unshown_words_list.word_list:
        guess()
    print(f"Game over, score: {score}")


def guess() -> None:
    choice: Word = pick_word()
    print(f"{'\n' * 3}")
    print(f"Write strong syllable index (from 1) for this word:")
    print(f"{choice.word_no_highlight}")

    user_guess: int = take_guess(choice)
    global score, possible_score, streak
    possible_score += 1
    if user_guess == choice.syllable_stress_index:
        print(f"Correct!🟢")
        score += 1
        streak += 1
        print(f"Current score: {score}/{possible_score}")
        print(f"Current streak: {streak}")
    else:
        print(f"Wrong!🔴")
        print(f"Correct: {choice.word}, {choice.syllable_stress_index}")
        streak = 0
        print(f"Current score: {score}/{possible_score}")
        print(f"Current streak: {streak}")


def take_guess(correct_word: Word) -> int:
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Your guess was not an integer!")
            continue
        if user_guess <= 0:
            print("Your guess was too low!")
            continue
        if user_guess > correct_word.syllables_count:
            print("Your guess was too high!")
            continue
        return user_guess
    return -1


def main() -> None:
    start()
    print(words_list.word_list)
    #play()


if __name__ == '__main__':
    main()
    UI.run()
