from string_manager import StringManager


class Word:
    def __init__(self, word: str):
        self.word: str = word
        self.word_no_highlight: str = Word.remove_stress(word)
        self.syllables_count: int = Word.count_syllables(word)
        self.stress_index: int = Word.calculate_stress_index(word)
        self.syllable_stress_index: int = Word.count_syllable_stress_index(word)


    ## SINGLE WORD!!!
    @staticmethod
    def parse_string_to_word(word_str: str) -> str:
        return word_str.strip().lower()


    @staticmethod
    def remove_stress(text: str) -> str:
        return text.replace("\u0301", "")


    @staticmethod
    def calculate_stress_index(text: str) -> int:
        for index, letter in enumerate(text):
            if letter == StringManager.STRESS_MARK:
                return index - 1
            elif letter == "ё":
                return index
        return -1


    @staticmethod
    def count_syllables(word_str: str) -> int:
        syllables_count = 0
        for letter in word_str:
            if letter in StringManager.VOWELS: syllables_count += 1
        return syllables_count


    @staticmethod
    def count_syllable_stress_index(word_str: str) -> int:
        syllable_index = 0
        for letter in word_str:
            if letter in StringManager.VOWELS: syllable_index += 1
            elif letter == StringManager.STRESS_MARK or letter == "ё": return syllable_index
        return -1


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