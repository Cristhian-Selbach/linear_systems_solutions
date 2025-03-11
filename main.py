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

# -------------------------------------------------------
def increase():
  matrix_size.set(matrix_size.get() + 1)


def decrease():
  matrix_size.set(matrix_size.get() - 1)


# --------------------------------------------------------------

title_label = ctk.CTkLabel(window, text="Linear Systems Solutions", font=title_font)
title_label.pack(pady = 20)

cells_frame = ctk.CTkFrame(master=window)
cells_frame.pack(pady=20)

matrix_size = ctk.IntVar(value=2)
matrix = []
entries = []

# Allocating Matrix Size
for i in range(matrix_size.get()):
  line = []
  for j in range(matrix_size.get() + 1):
    line.append(0)
  matrix.append(line)


# Rendering Matrix Cells
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

  entries.append(row_entries)

def get_matrix_values():
  for i in range(matrix_size.get()):
    for j in range(matrix_size.get() + 1):
      value = entries[i][j].get()  
      matrix[i][j] = float(value)
      print(f"[{i}][{j}] = {matrix[i][j]}")

get_values_button = Button(window, text="values", command=get_matrix_values)
get_values_button.pack(pady=10)



# increase_button = Button(frame, text="+", width=30, command=increase)
# decrease_button = Button(frame, text="-", width=30)
# increase_button.pack(side="left")
# decrease_button.pack(side="left")



window.mainloop()