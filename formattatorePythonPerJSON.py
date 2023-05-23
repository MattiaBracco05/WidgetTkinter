import tkinter as tk

def replace_special_characters():
    input_string = input_text.get("1.0", tk.END)  
    modified_string = ""

    for char in input_string:
        if char == '\n':
            modified_string += '\\n'
        elif char == '\t':
            modified_string += '\\t'
        elif char == '"':
            modified_string += "'" 
        else:
            modified_string += char

    output_text.delete("1.0", tk.END)  
    output_text.insert(tk.END, modified_string)  


window = tk.Tk()
window.title("Sostituisci con i caratteri speciali")

input_label = tk.Label(window, text="Inserisci la tua stringa:")
input_label.pack()
input_text = tk.Text(window, height=4)
input_text.pack()

replace_button = tk.Button(window, text="Replace", command=replace_special_characters)
replace_button.pack()

output_label = tk.Label(window, text="Modified string:")
output_label.pack()
output_text = tk.Text(window, height=4)
output_text.pack()

window.mainloop()
