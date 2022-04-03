alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
lenn = len(alphabet)
step = int(input("Enter the step:\n"))
text = list(input("Enter you message:\n"))
encrypted_text = []
for i in range(len(text)):
    symbol = text[i]
    if symbol in alphabet:
        letter = alphabet.index(symbol)
        if letter + step < lenn:
            symbol = alphabet[letter + step]
        else:
            symbol = alphabet[letter + step - lenn]
        encrypted_text.append(symbol)
    else:
        encrypted_text.append(text[i])
print(''.join(encrypted_text))
