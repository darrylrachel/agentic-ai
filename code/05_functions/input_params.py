chai = [ 1, 2, 3, 4 ]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeelin", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keywords


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="Yes")

def special_chai_args(*args, **kwargs):
    print("Ingredients", args)
    print("Extras", kwargs)

special_chai_args("Cinnamon", "Cardmom", sweetener="Honey", foam="Yes")


def chai_orders(order="default"):
    