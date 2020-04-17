"""
Kabir Sawal, 2020
DISCLAIMER: This code is for educational use only!
            Please do not use it for school projects
            or assignments.
Repository available at https://github.com/ksawal/treasure-tracker
"""

import sys
import copy

class Treasure:
    
    #read in maze file
    def readMaze(self):
    
        #read in the file
        fName = sys.argv[1]
        self.searchType = sys.argv[2]
        file = open(fName,"r")
        self.map_size = int(file.readline()) #read in map's size
        self.map = []
        
        #parse through the file and create the map
        column_count = 0
        row_count = 0
        while row_count < self.map_size:
            current_row = []
            row_string = file.readline()
            if row_count+1 < self.map_size: row_string = row_string[:-1]
            for i in range(0,len(row_string)):
                current_row.append(row_string[i])
                if row_string[i] == '@':
                    self.start_row = row_count
                    self.start_col = i
            row_count += 1
            self.map.append(current_row)
        
        self.route = copy.deepcopy(self.map)
            
    #look at four sides
    def search(self):
        #add starting tile to stack
        self.stack = []
        self.found = False
        self.treasure_location = (('Not found'))
        self.stack.append((self.start_row,self.start_col))

        while len(self.stack) > 0:
            #move to next tile
            if self.searchType == "depth": current_tile = self.stack.pop()
            elif self.searchType == "breadth": current_tile = self.stack.pop(0)
            row = current_tile[0]
            col = current_tile[1]
            for direction in range (4): # 1 = north, 2 = east, 3 = west, 4 = south
                if direction == 0 and (row-1) >= 0: #NORTH
                    if self.map[row-1][col] == '$': #find treasure
                        self.treasure_location = (row-1,col)
                        self.found = True
                        self.map[row-1][col] = 'N' #mark direction of travel
                    elif self.map[row-1][col] == ' ': #no treasure
                        self.stack.append((row-1,col)) #push tile to stack
                        self.map[row-1][col] = 'N' #mark direction of travel
                if self.found: return
                if direction == 1 and (col+1) < self.map_size: #EAST
                    if self.map[row][col+1] == '$': #find treasure
                        self.treasure_location = (row,col+1)
                        self.found = True
                        self.map[row][col+1] = 'E' #mark direction of travel
                    elif self.map[row][col+1] == ' ': #no treasure
                        self.stack.append((row,col+1)) #push tile to stack
                        self.map[row][col+1] = 'E' #mark direction of travel
                if self.found: return
                if direction == 2 and (col-1) >= 0: #WEST
                    if self.map[row][col-1] == '$': #find treasure
                        self.treasure_location = (row,col-1)
                        self.found = True
                        self.map[row][col-1] = 'W' #mark direction of travel
                    elif self.map[row][col-1] == ' ': #no treasure
                        self.stack.append((row,col-1)) #push tile to stack
                        self.map[row][col-1] = 'W' #mark direction of travel
                if self.found: return
                if direction == 3 and (row+1) < self.map_size: #SOUTH
                    if self.map[row+1][col] == '$': #find treasure
                        self.treasure_location = (row+1,col)
                        self.found = True
                        self.map[row+1][col] = 'S' #mark direction of travel
                    elif self.map[row+1][col] == ' ': #no treasure
                        self.stack.append((row+1,col)) #push tile to stack
                        self.map[row+1][col] = 'S' #mark direction of travel
                if self.found: return
    
    #draw route
    def path(self):
        if not self.found:
            print("Your search was for naught...")
            exit()
        self.steps = 0
        directions = []
        current_tile = self.treasure_location
        
        while(current_tile[0] != self.start_row & current_tile[1] != self.start_col):
            self.steps += 1
            if self.map[current_tile[0]][current_tile[1]] == 'N': #NORTH
                if self.map[current_tile[0]+1][current_tile[1]] != '@': #check for start
                    self.route[current_tile[0]+1][current_tile[1]] = '+' #mark route
                    directions.append((current_tile[0]+1,current_tile[1]))
                current_tile = (current_tile[0]+1,current_tile[1]) #move to next tile
                    
            elif self.map[current_tile[0]][current_tile[1]] == 'E': #EAST
                if self.map[current_tile[0]][current_tile[1]-1] != '@': #check for start
                    self.route[current_tile[0]][current_tile[1]-1] = '+' #mark route
                    directions.append((current_tile[0],current_tile[1]-1))
                current_tile = (current_tile[0],current_tile[1]-1) #move to next tile
                
            elif self.map[current_tile[0]][current_tile[1]] == 'W': #WEST
                if self.map[current_tile[0]][current_tile[1]+1] != '@': #check for start
                    self.route[current_tile[0]][current_tile[1]+1] = '+' #mark route
                    directions.append((current_tile[0],current_tile[1]+1))
                current_tile = (current_tile[0],current_tile[1]+1) #move to next tile
                
                
            elif self.map[current_tile[0]][current_tile[1]] == 'S': #SOUTH
                if self.map[current_tile[0]-1][current_tile[1]] != '@': #check for start
                    self.route[current_tile[0]-1][current_tile[1]] = '+' #mark route
                    directions.append((current_tile[0]-1,current_tile[1]))
                current_tile = (current_tile[0]-1,current_tile[1]) #move to next tile
                
        ending = "It took " + str(self.steps) + " steps to find the treasure. It was found at " + str(self.treasure_location) + ". This was the path taken:\n"
        print(ending)
        for i in self.route:
            print ("".join(i))
        print("\n")
        
        print("If you'd like to find the treasure yourself, follow these directions:\n")
        for i in range(len(directions)):
            print(directions[len(directions) - i - 1])

#main function
def main():
    game = Treasure()
    game.readMaze()
    game.search()
    game.path()
if __name__ == '__main__': main()
