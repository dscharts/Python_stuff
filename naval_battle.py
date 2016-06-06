from random import randint

print "Welcome to Your Death"

game = True

ocean = []

columns = input("Choose number of columns")
lines = input("Choose number of lines")

li = ['0'] * columns

for x in range(lines):
    ocean.append(["O"] * columns)

ship_line = randint(0, lines-1)
ship_column = randint(0, columns-1)


def make_ocean(t):
    for li in t:
        print " ".join(li)

while game:
    make_ocean(ocean)

    try_line = input("Which line? Be careful with your answer...") -1
    try_column = input("Which column? Be afraid of the answer...") -1

    if try_line == ship_line and try_column == ship_column:
        print "You've survived... for now"
        game = False
    elif try_line >= lines or try_column >= columns:
        print "No"
    elif ocean[try_line][try_column] == "Y":
        print "Don't be stupid"
    else:
        print "Try again"
        ocean[try_line][try_column] = "Y"
        
