"""
Program: Coupon Calculation.py
Author:  Ondrea Li
Date: 6/10/20

This program
"""

#What is starting price?
#Which cash coupon are you using?
#What type of discount coupon are you using

def online_shopping_insert():
    amt = int(input("Enter the price of your item"))
    return amt_after_shipping(amt)


#check for ranges

#up to $10 dollars, shipping is $5.95
#$10 and up to $30 dollars, shipping is $7.95
#$30 and up to $50 dollars, shipping is $11.95
#Shipping is free for $50 and over

def amt_after_shipping(amt):
    if amt <= '10':
        Shipping_cost = '5.95'
    elif amt > '10' 'AND' <='30':
        Shipping_cost = '7.95'
    elif amt >='30' 'AND' < '50':
        Shipping_cost = '11.95'
    else:
        print("free shipping")

#calcuating discounts
def types_of_coupon():
     cash_coupon = input(int("Apply one $5, or $10 cash off pre order"))
     discount_coupon = input(int("Apply one 10%, 15%, or 20% off"))
#Subtracting Cash_coupons

def type_of_cash_coupon():
    if cash_coupon == "5":
        print("-5")
    elif cash_coupon == "10":
        print("-10")

def type_of_Discount_coupon():
    if Discount_coupon == 10:
        Total_1 = amt*0.9
    elif Discount_coupon == 15:
        Total_1 = amt*0.85
    elif Discount_coupon == 20:
        Total_1 = amt*0.80
    else:
        print("Not applicable")


    #do some math
    return value





def calculate_price(price, cash_coupon, percent_coupon):
    price= input(int(amt +

    pass



def sub_total()
    tax = calculate_price * 1.06

print('Your total price is')

   #do i have a cash coupon? how does it affect the outcome
   #do i have a discount?
   #what is the shipping cost? How can I calculate that/add it inm



    #suptotal, now add tax
    #return your total value

    pass


if __name__ == '__main__':
    pass


remainder:


#calcuating discounts

cash_coupon = input(int("Apply one $5, or $10 cash off pre order"))
discount_coupon = input(int("Apply one 10%, 15%, or 20% off"))
#Subtracting Cash_coupons

def type_of_cash_coupon():
    if cash_coupon == "5":
    add '5'
        print("5")
        coupon = '5'
        return
    elif cash_coupon == "10":
        print("-10")
        coupon = '10'
        return
    return type_of_cash_coupon

def type_of_discount_coupon():
    if discount_coupon == 10:
        Total_1 = amt_after_shipping()* 0.9
    elif discount_coupon == 15:
        Total_1 = amt_after_shipping(*0.85
    elif discount_coupon == 20:
        Total_1 = amt*0.80
    else:
        print("Not applicable")
    return type_of_discount_coupon



def calculate_price(price, cash_coupon, percent_coupon):
    price= input(int(amt + amt_after_shipping()


'price' + 'tax' = calculate_price * 1.06
sub_total = print str(input("Your sub total is" ""))

print("Your total price is" + str(amt) + )

   #do i have a cash coupon? how does it affect the outcome
   #do i have a discount?
   #what is the shipping cost? How can I calculate that/add it inm



    #suptotal, now add tax
    #return your total value

    pass



   def test_price_more_thanequal_10_lessthan_20(self):
        value_under_ten = 27.99
        shipping = 7.95
        self.assertAlmostEqual(cc.calculate_pricefn(5, 10, value_under_ten), 9.16, places=2)
        self.assertAlmostEqual(cc.calculate_pricefn(5, 15, value_under_ten), 9.00, places=2)
        self.assertAlmostEqual(cc.calculate_pricefn(5, 20, value_under_ten), 8.84, places=2)
        self.assertAlmostEqual(cc.calculate_pricefn(10, 10, value_under_ten), 4.39, places=2)
        self.assertAlmostEqual(cc.calculate_pricefn(10, 15, value_under_ten), 4.50, places=2)
        self.assertAlmostEqual(cc.calculate_pricefn(10, 20, value_under_ten), -2.01, places=2)


