### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                return False
            return True
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        large = int(input("how many large dollars?: "))
        half = int(input("how many half dollars?: "))
        quarter = int(input("how many quarters? :"))
        nickel = int(input("how many nickels? :"))
        total = (large * 1.0) + (half * 0.5) + (quarter * 0.25) + (nickel * 0.05)
        return total

    def transaction_result(self, coins, cost):
        return coins >= cost

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()
    if choice == 'off':
        break
    elif choice == 'report':
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} ounce(s)")
    elif choice in ['small', 'medium', 'large']:
        recipe = recipes[choice]
        ingredients_needed = recipe['ingredients']
        cost = recipe['cost']
        if machine.check_resources(ingredients_needed):
            print("Please insert coins.")
            total_inserted = machine.process_coins()
            if machine.transaction_result(total_inserted, cost):
                change = total_inserted - cost
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                machine.make_sandwich(choice, ingredients_needed)
                print(f"{choice} sandwich is ready. Bon appetit!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            for ingredient, required in ingredients_needed.items():
                if machine.machine_resources[ingredient] < required:
                    print(f"Sorry there is not enough {ingredient}.")
                    break
    else:
        print("Invalid choice. Please try again.")