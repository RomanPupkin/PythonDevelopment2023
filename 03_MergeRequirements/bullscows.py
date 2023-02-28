import argparse
import urllib.request
import random
import argparse

def bullscows(guess: str, secret: str) -> (int, int):
    return sum(i == j for i, j in zip(guess, secret)), len(set(guess).intersection(secret))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = random.choice(words)
    iterations = 0
    guess = ""
    while guess != word:
        iterations += 1
        guess = ask("Введите слово: ", words)
        b, c = bullscows(guess, word)
        inform("Быки: {}, Коровы: {}", b, c)
    
    print(f"Попыток: {iterations}")
    return iterations


def ask(prompt: str, valid: list[str] = None) -> str:
    guess = input(prompt)

    if valid is not None:
        while not guess in valid:
            print("Допустимы слова только из словаря!")
            guess = input(prompt)
    return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="dict", default='', help="path or url of dictionary")
    parser.add_argument(dest="length", default=5, help="length of word", type=int)
    args = parser.parse_args()
    
    words_list = []
    if args.dict.startswith("http"):
        full_dict = ""
        with urllib.request.urlopen(args.dict) as fin:
            full_dict = fin.read().decode("utf-8")
        words_list = [word.strip() for word in full_dict.split() if len(word.strip()) == args.length]
    else:
        with open(args.dict) as fin:
            words_list = [line.strip() for line in fin if len(line.strip()) == args.length]
    
    gameplay(ask, inform, words_list)
