from notice2 import Note, NotesList

main_menu = {1: "Показать все",
             2: "Добавить",
             3: "Редактировать",
             4: "Удалить"}

notes = NotesList('notes.json')


def get_note():
    return Note(title=input(f"Введите название заметки\n"), body=input(f"Введите текст заметки\n"))


def add_note():
    notes.add_note(get_note())


def change_note():
    idxs = list(notes.notes.keys())
    if idxs:
        idx = input(f"ВВведите id редактируемой заметки\n Возможные варианты: {idxs}\n")
        while True:
            if idx.isdigit() and int(idx) in idxs:
                new_note = get_note()
                notes.change_note(int(idx), new_note)
                break
            else:
                idx = input(f"Неверный воод!\n Возможные варианты: {idxs}\n")
    else:
        print(f"Список заметок пуст")


def del_note():
    idxs = list(notes.notes.keys())
    if idxs:
        idx = input(f"Введите id удаляемой заметки\n Возможные варианты: {idxs}\n")
        while True:
            if idx.isdigit() and int(idx) in idxs:
                notes.remove_note(int(idx))
                break
            else:
                idx = input(f"Неверный воод!\n Возможные варианты: {idxs}\n")
    else:
        print(f"Список заметок пуст")

def main():
    while True:
        print(f"Всего заметок: {len(notes)}")
        for k, v in main_menu.items():
            print(f"{k}: {v}")
        answer = input(f"Выбери номер пункта меню:\nДля выхода введи любой другой символ\n")
        if not (answer.isdigit() and int(answer) in main_menu):
            break
        # print(f"{Fore.RED}{'@' * 100}{Style.RESET_ALL}")
        if int(answer) == 1:
            notes.show_notes()
        elif int(answer) == 2:
            add_note()
        elif int(answer) == 3:
            change_note()
        elif int(answer) == 4:
            del_note()
        # print(f"{Fore.RED}{'@' * 100}{Style.RESET_ALL}")


if __name__ == '__main__':
    main()