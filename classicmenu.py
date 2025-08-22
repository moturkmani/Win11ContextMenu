import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import ctypes
import sys
import os

# Check if running as admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Run PowerShell command and show output
def run_powershell(cmd):
    try:
        completed = subprocess.run(
            ["powershell", "-Command", cmd], capture_output=True, text=True
        )
        output_text.insert(
            tk.END,
            f"> {cmd}\n{completed.stdout}\n{completed.stderr}\n{'-'*50}\n"
        )
        output_text.see(tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def enable_classic_menu():
    cmd = r'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /ve /f; Stop-Process -Name explorer -Force'
    run_powershell(cmd)

def restore_win11_menu():
    cmd = r'reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f; Stop-Process -Name explorer -Force'
    run_powershell(cmd)

# Relaunch as admin if not already
if not is_admin():
    messagebox.showinfo("Admin Required", "Restarting with Administrator privileges...")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

# GUI Setup
root = tk.Tk()
root.title("Windows 11 Context Menu Switcher")

# Handle PyInstaller bundle path
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Set custom icon (embedded in exe)
icon_path = resource_path("windows.ico")
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Icon not set: {e}")

# Center window on screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int((screen_height / 2) - (window_height / 2))
position_right = int((screen_width / 2) - (window_width / 2))
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Dark theme background
root.configure(bg="black")

# Admin status
admin_label = tk.Label(
    root, text="Admin Mode Enabled ✔", fg="green", bg="black", font=("Arial", 12, "bold")
)
admin_label.pack(pady=10)

# Buttons with flat/modern look
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

button_style = {
    "relief": "flat",
    "bd": 0,
    "font": ("Segoe UI", 11, "bold"),
    "activeforeground": "white"
}

enable_btn = tk.Button(
    frame, text="Enable Classic Menu", command=enable_classic_menu, width=25,
    bg="#1e90ff", fg="white", activebackground="#4682b4", **button_style
)
enable_btn.grid(row=0, column=0, padx=10)

restore_btn = tk.Button(
    frame, text="Restore Windows 11 Menu", command=restore_win11_menu, width=25,
    bg="#32cd32", fg="white", activebackground="#228b22", **button_style
)
restore_btn.grid(row=0, column=1, padx=10)

# Output box styled like PowerShell
output_text = scrolledtext.ScrolledText(
    root, width=70, height=15, bg="#012456", fg="white", insertbackground="white",
    font=("Consolas", 10), relief="flat", bd=0
)
output_text.pack(pady=10)

root.mainloop()
