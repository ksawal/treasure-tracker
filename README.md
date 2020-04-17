TREASURE TRACKER
--------------------
# What is this?
This project creates two ways to search for a "treasure" inside a formatted map; using a breadth-first search and a depth-first search. All maps must be squares formatted as follows:
1) Select a map dimension
2) Type this map dimension at the top of the file
3) Tile types are ' ', #, @, and $
3) @ is the starting location, $ is the treasure location, ' ' are traversible, and # are non-traversible.
4) All tile characters should be contained within the bounds of the chosen dimension  
**Note:** the map need not be bounded by #'s, but all empty (traversible) tiles must be typed out spaces. Please take a look at maps in the repository for reference. 
--------------------
# How to run
1) Navigate to project directory in terminal
2) Select a maze
3) Select search type
3) Run `$ python3 treasure.py "maze[#].txt" "[depth OR breadth]"`
4) View output in terminal
**Note:** I have not included error-checking because I believe in you! But also because I'm not being graded...
