
class TSPParser:
    def __init__(self, filename):
        self.city_coords = {}# list of coords in file
        self.city_tour_init = [] #
        self.city_tour_tuples = []
        self.filename = filename
        self.display_status = ''
        if self.check_filename(filename):
            content = self.read_filename(filename) #read a file
            #print(content)# file splite every line
            self.dimension = self.get_dimension(content) # counter of cities
            if self.check_dimension(self.filename, self.dimension):
                self.city_coords = self.get_city_coord(self.content) ## make all pointler at coordinat
                #print(self.city_coords) # {1: ('41', '49'), 2: ('35', '17'), 3: ('55', '45'),......
                self.city_tour_init = self.create_initial_tour() ## take all cites
                #print(self.city_tour_init) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,....
                self.city_tour_tuples = self.create_initial_coord_tuples()# take all corr
                #print(self.city_tour_tuples)#[('41', '49'), ('35', '17'), ('55', '45'), ('55', '20'), ('15', '30'), ('25', '30'),.....

            else:
                self.display_status = ('Dimension of the file do not match with the name of the file!\n'
                                       'Please make sure you have a valid TSP data file.\n'
                                       'Please use another file or correct the one you have')
        else:
            self.display_status = 'This is not a valid TSP file, should look like example.tsp.Please use another one!'

    def check_filename(self, filename):
        """
            Check if the file provided is a valid TSP data file
            ...ends with .tsp
        """
        if self.filename.endswith(".tsp"):
            return True
        else:
            return False


    def read_filename(self, filename):
        """
            Read the TSP file line by line in a list
        """
        with open(self.filename) as f:
            self.content = f.read().splitlines()
        return self.content

    def get_dimension(self, content):
        """
            Check for the line DIMENSION and return the number
        """

        for line in self.content:
            if line.startswith("DIMENSION"):
                index, space, rest = line.partition(':')
                return rest.strip()

    def check_dimension(self, filename, dimension):
        """
            Checks if the dimension found in the TSP data matches
            the name of the file provided. ex. if you provide a file
            named "eil101.tsp" the dimension in the file should be "101"
        """
        self.dimension = dimension
        self.filename = filename
        if self.dimension in self.filename:
            return True
        else:
            return True
    def get_city_coord(self, content):
        """
            Returns the cities with their coordinates in a dict
            like {1: ('41', '49'), 2: ('35', '17'), 3: ('55', '45'), 4: ('55', '20'), 5: ('15', '30'), 6: ('25', '30'), 7: ('20', '50'), 8: ('10', '43'), 9: ('55', '60') .....
        """
        start = self.content.index("NODE_COORD_SECTION") # start with 5
        end = self.content.index("EOF")# end with 101
        for line in self.content[start + 1:end]:
            line = line.strip()
            city, space, coord = line.partition(" ")
            coord = coord.strip()
            x, space, y = coord.partition(" ")
            self.city_coords[int(city)] = (x.strip(), y.strip())
        return self.city_coords

    def create_initial_tour(self):
        for i in range(1, int(self.dimension) + 1):
            self.city_tour_init.append(i)
        return self.city_tour_init

    def create_initial_coord_tuples(self):
        city_tour_init = self.city_tour_init
        content = self.city_coords
        for i in city_tour_init:
            self.city_tour_tuples.append(content.get(i))
        return self.city_tour_tuples




