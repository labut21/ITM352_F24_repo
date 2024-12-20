from cryptography.fernet import Fernet 
 
# Generate a key 
key = Fernet.generate_key() 
cipher_suite = Fernet(key) 
 
# Get string input from the user 
user_input = input("Enter a string to encrypt: ") 
 
# Encode the string to bytes, encrypt it, and then print  
encoded_text = user_input.encode() # Encode the strng 
encrypted_text = cipher_suite.encrypt(encoded_text) 
print("Encrypted:", encrypted_text) 
 
# Decrypt the encrypted text and decode back to string  
decrypted_bytes = cipher_suite.decrypt(encrypted_text) 
decrypted_text = decrypted_bytes.decode()  
print("Decrypted:", decrypted_text) 