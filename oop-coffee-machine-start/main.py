
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_=Menu()
coffee_maker_=CoffeeMaker()
money_machine_=MoneyMachine()
is_on=True

while is_on:
    choice_ = input(f"What would you like? {menu_.get_items()}: ").lower()
    if choice_=="off":
        exit()
    elif choice_ == "report":
        coffee_maker_.report()
        money_machine_.report()
    else:
        order=menu_.find_drink(choice_)
        if not order:
            continue
        if coffee_maker_.is_resource_sufficient(order) and  money_machine_.make_payment(order.cost):
             coffee_maker_.make_coffee(order)
        else:
            exit()
