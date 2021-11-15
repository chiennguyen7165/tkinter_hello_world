import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.tk.call("source", "C:\\Users\\dpn\\Dropbox\\Stem3\\Azure-ttk-theme\\azure.tcl")
root.tk.call("set_theme","dark")

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)

# Create value lists
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create contro variables
var_0 = tk.BooleanVar()
var_1 = tk.BooleanVar(value=True)
var_2 = tk.BooleanVar()
var_3 = tk.IntVar(value=2)
var_4 = tk.StringVar(value=option_menu_list[1])
var_5 = tk.DoubleVar(value=75.0)

# checkbuttonsFrame
check_frame = ttk.LabelFrame(root, text="Checkbuttons", padding=(20,10))
check_frame.grid(row=0, column=0, padx=(20,10), pady=(20,10), sticky="nsew")

check1 = ttk.Checkbutton(check_frame, text="Unchecked", variable=var_0)
check1.grid(row = 0, column= 0, padx = 5, pady = 10, sticky="nsew")

check2 = ttk.Checkbutton(check_frame, text="Checked", variable = var_1)
check2.grid(row = 1, column= 0, padx = 5, pady = 10, sticky="nsew")

check3 = ttk.Checkbutton(check_frame, text="Thrid state", variable = var_2)
check3.state(["alternate"])
check3.grid(row = 2, column= 0, padx = 5, pady = 10, sticky="nsew")

check4 = ttk.Checkbutton(check_frame, text="Disable", state = "disabled")
check4.state(["disabled !alternate"])
check4.grid(row = 3, column= 0, padx = 5, pady = 10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20,10), pady=10, sticky="ew")

# radiobuttonsFrame
radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20,10))
radio_frame.grid(row = 2, column=0, padx=(20,10), pady=10, sticky="nsew")

radio_1 = ttk.Radiobutton(radio_frame, text="Unselected", variable = var_3, value=1)
radio_1.grid(row=0, column=0, padx=5,pady=10, sticky="nsew")

radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable = var_3, value=2)
radio_2.grid(row=1, column=0, padx=5,pady=10, sticky="nsew")

radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
radio_4.grid(row=2, column=0, padx=5,pady=10, sticky="nsew")


# Create a Frame for input wodgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row = 0, column=1, padx=10, pady=(30,10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Entry")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# Spinbox
spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100, increment=0.1)
spinbox.insert(0, "Spinbox")
spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Combobox
combobox = ttk.Combobox(widgets_frame, values=combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

# Read-only combobox
readonly_combo = ttk.Combobox(widgets_frame, state="readonly", values=readonly_combo_list)
readonly_combo.current(0)
readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

# Menu for the Menubutton
menu = tk.Menu(root)
menu.add_command(label="Menu item 1")
menu.add_command(label="Menu item 2")
menu.add_separator()
menu.add_command(label="Menu item 3")
menu.add_command(label="Menu item 4")

menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="ew")

# Optionmenu
optionmenu = ttk.OptionMenu(widgets_frame, var_4, *option_menu_list)
optionmenu.grid(row=5, column=0,padx=5, pady=10, sticky="ew")

# Button
button = ttk.Button(widgets_frame, text="Button")
button.grid(row = 6, column=0,padx=5, pady=10, sticky="ew")

# Accent_Button
accent_button = ttk.Button(widgets_frame, text="Accent button", style="Accent.TButton")
accent_button.grid(row = 7, column=0,padx=5, pady=10, sticky="ew")

# Toggle_Button
toggle_button = ttk.Button(widgets_frame, text="Toggle button",style="Toggle.TButton")
toggle_button.grid(row = 8, column=0,padx=5, pady=10, sticky="ew")

# Switch
swtich = ttk.Checkbutton(widgets_frame, text="Switch", style="Switch.TCheckbutton")
swtich.grid(row = 9, column=0,padx=5, pady=10, sticky="ew")


# Create Panewindow include 2 frame
pannedwindow = ttk.Panedwindow(root, orient="vertical")
pannedwindow.grid(row=0, column=2, padx=(25,5), sticky="nsew")

# Treeview frame is treeview
columns= ('column1', 'column2', 'column3')
treeview = ttk.Treeview(pannedwindow, columns=columns, show="headings")
pannedwindow.add(treeview)

# define headings
treeview.heading('column1', text='Column 1')
treeview.heading('column2', text='Column 2')
treeview.heading('column3', text='Column 3')

# generate sample data
datas = []
for n in range(1, 100):
    datas.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for data in datas:
    treeview.insert("", index="end", values=data)
    
treeview.grid(row=0,column=0, sticky="ew")

# Notebook
notebook = ttk.Notebook(pannedwindow)
pannedwindow.add(notebook)
# Tab1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index = 0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0,weight=1)
tab_1.rowconfigure(index=1,weight=1)
notebook.add(tab_1, text="Tab 1")

# Scale
scale = ttk.Scale(tab_1, from_=100, to=0, variable = var_5)
scale.grid(row = 0, column=0,padx=(20, 10), pady=20, sticky="ew")

# Progressbar
progress = ttk.Progressbar(tab_1, value=0, variable=var_5, mode="determinate")
progress.grid(row=0, column=1, padx=(20, 10), pady=20, sticky="ew")

# Label
label = ttk.Label(tab_1, text="Made be Chien Nguyen", font="Arial")
label.grid(row=1, column=0, columnspan=2)

# Tab2
tab_2 =ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Tab3
tab_3 =ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

notebook.grid(row=1,column=0,padx=5, pady=25, sticky="ew")

root.mainloop()