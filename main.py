#from word import Word
from word_list import WordList
import flet as ft
words_list: WordList | None = None


def read_file(file_name: str = "words.txt") -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def parse_file_content_to_words_list(file_content: str) -> WordList:
    return WordList(WordList.parse_file_to_words(file_content))


def ui(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Создаем поле для отображения числа
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Функция для кнопки "минус"
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

      # Функция для кнопки "плюс"
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # Добавляем элементы на страницу в строку
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def main():
    global words_list; words_list = parse_file_content_to_words_list(read_file())
    print(words_list.word_list)

ft.app(ui)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
