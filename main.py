#from word import Word
from word_list import WordList

words_list: WordList | None = None


def read_file(file_name: str = "words.txt") -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def parse_file_content_to_words_list(file_content: str) -> WordList:
    return WordList(WordList.parse_file_to_words(file_content))


def main():
    global words_list; words_list = parse_file_content_to_words_list(read_file())
    print(words_list.word_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
