class StringManager:
    LETTERS: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    VOWELS: str = "уеёыаоэяию"
    STRESS_MARK: str = "\u0301"

    @staticmethod
    def remove_stress(text: str) -> str:
        return text.replace("\u0301", "")

    @staticmethod
    def calculate_stress_index(text: str) -> int:
        for index, letter in enumerate(text):
            if letter == StringManager.STRESS_MARK: return index-1
            elif letter == "ё": return index
        return -1