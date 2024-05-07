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

    def mainloop(self, n: int = 0) -> None:
        """
        Run the FernetGUI-application. Don't touch `n` if you aren't exactly
        sure on what you are doing.
        """
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = FernetGUI()
    app.mainloop()
