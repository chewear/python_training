from pages.page_rates import PageRates
from pages.page_convert import ConvertMenu
from pages.page_main_menu import MainMenu

class Router:
    def route_choice(self):
        main_menu = MainMenu()
        choice = main_menu.display()
        pages = {
            1: PageRates().display_rates,
            2: ConvertMenu().input_menu
        }

        while True:
            try:
                choice = int(choice)
                if choice in pages.keys():
                    pages[choice]()
                    choice = main_menu.display()
                else:
                    print(f"Invalid option. Please choose from {list(pages.keys())}.")
                    choice = main_menu.display()
            except ValueError:
                print("Invalid input. Please enter a number.")
                choice = main_menu.display()
