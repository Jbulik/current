import json
import os
from datetime import datetime

# Путь к файлу с данными заметок
DATA_FILE = "notes.json"


def load_notes():
    """Функция загрузки данных заметок из файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []



# Функция принимает список заметок как аргумент и записывает его в файл в формате JSON
def save_notes(notes):
    """Функция для загрузки данных заметок в файл"""
    with open(DATA_FILE, "w") as file:
        json.dump(notes, file, indent=4)


# обновляет id, добавляет текущую дату/время и затем сохраняет обновленный список заметок в файл
def add_note(title, body):
    """Функция для обавления новой заметку в список заметок"""
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена")


# выводит информацию о каждой заметке по указанной Дате
def list_notes(filter_date=None):
    """Функция для поиска заметок"""
    notes = load_notes()
    if filter_date:
        filtered_notes = [note for note in notes if filter_date in note["timestamp"]]
        notes = filtered_notes
    if notes:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/время: {note['timestamp']}")
            print(f"Тело заметки:\n{note['body']}\n")
    else:
        print("Заметок не найдено")


print("Заметка с данным ID не найдена")

def edit_note(note_id, new_title, new_body):
    """Функция для редактирования заметок"""
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с данным ID не найдена")


def delete_note(note_id):
    """Функция для удаления заметок"""
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")


def main():
    """Функция с меню для выбора действия в консоли"""
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input()

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add_note(title, body)
        elif choice == "2":
            filter_date = input("Введите дату для фильтрации (YYYY-MM-DD): ")
            list_notes(filter_date)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое тело заметки: ")
            edit_note(note_id, new_title, new_body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()



