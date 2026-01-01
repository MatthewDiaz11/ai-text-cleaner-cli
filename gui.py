import tkinter as tk

def toggle_gui(frame):
    if frame.winfo_ismapped():  
        frame.pack_forget()
    else:   
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
root = tk.Tk()
root.title("Productivity Application")
root.geometry("800x800")

## -- AI text cleaner section -- ##

# - Create frame
text_cleaner_frame = tk.Frame(root, bg="lightblue", borderwidth=2, relief="groove")
text_cleaner_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# - Label 
text_cleaner_label = tk.Label(text_cleaner_frame, text="AI Text Cleaner", bg="lightblue")
text_cleaner_label.pack(pady=50)



## -- File Organizer Section -- ##

# Create frame
file_organizer_frame = tk.Frame(root, bg="lightgreen", borderwidth=2, relief="groove")
file_organizer_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label_right = tk.Label(file_organizer_frame, text="File Organizer", bg="lightgreen")
label_right.pack(pady=50)

button_right = tk.Button(file_organizer_frame, text="Button in Right Frame", command=lambda: toggle_gui(text_cleaner_frame))
button_right.pack()



root.mainloop()