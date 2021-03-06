"""
Program: Coupon Calculation.py
Author:  Ondrea Li
Date: 6/10/20

The purpose of this program is to write a function, accept the amount of the purchase,
the cash coupon, the percent coupon,
and it will calculate and return the total order item.

They offer two types of discounts.
The first is cash-off coupons, that you earn by shoppings.
You may apply one $5 or $10 cash off per order.
The second is percent discount coupons for 10%, 15%, or 20% off.
If you have cash-off coupons, those must be applied first,
then apply the percent discount coupons on the pre-tax amount.
Then you add tax at 6% and shipping according to these guidelines:
"""

#What is starting price?
#Which cash coupon are you using?
#What type of discount coupon are you using


def type_of_cash_coupon(initial_cost, coupon_choice):
    #if statements
    if coupon_choice == 5:
        net1 = initial_cost-coupon_choice
        print("Your total after cash coupon is" + str(initial_cost-5))
    elif coupon_choice == 10:
        print("Your total after cash coupon is" + str(initial_cost-10))
        net1 = initial_cost-coupon_choice
    else:
        print("Not applicable")
    return net1

def type_of_discount(net1):
    print(str("type_of_discount"))
    if discount == 10:
        net2 = float(net1*9/10)
        print("Your total after discount is" + "" + str(net2))
    elif discount == 15:
        net2 = float(net1*8.5/10)
        print("Your total after discount is" + "" + str(net1*8.5/10))
    elif discount == 20:
        net2 = float(net1*8/10)
        print("Your total after discount is" + "" + str(net1*8/10))
    else:
        print("Not applicable")
    return net2

def amt_after_shipping(net2):
    if net2 <= 10:
        shipping_cost = 5.95
        print("Your shipping price is $5.95")
    elif 10 < net2 <= 30:
        shipping_cost = 7.95
        print("Your shipping price is $7.95")
    elif 30<= net2 < 50:
        shipping_cost = 11.95
        print("Your shipping price is $11.95")
    else:
        shipping_cost = None
        print("free shipping")
    return shipping_cost

def calculate_pricefn(net2, shipping_cost):
    calculate_price = (net2 +shipping_cost)*1.06
    print(calculate_price)

def end_total(initialcost, coupon, discount, shipping_cost):

    final_cost = ((initialcost - coupon) * (1 - discount/100) + shipping_cost)*1.06
    return final_cost

initial_cost = float(input("What is your initial cost?"))
coupon_choice = float(input("Apply one $5 or $10 coupon"))
discount = float(input("Choose percent discount 10%,15%, 20% "))



C =(amt_after_shipping(type_of_discount(type_of_cash_coupon(initial_cost, coupon_choice))))



final_price = calculate_pricefn(type_of_discount(type_of_cash_coupon(initial_cost, coupon_choice)), C )




if __name__ == '__main__':
    pass



