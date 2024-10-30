from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return sum(char.isdigit() for char in self.data)
    
        # count = 0
        # for char in self.data:
        #     if char.isdigit():
        #         count += 1

        # return count
    
my_string = NumberString("1234hhhhh")
print(my_string.number_count())
