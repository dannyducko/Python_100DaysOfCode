alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# original set up. Can be tidied up as per below.

# def encrypt(message, shift_amount):
#     cypher_text = ""
#     for char in message:
#         letter_index = alphabet.index(char) + shift_amount
#         if letter_index > len(alphabet):
#             letter_index -= len(alphabet)
#         cypher_text += alphabet[letter_index]
#     print(f"The encoded message: {cypher_text}")
#
#
# # no need to play with shift amount as python handles -indices by starting from the end.
# def decrypt(message, shift_amount):
#     cypher_text = ""
#     for char in message:
#         letter_index = alphabet.index(char) - shift_amount
#         cypher_text += alphabet[letter_index]
#     print(f"The encoded message: {cypher_text}")


def caesar(message, shift_amount, cypher_direction):
    cypher_text = ""
    for char in message:
        if cypher_direction == "encode":
            letter_index = alphabet.index(char) + shift_amount
            if letter_index > len(alphabet):
                letter_index -= len(alphabet)
            cypher_text += alphabet[letter_index]
        elif cypher_direction == "decode":
            letter_index = alphabet.index(char) - shift_amount
            cypher_text += alphabet[letter_index]
        else:
            exit()
    print(f"The {cypher_direction}d message: {cypher_text}")


#Course solution.
def caesar1(message, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d results: {end_text}")

caesar(message=text, shift_amount=shift, cypher_direction=direction)
