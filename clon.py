#very simple but yet effective code
__doc__ = """
to use this module properly you should first inherit from clon base class
than you can use dump function to take a dictionary which contains the changes since the last dump call
at last can use load function to apply these values to another clon inherited object
"""

class clon:#don't instance from this, inherit instead
    def dump(self):#use to sum up changed values in one dictionary object
        try:
            self.lastcopy#a dictionary to filter changed values.If there is none, it defines one in order to get catched by a nameerror 
        except NameError:
            self.lastcopy = None
         for var, val in self.__dict__:
            if not var in self.lastcopy:#if a new variable defined since the last dump call, it gets recorded here
                returndict[var] = val

            else:
                if not self.lastcopy[var] == val:#if a variable has changed since the last dump call, it gets recorded here 
                    returndict[var] = val

        self.lastcopy = self.__dict__
        return returndict

    def dump_all(self):#to be used with compare method
        return self.__dict__

    def compare(self, data):#to get a dict containing changed or new values
        returndict = {}
        for var, val in self.__dict__:
            if not var in data:
                returndict[var] = val

            else:
                if not data[var] == val:
                    returndict[val] = var

        return returndict


    def load(self, data):#the main way to load a pre-dumped dict
        for var, val in data:
            self.__dict__[var] = val