class PalindromeChecker:

    def __init__(self,user_input):
        self.user_input = user_input 

    def check_input(self):
        input_form = ''.join(char for char in self.user_input.lower() if char.isalnum())

        input_list = list(input_form)
        input_list.reverse()
        reverse_str = ''.join(input_list)

        if len(input_form) < 1:
            return None
        else:
            return reverse_str==input_form







