# from turtle import Turtle,Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Squirtle", "Charmander"])
table.add_column("Type", ["Grass", "Water", "Fire"])
table.align = "l"

print(table)