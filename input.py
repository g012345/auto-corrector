import tkinter as tk

keyboard_mapping_rus = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[',
    'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';',
    'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`',
    'Q': 'й', 'W': 'ц', 'E': 'у', 'R': 'к', 'T': 'е', 'Y': 'н', 'U': 'г', 'I': 'ш', 'O': 'щ', 'P': 'з', '[': 'х',
    ']': 'ъ', 'A': 'ф', 'S': 'ы', 'D': 'в', 'F': 'а', 'G': 'п', 'H': 'р', 'J': 'о', 'K': 'л', 'L': 'д', ';': 'ж',
    "'": 'э', 'Z': 'я', 'X': 'ч', 'C': 'с', 'V': 'м', 'B': 'и', 'N': 'т', 'M': 'ь', ',': 'б', '.': 'ю', '`': 'ё'
}

keyboard_mapping_eng = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',
    ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
    "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '`': 'ё',
    'Q': 'й', 'W': 'ц', 'E': 'у', 'R': 'к', 'T': 'е', 'Y': 'н', 'U': 'г', 'I': 'ш', 'O': 'щ', 'P': 'з', '{': 'х',
    '}': 'ъ', 'A': 'ф', 'S': 'ы', 'D': 'в', 'F': 'а', 'G': 'п', 'H': 'р', 'J': 'о', 'K': 'л', 'L': 'д', ':': 'ж',
    '"': 'э', 'Z': 'я', 'X': 'ч', 'C': 'с', 'V': 'м', 'B': 'и', 'N': 'т', 'M': 'ь', '<': 'б', '>': 'ю', '~': 'ё'
}

def transform_text(text, mapping):
    transformed_text = ''
    inside_quotes = False
    for char in text:
        if char == "'" or char == '"':
            inside_quotes = not inside_quotes

        if not inside_quotes:
            if char in mapping:
                transformed_text += mapping[char]
            elif char.lower() in mapping:
                transformed_text += mapping[char.lower()].upper() if char.isupper() else mapping[char.lower()]
            elif char.lower() == 'g':
                transformed_text += 'г' if char.islower() else 'Г'
            elif char.lower() == 'h':
                transformed_text += 'н' if char.islower() else 'Н'
            else:
                transformed_text += char
        else:
            transformed_text += char

    return transformed_text

def handle_transform():
    language = language_var.get()
    input_text = text_entry.get()
    if language == 'rus':
        transformed_text = transform_text(input_text, keyboard_mapping_rus)
    elif language == 'eng':
        transformed_text = transform_text(input_text, keyboard_mapping_eng)
    else:
        transformed_text = "Выбран неверный язык."
    result_label.config(text=transformed_text)

root = tk.Tk()
root.title("Keyboard Transformation")

language_var = tk.StringVar()
language_var.set("rus")

language_label = tk.Label(root, text="Выберите язык (русский - 'rus', английский - 'eng'): ")
language_label.pack()

language_entry = tk.Entry(root, textvariable=language_var)
language_entry.pack()

text_label = tk.Label(root, text="Введите текст: ")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

submit_button = tk.Button(root, text="Transform", command=handle_transform)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
