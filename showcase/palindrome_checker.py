class PalindromeChecker:

    def __init__(self,user_input):
        self.user_input = user_input 

    def check_input(self):
        input_formatted = ''.join(char for char in self.user_input.lower() if char.isalnum())

        input_list = list(input_formatted)
        input_list.reverse()
        reverse_str = ''.join(input_list)
        
        return reverse_str==input_formatted 







