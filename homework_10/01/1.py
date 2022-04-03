vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input("Enter the text: ")
text = list(text)
vowels_text = [text[i] for i in range(len(text)) if text[i] in vowels]
print("The list of vowels: ", vowels_text)
print("Amount: ", len(vowels_text))
