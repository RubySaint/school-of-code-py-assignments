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

    def enter(self):
        self.user_input = self.entry_0.get()
        if PalindromeChecker.check_input(self) == None:
            self.label_2.config(fg='#A34343')
            self.label_2['text'] = f'Value entered cannot be empty.\nPlease enter a word, phrase or number and try again'
        elif PalindromeChecker.check_input(self):
            self.label_2.config(fg='#453F78')
            self.label_2['text'] = f'\'{self.user_input}\' is a palindrome!'
        else:
            self.label_2.config(fg='#453F78')
            self.label_2['text'] = f'\'{self.user_input}\' is not a palindrome'

if __name__ == '__main__':
    root = Root()
    root['bg'] = '#C0D6E8'
    root.mainloop()


    
