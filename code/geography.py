###########################
#                         #
# teacup geography module #
#                         #
###########################

def gen_quad(size):
#generates a quadrant of the globe
#uses dictionaries as the entries
#takes a scalar, size, which should be multiple of 2
#returns a 3D-array


class Region():
#one tile on the globe
#eg. north polar cap

    def __init__(self, z, y, x):
    #constructor for Region
    #takes z, y, x
    #returns the constructed Region
    
        self.z = z
        self.xmin = x
        self.xmax = x
        self.ymin = y
        self.ymax = y
        self.biome = 0
        self.pop = []
        self.grid = []
        
    def expand(self, y, x):
    #expands a Region into more cords
    #takes itself
    #returns itself
        self.ymin = min(self.ymin, y)
        self.ymax = max(self.ymax, y)
        self.xmin = min(self.xmin, x)
        self.xmax = max(self.xmax, x)
        return self
        
class Globe():
#the entire globe, with sun and moon

    def __init__(self, size=8):
    #constructor for Globe
    #also generates Globe
    #takes a scalar, size
    #returns itself
        
        size = size - (size % 2)
        self.equator = size
        grid_max_z = (size / 2) + 2
        grid_max_y = (size * 2) + 1
        grid_max_x = (size * 4)
        grid = []
        
        #core
        layer = []
        for y in range(grid_max_y):
            row = []
            for x in range(grid_max_x):
                row.append({'z'=0, 'ymin'=0, 'ymax'=grid_max_y, 'xmin'=0, 'xmax'=grid_max_x})
            layer.append(row[:])
        grid.append(layer[:])
        #cube
        layer = []
        for y in range(grid_max_y):
            row = []
            for x in range(grid_max_x):
                row.append({'z'=0, 'ymin'=0, 'ymax'=grid_max_y, 'xmin'=0, 'xmax'=grid_max_x})
            layer.append(row[:])
        grid.append(layer[:])
        
    
        
        