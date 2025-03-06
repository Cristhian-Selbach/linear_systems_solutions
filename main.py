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
class std_button(ctk.CTkButton):
  def __init__(self, master, text, command=None):
    super().__init__(
      master, 
      text=text,
      fg_color="#D9D9D9",   
      hover_color="#8A8A8A", 
      text_color="#262626",
      corner_radius=0,
      border_width=0,
      command=command,
      font=text_font
    )
# ------------------------------------------------------------


title_label = ctk.CTkLabel(window, text="Linear Systems Solutions", font=title_font)
title_label.pack(pady = 20)

button = std_button(window, "Test button")
button.pack()



window.mainloop()