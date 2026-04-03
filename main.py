"""
main.py - Controller that integrates all modules.

This is the entry point and integration layer as specified in
Section 8.5 of the project manual. It launches the GUI which
internally connects to all backend modules.

Run with: python main.py
"""

from gui.app import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
