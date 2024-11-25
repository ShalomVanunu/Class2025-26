

with open("text.txt", "r") as file:
    file_cont= file.readlines()

for sentence in file_cont:
    for letter in sentence.removesuffix("\n"):
        print(letter)