<<<<<<< HEAD
<<<<<<< HEAD
"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of bricks ($/m^2): "))

total_concrete = (foundation_length * foundation_width * foundation_height)
total_cost_of_concrete = (cost_of_concrete * total_concrete)
total_brick = ((wall_height * foundation_width) * 2) + \
    ((wall_height * foundation_length) * 2)
total_cost_of_bricks = (cost_of_bricks * total_brick)
total_cost = (total_cost_of_concrete + total_cost_of_bricks)

print(f"""\nConcrete needed for foundation (m^3): {total_concrete:.2f}
Cost of concrete: ${total_cost_of_concrete:,.2f}
Bricks needed for walls (m^2): {total_brick:.2f}
Cost of bricks: ${total_cost_of_bricks:,.2f}
Total cost: ${total_cost:,.2f}""")
=======
"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of bricks ($/m^2): "))

total_concrete = (foundation_length * foundation_width * foundation_height)
total_cost_of_concrete = (cost_of_concrete * total_concrete)
total_brick = ((wall_height * foundation_width) * 2) + \
    ((wall_height * foundation_length) * 2)
total_cost_of_bricks = (cost_of_bricks * total_brick)
total_cost = (total_cost_of_concrete + total_cost_of_bricks)

print(f"""\nConcrete needed for foundation (m^3): {total_concrete:.2f}
Cost of concrete: ${total_cost_of_concrete:,.2f}
Bricks needed for walls (m^2): {total_brick:.2f}
Cost of bricks: ${total_cost_of_bricks:,.2f}
Total cost: ${total_cost:,.2f}""")
>>>>>>> d6eb7da952c8681bd6e50193b3ad6c73c6ea18f6
=======
"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of bricks ($/m^2): "))

total_concrete = (foundation_length * foundation_width * foundation_height)
total_cost_of_concrete = (cost_of_concrete * total_concrete)
total_brick = ((wall_height * foundation_width) * 2) + \
    ((wall_height * foundation_length) * 2)
total_cost_of_bricks = (cost_of_bricks * total_brick)
total_cost = (total_cost_of_concrete + total_cost_of_bricks)

print(f"""\nConcrete needed for foundation (m^3): {total_concrete:.2f}
Cost of concrete: ${total_cost_of_concrete:,.2f}
Bricks needed for walls (m^2): {total_brick:.2f}
Cost of bricks: ${total_cost_of_bricks:,.2f}
Total cost: ${total_cost:,.2f}""")
>>>>>>> d6eb7da952c8681bd6e50193b3ad6c73c6ea18f6
