import base64

def encode(text):
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded_text

def decode(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
    return decoded_text

def main():
    print("Welcome to HyperEncoder!")
    while True:
        choice = input("Do you want to (E)ncode or (D)ecode? (Q to quit): ").upper()
        if choice == 'E':
            text = input("Enter text to encode: ")
            print("Encoded text:", encode(text))
        elif choice == 'D':
            encoded_text = input("Enter text to decode: ")
            print("Decoded text:", decode(encoded_text))
        elif choice == 'Q':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
