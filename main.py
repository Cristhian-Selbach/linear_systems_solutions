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
# --------------------------------------------------------------

# Functions -----------------------------------------------------
def increase():
  matrix_size.set(matrix_size.get() + 1)
  matrix_label.configure(text=(matrix_size.get()))


def decrease():
    matrix_size = matrix_size - 1


title_label = ctk.CTkLabel(window, text="Linear Systems Solutions", font=title_font)
title_label.pack(pady = 20)

matrix_size = ctk.IntVar(value=2)

matrix = []

matrix_label = ctk.CTkLabel(window, text="[2, 2]", font=title_font)
matrix_label.pack(pady = 20)

frame = ctk.CTkFrame(master=window, width=200, height=200)
frame.pack()
increase_button = Button(frame, text="+", width=30, command=increase)
decrease_button = Button(frame, text="-", width=30)
increase_button.pack(side="left")
decrease_button.pack(side="left")



window.mainloop()