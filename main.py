import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Project settings ---------------------------------------------
window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.title("Linear Systems Solutions")
window.geometry("900x500")
window.iconbitmap("assets/icon.ico")

title_font=ctk.CTkFont(family='Inter', size=28, weight="bold")
caption_font=ctk.CTkFont(family='Inter', size=18, weight="bold")
text_font=ctk.CTkFont(family='Inter', size=14, weight="bold")
# --------------------------------------------------------------

# Patterns -----------------------------------------------------
class Button(ctk.CTkButton):
  def __init__(self, master, text, width=140, command=None, fg_color="#D9D9D9"):
    super().__init__(
      master, 
      text=text,
      width=width,
      fg_color=fg_color,   
      hover_color="#8A8A8A", 
      text_color="#262626",
      corner_radius=0,
      border_width=0,
      command=command,
      font=text_font,
    )

class Entry(ctk.CTkEntry):
  def __init__(self, master, textvariable = None, placeholder_text = None):
   super().__init__(
            master,
            width=64,
            textvariable=textvariable,
            placeholder_text=placeholder_text,
            fg_color="#D9D9D9",  
            text_color="#262626",   
            border_width=0,
            corner_radius=0,
            font=text_font,
        )

# --------------------------------------------------------------
def increase():
  matrix_size.set(matrix_size.get() + 1)
  render_matrix_cells()

def decrease():
  if matrix_size.get() > 2:
    matrix_size.set(matrix_size.get() - 1)
    render_matrix_cells()

current_theme = ctk.get_appearance_mode()

title_label = ctk.CTkLabel(window, text="Linear Systems Solutions", font=title_font)
title_label.pack(pady = 20)

def change_theme():
  global current_theme, theme_image
    
  if current_theme == "Dark":
    ctk.set_appearance_mode("light")
    current_theme = "Light"
    new_image = Image.open("assets/images/dark_mode.png")
    theme_mode_button.configure(hover_color="#BCBCBC")

  else:
    ctk.set_appearance_mode("dark")
    current_theme = "Dark"
    new_image = Image.open("assets/images/light_mode.png")
    theme_mode_button.configure(hover_color="#1A1A1A")

  theme_image = ctk.CTkImage(new_image, size=(25, 25))
  theme_mode_button.configure(image=theme_image)


theme_image = Image.open("assets/images/light_mode.png")
button_image = ctk.CTkImage(light_image=theme_image, size=(25, 25))

theme_mode_button = ctk.CTkButton(window, text="", image=button_image, width=25, hover_color="#1A1A1A", fg_color="transparent", command=change_theme)
theme_mode_button.place(x=800, y=25)


matrix_size = ctk.IntVar(value=2)
matrix_entries = []
matrix = []

matrix_frame = ctk.CTkFrame(master=window)
matrix_frame.pack(pady=20)

cells_frame = None

def render_matrix_cells():
  global cells_frame, matrix_entries

  if cells_frame:
    cells_frame.destroy()

  cells_frame = ctk.CTkFrame(master=matrix_frame)
  cells_frame.pack()

  matrix_entries.clear()

  for i in range(matrix_size.get()):
    row_frame = ctk.CTkFrame(cells_frame, fg_color="transparent")  
    row_frame.pack(pady=5)
    row_entries = []

    for j in range(matrix_size.get() + 1):
      placeholder = f"x{j+1}" if j < matrix_size.get() else ""

      entry = Entry(row_frame, placeholder_text=placeholder)
      entry.pack(side="left", padx=5)
      row_entries.append(entry)

      if j < matrix_size.get() - 1:
        plus_label = ctk.CTkLabel(row_frame, text="+", font=text_font)
        plus_label.pack(side="left", padx=5)

      if j == matrix_size.get() - 1:
        equals_label = ctk.CTkLabel(row_frame, text="=", font=text_font)
        equals_label.pack(side="left", padx=5)

    matrix_entries.append(row_entries)

render_matrix_cells()

def allocate_matrix_size():
  global matrix
  size = matrix_size.get()

  while len(matrix) < size:
    matrix.append([0] * (size + 1))  
  for i in range(size):
    while len(matrix[i]) < size + 1:
       matrix[i].append(0) 

def get_matrix_values():
  allocate_matrix_size()

  for i in range(matrix_size.get()):
    for j in range(matrix_size.get() + 1):

      try:
        value = float(matrix_entries[i][j].get())  
        matrix[i][j] = value
        print(f"[{i}][{j}] = {matrix[i][j]}")

      except ValueError:
        messagebox.showerror("Input Error", f"The value at position [{i+1}][{j+1}] is not a valid number.")
        print(f"[{i}][{j}] = Invalid")

def render_options():
  options_frame = ctk.CTkFrame(window, fg_color="transparent")
  options_frame.pack(pady=20)

  cells_label = ctk.CTkLabel(options_frame, text="Cells: ", font=caption_font)
  cells_label.pack(side="left", padx=5)

  increase_button = Button(options_frame, text="+", width=40, command=increase)
  increase_button.pack(side="left", padx=5)

  decrease_button = Button(options_frame, text="-", width=40, command=decrease)
  decrease_button.pack(side="left", padx=5)

  bar_frame_1 = ctk.CTkFrame(options_frame, width=3, height=30, fg_color="#D9D9D9")
  bar_frame_1.pack(side="left", padx=8)

  option_menu = ctk.CTkOptionMenu(
      options_frame, 
      values=["Gaussian Elimination", "Cramer's Rule", "LU Decomposition"],  # Opções do menu
      fg_color="#D9D9D9",  
      button_color="#8A8A8A", 
      button_hover_color="#686868",  
      text_color="#262626", 
      corner_radius=0,  
      font=text_font,
      dropdown_font=text_font
  )
  option_menu.pack(side="left", padx=5)

  bar_frame_2 = ctk.CTkFrame(options_frame, width=3, height=30, fg_color="#D9D9D9")
  bar_frame_2.pack(side="left", padx=8)

  example_button = Button(options_frame, text="Example", width=90)
  example_button.pack(side="left", padx=5)

  bar_frame_3 = ctk.CTkFrame(options_frame, width=3, height=30, fg_color="#D9D9D9")
  bar_frame_3.pack(side="left", padx=8)

  solve_button = Button(options_frame, text="Solve", width=80, fg_color="#F46F6F", command=get_matrix_values)
  solve_button.pack(side="left", padx=5)

render_options()

window.mainloop()