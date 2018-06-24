# clon
Can be used as a very primitive serialization method. The very focus of this module is the data size as it planned to be used together with sockets


The proper way to use this module is to inherit from clon base class
after inheriting you can get a dictionary object which contains changes since the last dump call
you can later use this dictionary object to apply these values to another clon inherited object or use them as you wish
