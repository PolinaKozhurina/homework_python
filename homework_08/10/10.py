message_word = input("Enter encrypted message:\n")
message_list = list(message_word)
decrypted_mess = []
for i in range(len(message_list)):
    if i % 2 == 0:
        decrypted_mess.append(message_list[i])
for i in range(len(message_list) - 1, -1, -1):
    if i % 2 != 0:
        decrypted_mess.append(message_list[i])
decrypted_mess = [''.join(decrypted_mess)]
print(decrypted_mess)
