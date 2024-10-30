from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(value for value in self.data if value > 0)
        # # def amount_payment(payment):
        # sum = 0
        # for value in self.data:
        #     if value > 0:
        #         sum = sum + value
        # return sum

payment = [1, -3, 4]

my_list = AmountPaymentList(payment)
print(my_list.amount_payment())
