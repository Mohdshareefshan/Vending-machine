print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

# Create a vending machine

print('_______________')
print('Welcome to the vending machine')
print('-------------------------------')
print('Language = English / عربي')
print('_______________')

# Select language
language = {
    '1': 'English',
    '2': 'عربي'
}
language_codee = input('Please select the language (1 for English, 2 for عربي): ')

if language_codee == '1':
    print('Selected English')
elif language_codee == '2':
    print('تم اختيار اللغة العربية')
else:
    print('Invalid selection. Defaulting to English.')
    language_codee = '1'



def vending_menu(categories):
    """Display the vending machine menu"""
    print('\n--- VENDING MACHINE MENU ---')
    for category, items in categories.items():
        print(f'\n{category}')
        for code, detail in items.items():
            print(f'{code}: {detail["name"]} - ${detail["price"]:.2f} ({detail["stock"]} in stock)')

def get_selection(categories):
    """Prompt user for their selection and quantity"""
    while True:
        try:
            code = int(input('\nEnter the code of the item you would like to purchase: '))
            for items in categories.values():
                if code in items:
                    item = items[code]
                    if item['stock'] > 0:
                        while True:
                            try:
                                quantity = int(input(f'Enter the quantity you need (Available: {item["stock"]}): '))
                                if 1 <= quantity <= item['stock']:
                                    return code, item, quantity
                                else:
                                    print(f'Invalid quantity. Please choose between 1 and {item["stock"]}.')
                            except ValueError:
                                print('Invalid input. Please enter a number.')
                    else:
                        print('Sorry, that item is out of stock. Please choose another.')
                        break
            else:
                print('Invalid code. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def process_payment(total_price):
    """Handle payment and return the change"""
    while True:
        try:
            amount = float(input(f'The total price is ${total_price:.2f}. Please insert cash: '))
            if amount < total_price:
                print(f'Insufficient amount. You need ${total_price - amount:.2f} more.')
            else:
                return amount, amount - total_price
        except ValueError:
            print('Invalid input. Please enter a valid amount.')
def suggest_complementary_item(code, categories):
    """Suggest a complementary item to the user"""
    if code in complementary_items:
        comp_code = complementary_items[code]
        for items in categories.values():
            if comp_code in items:
                comp_item = items[comp_code]
                if comp_item['stock'] > 0:
                    response = input(f"Would you like to add {comp_item['name']} for ${comp_item['price']:.2f}? (yes/no): ").strip().lower()
                    if response == 'yes':
                        return comp_code, comp_item
    return None, None
def apply_discount(total_price):
    """Apply a 10% discount if the total price exceeds $10"""
    if total_price > 10:
        discount = total_price * 0.10
        total_price -= discount
        print(f'A discount of ${discount:.2f} has been applied.')
    return total_price

def vending_machine():
    """Main function to operate the vending machine"""
    # Define categories
categories = {
    "Snacks": {
        1: {'name': 'Chips', 'price': 1.50, 'stock': 10},
        2: {'name': 'KitKat', 'price': 2.50, 'stock': 5},
        3: {'name': 'Cookies', 'price': 4.00, 'stock': 7},
        4: {'name': 'Oreo Biscuit', 'price': 3.00, 'stock': 6},
    },
    "Drinks": {
        5: {'name': 'Water', 'price': 1.00, 'stock': 10},
        6: {'name': 'Coffee', 'price': 3.50, 'stock': 8},
        7: {'name': 'Chocolate Shake', 'price': 5.00, 'stock': 7},
        8: {'name': 'Mountain Dew', 'price': 2.50, 'stock': 10},
    }
}

categories_ar = {
    "وجبات خفيفة": {
        1: {'name': 'رقائق', 'price': 1.50, 'stock': 10},
        2: {'name': 'كيت كات', 'price': 2.50, 'stock': 5},
        3: {'name': 'بسكويت', 'price': 4.00, 'stock': 7},
        4: {'name': 'بسكويت أوريو', 'price': 3.00, 'stock': 6},
    },
    "مشروبات": {
        5: {'name': 'ماء', 'price': 1.00, 'stock': 10},
        6: {'name': 'قهوة', 'price': 3.50, 'stock': 8},
        7: {'name': 'ميلك شيك شوكولاتة', 'price': 5.00, 'stock': 7},
        8: {'name': 'ماونتن ديو', 'price': 2.50, 'stock': 10},
    }
}
complementary_items = {
    1: 5,  # Chips -> Water
    2: 6,  # KitKat -> Coffee
    3: 7,  # Cookies -> Chocolate Shake
    4: 8,  # Oreo Biscuit -> Mountain Dew
    5: 1,  # Water -> Chips
    6: 2,  # Coffee -> KitKat
    7: 3,  # Chocolate Shake -> Cookies
    8: 4   # Mountain Dew -> Oreo Biscuit
}

selected_categories = categories if language_codee == '1' else categories_ar


# Assign the selected categories
if language_codee == '2':  # Arabic
    selected_categories = categories_ar
else:  # Default to English
    selected_categories = categories
while True:
        vending_menu(selected_categories)
        code, item, quantity = get_selection(selected_categories)
        print(f'\nDispensing {quantity} x {item["name"]}...')
        
        # Calculate total price
        total_price = item["price"] * quantity
        total_price = apply_discount(total_price)      
        # Process payment
        amount_paid, change = process_payment(total_price)
        print(f'\nPayment successful. Change: ${change:.2f}')
        
        # Decrease stock
        item["stock"] -= quantity
        # Suggest complementary item
        comp_code, comp_item = suggest_complementary_item(code, selected_categories)
        if comp_item:
            total_price = comp_item["price"]
            amount_paid, change = process_payment(total_price)
            print(f'\nDispensing 1 x {comp_item["name"]}...')
            comp_item["stock"] -= 1
            print(f'\nPayment successful. Change: ${change:.2f}')

        # Ask the user to buy another item
        another = input('\nWould you like to buy another item? (yes/no): ').strip().lower()
        if another != 'yes':
            print('\nThank you for using the vending machine!')
            break

# Run the vending machine
if __name__ == "__main__":
    vending_machine()
