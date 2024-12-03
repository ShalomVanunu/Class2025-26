
line1= "my name is "
line2 = "Shalom vanunu"
line3 = "new new"

with open("text1.txt", "a") as file:
    file.write(line1)
    file.write(line2)

file = open("text4.txt", "r")
#file.write(line1)
#file.write(line2)
file.write(line3)



