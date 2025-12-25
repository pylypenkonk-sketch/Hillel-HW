import codecs
import re
import os


def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Отримуємо шлях до папки, де лежить скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, html_file)

    # Перевірка наявності файлу
    if not os.path.exists(full_path):
        print(f"Помилка: Файл {html_file} не знайдено в папці {current_dir}")
        return

    # Читання файлу
    with codecs.open(full_path, 'r', 'utf-8') as file:
        html_content = file.read()

    # Видалення HTML-тегів [cite: 1, 3]
    # Вираз <[^>]*> видаляє все між символами < та >
    cleaned_text = re.sub(r'<[^>]*>', '', html_content)

    # Видалення порожніх рядків (додаткове завдання)
    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    # Запис результату
    result_path = os.path.join(current_dir, result_file)
    with codecs.open(result_path, 'w', 'utf-8') as file:
        file.write('\n'.join(non_empty_lines))

    print(f"Файл успішно очищено. Результат у: {result_file}")


# Виклик функції (переконайтеся, що тут немає зайвих символів)
delete_html_tags('draft.html', 'cleaned.txt')