#very simple but yet effective code
__doc__ = """
to use this module properly you should first inherit from clon base class
than you can use dump function to take a dictionary which contains the changes since the last dump call
at last can use load function to apply these values to another clon inherited object
"""

class clon:#don't instance from this, inherit instead
    def dump(self):#use to sum up changed values in one dictionary object
        returndict = {}
        try:
            self.lastcopy#a dictionary to filter changed values.If there is none, it defines one in order to get catched by a nameerror 
        except AttributeError:
            self.lastcopy = {}
        for var in self.__dict__:
            if not var in self.lastcopy:#if a new variable defined since the last dump call, it gets recorded here
                returndict[var] = self.__dict__[var]
            else:
                if not self.lastcopy[var] == self.__dict__[var]:#if a variable has changed since the last dump call, it gets recorded here 
                    returndict[var] = self.__dict__[var]
        del self.__dict__["lastcopy"]
        self.lastcopy = {}
        for var in self.__dict__:
            self.lastcopy[var] = self.__dict__[var]
        if "lastcopy" in returndict:
            del returndict["lastcopy"]
        return returndict

    def dump_all(self):#to be used with compare method
        returndict = {}
        for var in self.__dict__:#copying value
            returndict[var] = self.__dict__[var]

        if "lastcopy" in returndict:
            del returndict["lastcopy"]
        return returndict

    def compare(self, data):#to get a dict containing changed or new values
        returndict = {}
        for var in self.__dict__:
            if not var in data:
                returndict[var] = self.__dict__[var]

            else:
                if not data[var] == self.__dict__[var]:
                    returndict[val] = var
        if "lastcopy" in returndict:
            del returndict["lastcopy"]
        return returndict


    def load(self, data):#the main way to load a pre-dumped dict
        for var in data:
            self.__dict__[var] = data[var]
