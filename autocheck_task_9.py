from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return [key for key, key_value in self.data.items() if key_value == value ]
        # keys = []
        # for key, key_value in self.data.items():
        #     if key_value == value:
        #         keys.append(key)
        # return keys
    
    def print_dict(self):
        print(self.data)
    
d = {"a": 1, "b": 1, "c": 3}

my_dict = LookUpKeyDict(d)
# my_dict.print_dict()
print(my_dict.lookup_key(1))
