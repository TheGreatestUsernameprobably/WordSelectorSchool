from string_manager import StringManager


class Word:
    def __init__(self, word: str):
        self.word: str = word
        self.word_no_highlight: str = Word.word_to_no_highlight(self.word)
        self.syllables_count: int = Word.count_syllables(word)
        self.stress_index: int = StringManager.calculate_stress_index(word)


    @staticmethod
    def count_syllables(word_str: str) -> int:
        syllables_count = 0
        for letter in word_str:
            if letter in StringManager.VOWELS: syllables_count += 1
        return syllables_count

    ## SINGLE WORD!!!
    @staticmethod
    def parse_string_to_word(word_str: str) -> str:
        return word_str.strip().lower()


    @staticmethod
    def word_to_no_highlight(word_str: str) -> str:
        return StringManager.remove_stress(word_str)

    def __str__(self):
        return self.word


    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"word={self.word!r}, "
            f"word_no_highlight={self.word_no_highlight!r}, "
            f"syllables_count={self.syllables_count}, "
            f"stress_index={self.stress_index})"
        )