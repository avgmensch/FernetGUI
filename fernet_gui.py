import tkinter as tk
import tkinter.ttk as ttk


class FernetGUI:
    def __init__(self, window: tk.Tk | None = None) -> None:
        """Create a new FernetGUI-window."""

        # Setup window
        user_provided_window = window is not None
        self.tk = window if user_provided_window else tk.Tk()
        if not user_provided_window:
            self.tk.title("FernetGUI")
            self.tk.rowconfigure((0), weight=1)
            self.tk.columnconfigure((0), weight=1)

        # ROOT WIDGET
        self.root = ttk.Frame(self.tk)
        self.root.rowconfigure((0), weight=1)
        self.root.columnconfigure((0), weight=1)
        self.root.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

        # DECRYPTED CONTENT
        # Wrapper frame
        self.dec = ttk.Labelframe(self.root, text="Decrypted Content")
        self.dec.rowconfigure((1), weight=1)
        self.dec.columnconfigure((0), weight=1)
        self.dec.grid(row=0, column=0, sticky="nsew")
        # Wrapper for buttons
        self.dec_file = ttk.Frame(self.dec)
        self.dec_file.columnconfigure((3), weight=1)
        self.dec_file.grid(row=0, column=0, padx=3, sticky="ew")
        # Buttons and entry for path
        self.dec_file_copy = ttk.Button(self.dec_file, text="Copy Text")
        self.dec_file_copy.grid(row=0, column=0)
        self.dec_file_select = ttk.Button(self.dec_file, text="Select File")
        self.dec_file_select.grid(row=0, column=1)
        self.dec_file_load = ttk.Button(self.dec_file, text="Load File")
        self.dec_file_load.grid(row=0, column=2)
        self.dec_file_path = ttk.Entry(self.dec_file)
        self.dec_file_path.grid(row=0, column=3, sticky="ew")
        # Input / display for text
        self.dec_text = tk.Text(self.dec)
        self.dec_text.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

    def mainloop(self, n: int = 0) -> None:
        """
        Run the FernetGUI-application. Don't touch `n` if you aren't exactly
        sure on what you are doing.
        """
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = FernetGUI()
    app.mainloop()
