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
            self.tk.geometry("600x300")
            self.tk.minsize(600, 300)

        # ROOT WIDGET
        self.root = ttk.Frame(self.tk)
        self.root.rowconfigure((0), weight=1)
        self.root.columnconfigure((0, 2), weight=1)
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

        # VERTICAL CONTENT SPACER
        self.spacer_vertical = ttk.Frame(self.root)
        self.spacer_vertical.grid(row=0, column=1, padx=3)

        # ENCRYPTED CONTENT
        # Wrapper frame
        self.enc = ttk.Labelframe(self.root, text="Encrypted Content")
        self.enc.rowconfigure((1), weight=1)
        self.enc.columnconfigure((0), weight=1)
        self.enc.grid(row=0, column=2, sticky="nsew")
        # Wrapper for buttons
        self.enc_file = ttk.Frame(self.enc)
        self.enc_file.columnconfigure((3), weight=1)
        self.enc_file.grid(row=0, column=0, padx=3, sticky="ew")
        # Buttons and entry for path
        self.enc_file_copy = ttk.Button(self.enc_file, text="Copy text")
        self.enc_file_copy.grid(row=0, column=0)
        self.enc_file_select = ttk.Button(self.enc_file, text="Select File")
        self.enc_file_select.grid(row=0, column=1)
        self.enc_file_load = ttk.Button(self.enc_file, text="Load File")
        self.enc_file_load.grid(row=0, column=2)
        self.enc_file_path = ttk.Entry(self.enc_file)
        self.enc_file_path.grid(row=0, column=3, sticky="ew")
        # Input / display for text
        self.dec_text = tk.Text(self.enc)
        self.dec_text.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

        # HORIZONTAL CONTENT SPACER
        self.spacer_horizontal = ttk.Frame(self.root)
        self.spacer_horizontal.grid(row=1, column=0, columnspan=3, pady=3)

        # PASSWORD SETTINGS
        # Wrapper frame
        self.set = ttk.Labelframe(self.root, text="Password Settings")
        self.set.columnconfigure((0), weight=1)
        self.set.grid(row=2, column=0, columnspan=3, sticky="ew")
        # Password and encrypt / decrypt
        self.set_passwd = ttk.Frame(self.set)
        self.set_passwd.columnconfigure((2), weight=1)
        self.set_passwd.grid(row=0, column=0, padx=3, sticky="ew")
        self.set_passwd_enc = ttk.Button(self.set_passwd, text="Encrypt")
        self.set_passwd_enc.grid(row=0, column=0)
        self.set_passwd_dec = ttk.Button(self.set_passwd, text="Decrypt")
        self.set_passwd_dec.grid(row=0, column=1)
        self.set_passwd_entry = ttk.Entry(self.set_passwd)
        self.set_passwd_entry.grid(row=0, column=2, sticky="ew")
        # Salt and pepper
        self.set_sec = ttk.Frame(self.set)
        self.set_sec.columnconfigure((3), weight=1)
        self.set_sec.grid(row=1, column=0, padx=3, pady=3, sticky="ew")
        self.set_sec_pepper = ttk.Button(self.set_sec, text="Pepper: Off")
        self.set_sec_pepper.grid(row=1, column=0)
        self.set_sec_select_salt = ttk.Button(self.set_sec, text="Select Salt")
        self.set_sec_select_salt.grid(row=1, column=1)
        self.set_sec_load_salt = ttk.Button(self.set_sec, text="Load Salt")
        self.set_sec_load_salt.grid(row=1, column=2)
        self.set_sec_path_salt = ttk.Entry(self.set_sec)
        self.set_sec_path_salt.grid(row=1, column=3, sticky="ew")

    def mainloop(self, n: int = 0) -> None:
        """
        Run the FernetGUI-application. Don't touch `n` if you aren't exactly
        sure on what you are doing.
        """
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = FernetGUI()
    app.mainloop()
