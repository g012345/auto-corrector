keyboard_mapping = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'",
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`',
    'Q': 'й', 'W': 'ц', 'E': 'у', 'R': 'к', 'T': 'е', 'Y': 'н', 'U': 'г', 'I': 'ш', 'O': 'щ', 'P': 'з', '[': 'х', ']': 'ъ',
    'A': 'ф', 'S': 'ы', 'D': 'в', 'F': 'а', 'G': 'п', 'H': 'р', 'J': 'о', 'K': 'л', 'L': 'д', ';': 'ж', "'": 'э',
    'Z': 'я', 'X': 'ч', 'C': 'с', 'V': 'м', 'B': 'и', 'N': 'т', 'M': 'ь', ',': 'б', '.': 'ю', '`': 'ё'
}

def transform_text(text):
    transformed_text = ''
    for char in text:
        if char in keyboard_mapping:
            transformed_text += keyboard_mapping[char]
        elif char.lower() == 'g':
            transformed_text += 'g'
        else:
            transformed_text += char
    return transformed_text

input_text = input()
transformed_text = transform_text(input_text)
print(transformed_text)  
