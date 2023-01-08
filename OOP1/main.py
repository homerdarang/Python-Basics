from turtle import Turtle, Screen
from prettytable import PrettyTable

#  USING TURTLE & SCREEN PACKAGES
# tim = Turtle()
# tim.shape("turtle")
# tim.color("cyan2")
# tim.forward(100)


# screen = Screen()

# screen.exitonclick()


#  USING PRETTTTABLE PACKAGE
table = PrettyTable()
table.add_column("Name", ["Homer", "Kali", "Harriet"])
table.add_column("Age", [28, 1, 10])
table.add_column("Talent", ["Singing", "None", "None"])
table.add_column("Likes", ["Coding", "Eating", "Playing"])
table.align = "l"

print(table)

# Turtle Module and OOP
# Renamed base folder



