import customtkinter as ctk

# Project settings ---------------------------------------------
window = ctk.CTk()
window.title("Linear Systems Solutions")
window.geometry("900x450")
window.iconbitmap("assets/icon.ico")

title_font=ctk.CTkFont(family='Inter', size=28, weight="bold")
text_font=ctk.CTkFont(family='Inter', size=14, weight="bold")
# --------------------------------------------------------------

# Patterns -----------------------------------------------------
class Button(ctk.CTkButton):
  def __init__(self, master, text, width=140, command=None):
    super().__init__(
      master, 
      text=text,
      width=width,
      fg_color="#D9D9D9",   
      hover_color="#8A8A8A", 
      text_color="#262626",
      corner_radius=0,
      border_width=0,
      command=command,
      font=text_font,
    )

class Entry(ctk.CTkEntry):
  def __init__(self, master, placeholder_text_color = None, textvariable = None, placeholder_text = None):
   super().__init__(
            master,
            width=64,
            placeholder_text=placeholder_text,
            fg_color="#D9D9D9",  
            text_color="#262626",   
            border_width=0,
            corner_radius=0,
            font=text_font,
        )
# --------------------------------------------------------------

# Functions -----------------------------------------------------
def increase():
  matrix_size.set(matrix_size.get() + 1)


def decrease():
  matrix_size.set(matrix_size.get() - 1)
# --------------------------------------------------------------


title_label = ctk.CTkLabel(window, text="Linear Systems Solutions", font=title_font)
title_label.pack(pady = 20)

matrix_size = ctk.IntVar(value=2)
matrix = []


cells_frame = ctk.CTkFrame(master=window)
cells_frame.pack(pady=20)

variables_frame = ctk.CTkFrame(master=cells_frame)
variables_frame.pack()

x_var_label = ctk.CTkLabel(variables_frame, text="x", font=title_font)
y_var_label = ctk.CTkLabel(variables_frame, text="y", font=title_font)
z_var_label = ctk.CTkLabel(variables_frame, text="z", font=title_font)
x_var_label.pack(side="left", padx=20)
y_var_label.pack(side="left", padx=20)
z_var_label.pack(side="left", padx=20)


# Rendering Matrix Cells
for i in range(3**2):
  entry = Entry(cells_frame, placeholder_text=f"{i}")
  entry.pack()



# increase_button = Button(frame, text="+", width=30, command=increase)
# decrease_button = Button(frame, text="-", width=30)
# increase_button.pack(side="left")
# decrease_button.pack(side="left")



window.mainloop()