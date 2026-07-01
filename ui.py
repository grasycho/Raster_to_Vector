import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os
import core_processing

class LucideConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raster to Lucide SVG Converter")
        self.root.geometry("500x320")
        self.root.resizable(False, False)
        
        self.input_file_path = ""
        
        self.create_widgets()

    def create_widgets(self):
        # Main Layout Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # File Selection Section
        ttk.Label(main_frame, text="1. Select Input Image:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.file_entry = ttk.Entry(file_frame, width=40)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        browse_btn = ttk.Button(file_frame, text="Browse...", command=self.browse_file)
        browse_btn.pack(side=tk.RIGHT)

        # Model Info Alert
        info_lbl = ttk.Label(main_frame, text="Target Backend: Pure Mathematical Engine (Deterministic Tracing)", font=("Arial", 9, "italic"), foreground="gray")
        info_lbl.pack(anchor=tk.W, pady=(0, 20))

        # Action Button
        self.convert_btn = ttk.Button(main_frame, text="Generate Lucide Icon", command=self.start_conversion, style="Accent.TButton")
        self.convert_btn.pack(fill=tk.X, ipady=5, pady=(0, 15))

        # Progress / Status Section
        self.status_lbl = ttk.Label(main_frame, text="Status: Idle", font=("Arial", 9))
        self.status_lbl.pack(anchor=tk.W, pady=(0, 5))
        
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X)

    def browse_file(self):
        file_types = [("Image files", "*.png *.jpg *.jpeg *.bmp *.webp")]
        selected_file = filedialog.askopenfilename(title="Select Icon Image", filetypes=file_types)
        if selected_file:
            self.input_file_path = selected_file
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, selected_file)

    def start_conversion(self):
        if not self.input_file_path:
            messagebox.showwarning("Missing Input", "Please select an image file first.")
            return
        
        # Disable button and start progress animation
        self.convert_btn.config(state=tk.DISABLED)
        self.progress_bar.start(10)
        self.status_lbl.config(text="Status: Applying pure math (Ramer-Douglas-Peucker)...")

        # Run process in a separate thread so UI stays responsive
        thread = threading.Thread(target=self.run_pipeline)
        thread.start()

    def run_pipeline(self):
        try:
            # Step 1: Save Output Location
            output_file = filedialog.asksaveasfilename(
                defaultextension=".svg",
                filetypes=[("SVG files", "*.svg")],
                initialfile="lucide_custom.svg",
                title="Save Your Lucide Icon"
            )
            
            if output_file:
                # Step 2: Run the math pipeline directly
                core_processing.extract_and_generate_svg(self.input_file_path, output_file)
                self.root.after(0, lambda p=output_file: messagebox.showinfo("Success", f"Icon successfully saved to:\n{p}"))
            
        except Exception as e:
            error_message = str(e)
            self.root.after(0, lambda msg=error_message: messagebox.showerror("Pipeline Error", msg))
        
        finally:
            self.root.after(0, self.reset_ui)

    def reset_ui(self):
        self.convert_btn.config(state=tk.NORMAL)
        self.progress_bar.stop()
        self.status_lbl.config(text="Status: Idle")