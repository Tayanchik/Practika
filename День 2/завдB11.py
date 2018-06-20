import string
alphabet_plaintext = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя ,.’'
alphabet_ciphertext = 'mnbvcxzasdfghjklpoiuytrewq-0987654321'
encryption_table = str.maketrans(alphabet_plaintext, alphabet_ciphertext)
decryption_table = str.maketrans(alphabet_ciphertext, alphabet_plaintext)
message = ""
cipher = message.lower().translate(encryption_table)
print('Encrypted message: {}').format(cipher)
print('Decrypted message: {}').format(cipher.translate(decryption_table))
