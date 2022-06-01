# Lables
visible_text = tk.Label(text='Text', font=('Arial', 24, 'bold'))
visible_text.pack()

# user input - Entry
input = tk.Entry(width=30)
input.insert(index=1, string='Write your text here')
input.pack()

# click button - Button
button = tk.Button(text='Click here', command=changing_text)
button.pack()

# Text box
text_box = tk.Text(height=5, width=30)
text_box.focus() #Allow on show cursor in the box
text_box.insert(END, string='Text')
print(text_box.get('1.0', index2=2))
text_box.pack()

#  Spinbox
def spinbox_used():
    print(spinbox_used.get())

spinbox = tk.Spinbox(from=0, to=10, width=5, command=spinbox_used())

spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = tk.Scale(from=0, to=10, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(checked_state.get())

    # Check if the box is ticked, if yes = 1, no = 0
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text='If Yes', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton

def radio_used():
    print(radio_state.get())

    radio_state = tk.IntVar()
    radiobutton_1 = tk.Radiobutton(text='Opcja 1', value=1, variable=radio_state, command=radio_used)
    radiobutton_2 = tk.Radiobutton(text='Opcja 2', value=2, variable=radio_state, command=radio_used)
    radiobutton_1.pack()
    radiobutton_2.pack()

# Listbox

def list_box(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(heigh=4)
fruits = ['Apple', 'Banana', 'Pear', 'Orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
