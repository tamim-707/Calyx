from tkinter import *
import threading
from GUI.GUI_brain import process_message
from Utils.helper import reply
from Utils.speech import speech_to_text
# ========= Calyx Forest Theme =========

BG = "#0F1F17"            # Main window
CHAT_BG = "#16281F"       # Chat area
BOTTOM_BG = "#1B2E23"     # Bottom/input area

USER_BG = "#2E7D32"       # User messages
BOT_BG = "#234D3C"        # Calyx messages

ENTRY_BG = "#203126"      # Input box
ENTRY_FG = "#EAF7EE"

BUTTON_BG = "#3FA34D"
BUTTON_ACTIVE = "#58C46B"
BUTTON_TEXT = "white"

TEXT = "#EAF7EE"
STATUS = "#9FC9A3"

SCROLL = "#3FA34D"

root = Tk()
root.title("Calyx")
root.geometry("600x600")
root.minsize(600, 400)
root.configure(bg=BG)
thinking_row = None

def send_message(event=None):
    if entry["state"] == DISABLED:
        return "break"

    message = entry.get().strip()

    if not message:
        return "break"

    add_message("You", message)
    status_label.config(text="🤖 Thinking...", fg="#E8D97A")

    entry.delete(0, END)

    entry.config(state=DISABLED)
    send_btn.config(state=DISABLED)
    mic_btn.config(state=DISABLED)

    add_message("Calyx", "Thinking...")

    threading.Thread(
        target=process_ai,
        args=(message,),
        daemon=True
    ).start()

    return "break"

def add_message(sender, message):

    global thinking_row

    row = Frame(messages_frame, bg=CHAT_BG)
    row.pack(fill=X, padx=15, pady=10)
    if sender == "You":

        # Make the first column take all extra space
        row.grid_columnconfigure(0, weight=1)

        bubble = Label(
            row,
            text=message,
            bg=USER_BG,
            fg="white",
            font=("Segoe UI", 11),
            wraplength=380,
            justify=LEFT,
            padx=18,
            pady=12
        )

        avatar = Label(
            row,
            text="👤",
            bg=CHAT_BG,
            fg=TEXT,
            font=("Segoe UI", 14)
        )

        bubble.grid(row=0, column=1, sticky="e")
        avatar.grid(row=0, column=2, padx=(8, 0), sticky="e")

    else:

        row.columnconfigure(2, weight=1)

        avatar = Label(
            row,
            text="🌿",
            bg=CHAT_BG,
            fg=TEXT,
            font=("Segoe UI",14)
        )
        avatar.grid(row=0, column=0, padx=(0,8))

        bubble = Label(
            row,
            text=message,
            bg=BOT_BG,
            fg="white",
            font=("Segoe UI",11),
            wraplength=380,
            justify=LEFT,
            padx=18,
            pady=12
        )
        bubble.grid(row=0, column=1, sticky="w")

        if message == "Thinking...":
            thinking_row = row


def replace_thinking(response):
    global thinking_row

    if thinking_row is not None:
        thinking_row.destroy()
        thinking_row = None

    add_message("Calyx", response)

def process_ai(message):
    response = process_message(message)

    reply(response)
    root.after(0,lambda: replace_thinking(response))
    root.after(0, enable_input)

def enable_input():
    entry.config(state=NORMAL)
    send_btn.config(state=NORMAL)
    mic_btn.config(state=NORMAL)
    status_label.config(text="✅ Ready",fg=STATUS)
    entry.focus()

def microphone():
    status_label.config(text="🎤 Listening...",fg="#7ED957")
    entry.config(state=DISABLED)
    send_btn.config(state=DISABLED)
    mic_btn.config(state=DISABLED)

    def listen():
        text = speech_to_text()

        def update():
            entry.config(state=NORMAL)
            send_btn.config(state=NORMAL)
            mic_btn.config(state=NORMAL)

            if text:
                entry.delete(0, END)
                entry.insert(0, text)
                send_message()

            entry.focus()

        root.after(0, update)

    threading.Thread(target=listen, daemon=True).start()

title = Label(
    root,
    text="🌿 Calyx",
    font=("Segoe UI",22,"bold"),
    bg=BG,
    fg="#58C46B"
)
title.pack(pady=(12,6))

# ==========================
# Chat Container
# ==========================

chat_container = Frame(root, bg=CHAT_BG)
chat_container.pack(
    fill=BOTH,
    expand=True,
    padx=12,
    pady=(12,6)
)

canvas = Canvas(
    chat_container,
    bg=CHAT_BG,
    highlightthickness=0,
    bd=0
)

scrollbar = Scrollbar(
    chat_container,
    orient="vertical",
    command=canvas.yview
)

messages_frame = Frame(
    canvas,
    bg=CHAT_BG
)

messages_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas_window = canvas.create_window(
    (0, 0),
    window=messages_frame,
    anchor="nw"
)
def resize_canvas(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", resize_canvas)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side=LEFT,
    fill=BOTH,
    expand=True
)

scrollbar.pack(
    side=RIGHT,
    fill=Y
)

#Status label
status_label = Label(
    root,
    text="Status: Ready",
    anchor="w",
    bg=BOTTOM_BG,
    fg=STATUS,
    font=("Segoe UI",10)
)
status_label.pack(fill=X,padx=8,pady=4)

# Bottom frame
bottom_frame = Frame(
    root,
    bg=BOTTOM_BG,
    height=60
)

bottom_frame.pack(
    side=BOTTOM,
    fill=X
)

bottom_frame.pack_propagate(False)



# Input box
entry = Entry(
    bottom_frame,
    font=("Segoe UI",11),
    bg=ENTRY_BG,
    fg=ENTRY_FG,
    insertbackground=ENTRY_FG,
    relief=FLAT,
    bd=0,
    highlightthickness=0
)

entry.pack(
    side=LEFT,
    fill=X,
    expand=True,
    padx=8,
    pady=8
)
# Press Enter to send
entry.bind("<Return>", send_message)

# Send button
send_btn = Button(
    bottom_frame,
    text="Send",
    width=8,
    command=send_message,
    bg=BUTTON_BG,
    fg=BUTTON_TEXT,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief=FLAT,
    bd=0,
    highlightthickness=0,
    cursor="hand2"
)

send_btn.pack(
    side=RIGHT,
    padx=8,
    pady=8
)

mic_btn = Button(
    bottom_frame,
    text="🎤",
    width=3,
    command=microphone,
    bg=BUTTON_BG,
    fg="white",
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief=FLAT,
    bd=0,
    highlightthickness=0,
    cursor="hand2"
)

mic_btn.pack(
    side=LEFT,
    padx=8,
    pady=8
)

def start_gui():
 entry.focus_set()
 root.mainloop()           