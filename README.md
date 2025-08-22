# Windows 11 Context Menu Switcher
A simple Python GUI tool that lets you toggle between the **classic Windows 10-style context menu** and the default **Windows 11 context menu**. The app includes a **Windows icon (`windows.ico`)** so the executable and GUI window both look polished and consistent with Windows.

## ✨ Features
- 🖱️ Enable the classic Windows 10 right-click menu in Windows 11.  
- 🔄 Restore the default Windows 11 context menu at any time.  
- ⚡ Built-in PowerShell execution with real-time output logging.  
- 🛡️ Auto-elevates with Administrator privileges when required.  
- 🎨 Modern Tkinter-based GUI with dark theme.  
- Uses `windows.ico` for both the **EXE file icon** and the **GUI window icon**.

## 📸 Screenshot
<img width="448" height="326" alt="{C09CBFE9-43DD-42BD-B0B0-A1E893441A62}" src="https://github.com/user-attachments/assets/7674aaca-8584-4e15-a252-38235d7866fc" />

## 🚀 Usage
1. Make sure you have **Python 3.x** installed.  
2. Place the following files together in the same folder (e.g., on your Desktop):  
   - `classicmenu.py` (the script)  
   - `windows.ico` (the icon)  
3. Run the script:  
   ```bash
   python classicmenu.py
   
## 📦 Building into an EXE
To create a standalone EXE with the icon embedded:<br>
```bash
pyinstaller --onefile --noconsole --icon=windows.ico --add-data "windows.ico;." classicmenu.py <br>
--icon=windows.ico → sets the EXE’s file icon (desktop/Explorer). <br>
--add-data "windows.ico;." → bundles the icon so the Tkinter window also uses it at runtime. <br>
The resulting EXE will not require Python to be installed.

## ⚠️ Notes

This tool modifies the Windows Registry to apply changes.  
Admin rights are required — the app will prompt and auto-relaunch with elevated privileges.  
File Explorer will be restarted when applying changes.  
Changes are safe and fully reversible.  

## 🖥️ Requirements

Windows 11  
Python 3.x  
Administrator access

Python Standard Libraries Used
tkinter (GUI)  
subprocess (run PowerShell)  
ctypes (admin check)  
sys, os (path + process handling)  
(No external packages required.)  
