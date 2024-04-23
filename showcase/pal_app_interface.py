import tkinter as tk
from palindrome_checker import PalindromeChecker

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label_1 = tk.Label(self, text='Enter a word, phrase or number to check if it\'s a palindrome: ', fg='#453F78',bg='#C0D6E8')
        self.label_1.pack()
        self.entry_0 = tk.Entry(self,bg='#DFF5FF')
        self.entry_0.pack()
        self.label_2 = tk.Label(self,fg='#453F78',bg='#C0D6E8')
        self.label_2.pack()
        self.btn = tk.Button(self,text='Enter',command=self.enter)
        self.btn.pack()

        self.bind('<Return>',self.enter) #Recognises enter key as equivalent to pressing the button

    def enter(self, event=None): #Added 'event' parameter (as suggested in assignment feedback) to handle output of the 'bind' call
        self.user_input = self.entry_0.get()
        checker = PalindromeChecker(self.entry_0.get())
        is_palindrome = checker.check_input()
        if not self.user_input: #Handles empty input
            self.label_2.config(fg='#A34343')
            self.label_2['text'] = f'Value entered cannot be empty.\nPlease enter a word, phrase or number and try again'
        elif is_palindrome:
            self.label_2.config(fg='#453F78')
            self.label_2['text'] = f'\'{self.user_input}\' is a palindrome!'
        else:
            self.label_2.config(fg='#453F78')
            self.label_2['text'] = f'\'{self.user_input}\' is not a palindrome'        
        
        self.entry_0.delete(0,tk.END) #Clears the entry box after the button is pressed

if __name__ == '__main__':
    root = Root()
    root['bg'] = '#C0D6E8'
    root.mainloop()


    
