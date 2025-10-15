import tkinter as tk
from tkinter import ttk
from ai_handler import *

##Variables for font and size for later adaptaion to allow users to choose style and size
fontStyle = "Segoe UI"
size = 11

def startWindow():
    root = tk.Tk()
    
    ##window Set Up
    root.title("Fun Editor")
    root.state('zoomed')

    mainframe = ttk.PanedWindow(root, orient="horizontal")
    mainframe.pack(fill="both", expand=True)


    ##defining style for window
    style = ttk.Style()

    if "vista" in style.theme_names():
        style.theme_use("vista")
    elif "aqua" in style.theme_names():
        style.theme_use("aqua")
    else:
        style.theme_use("clam")

    style.configure("Vertical.TScrollbar",
                    troughcolor="#abaeaf",
                    background="#e1efe8",
                    arrowcolor="#222222",
                    width=7,
                    gripcount = 0)


    ##sets up frame for text with scrollbar and text box
    text_frame = ttk.Frame(mainframe, padding=5)
    mainframe.add(text_frame)

    scrollbar = ttk.Scrollbar(text_frame, style ="Vertical.TScrollbar")
    scrollbar.pack(side="right", fill="y")

    text_box = tk.Text(
        text_frame,
        wrap='word',
        undo=True,
        bg=style.lookup("TFrame", "background"),
        fg="#222",
        font=(fontStyle, size),
        relief="flat",
        yscrollcommand=scrollbar.set)
    text_box.pack(fill="both", expand=True)
    scrollbar.config(command=text_box.yview)

    text_box.bind(".", lambda event: on_period_pressed())


    #takes the last wrtieen sentence and translates it with ChatGPT
    def on_period_pressed():
        full_text = text_box.get("1.0", "end-1c")

        cursor_index = text_box.index("insert")
        cursor_pos = int(text_box.count("1.0", cursor_index)[0])

        prev_dot = full_text.rfind(".", 0, cursor_pos-1)
        start_index = prev_dot + 1 if prev_dot != -1 else 0

        sentence = full_text[start_index:cursor_pos]

        translated = string_translation(sentence.strip(), "Middle English(14th Century) Chaucer-Style")

        start_idx = f"1.0 + {start_index} chars"
        end_idx = f"1.0 + {cursor_pos} chars"

        text_box.delete(start_idx, end_idx)
        text_box.insert(start_idx, translated)

        text_box.mark_set("insert", f"{start_idx} + {len(translated)} chars")

    root.mainloop()


