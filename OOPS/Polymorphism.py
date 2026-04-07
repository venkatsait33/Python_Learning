# 🔹 Concept
# Same method name → different behavior


class payment:
    def pay(self):
        print("paying salary")
        
class UPI(payment):
    def pay(self):
        print("paying salary to upi")

class DebitCard(payment):
    def pay(self):
        print("paying salary to debit card")

# we created a class called payment and we created a method called pay
# we created two classes called UPI and DebitCard and we overrode the pay method
# we created a function called make_payment and we passed in a method as an argument
# we called the pay method on the method that was passed in

def make_payment(method):
    method.pay()
    
make_payment(UPI())
make_payment(DebitCard())