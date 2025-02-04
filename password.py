import tkinter as tk
import random
import string


def generate_password():
    length = int(length_entry.get())
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

   
    char_set = letters
    if use_numbers:
        char_set += numbers
    if use_symbols:
        char_set += symbols

   
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    
    result_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Password Generator")


tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)


numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


result_label = tk.Label(root, text="Generated Password: ")
result_label.pack(pady=10)


root.mainloop()
