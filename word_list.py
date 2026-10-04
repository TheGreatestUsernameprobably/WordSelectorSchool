from word import Word
class WordList:
    def __init__(self, word_list: list[Word]):
        self.word_list = word_list

    @staticmethod
    def parse_string_to_word_list(string_content: str) -> list[Word]:
        words: list[Word] = []
        for file_line in string_content.split("\n"):
            for word_str in file_line.split(","):
                word_str: str = Word.parse_string_to_word(word_str)
                word = Word(word_str)
                words.append(word)
        return words


    @staticmethod
    def parse_file_to_words(file_contents: str) -> list[Word]:
        new_words_list: list[Word] = []
        new_words_list.extend(WordList.parse_string_to_word_list(file_contents))
        return new_words_list



    def __str__(self):
        return str(self.word_list)

    def __repr__(self):
        return str(self.word_list)