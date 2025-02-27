class Recording:
    def __init__(self, length):
        self.__length = length  
    
    def get_length(self):
        return self.__length  
    
    def set_length(self, length):
        self.__length = length  

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        self.__length = length

the_wall = Recording(43)
print(the_wall.length) 

the_wall.length = 44  
print(the_wall.length)  
