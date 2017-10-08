import unittest

class MenuChoices(unittest.TestCase):

    def get_main_menu_choice(self):
      menu_choice = GetMainMenuChoice(2)
        self.assert(menu_choice, 3)

if __name__ == '__main__':
    unittest.main()