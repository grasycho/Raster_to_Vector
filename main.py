import tkinter as tk
from ui import LucideConverterApp

def main():
    root = tk.Tk()
    # Instantiate the application UI
    app = LucideConverterApp(root)
    # Start the Tkinter event listener loop
    root.mainloop()

if __name__ == "__main__":
    main()