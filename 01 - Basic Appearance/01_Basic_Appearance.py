import Tkinter as tk
try:
    import AppKit
except ImportError, e:
    AppKit = None


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Hello World")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')  # '#ececec' is the standard gray background of El Capitain

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        tk.Label(self, text="This is your first GUI. (highfive)").pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    if AppKit is not None:
        AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

"""
When launched the GUI is placed behind our active application window, has a white background and can be re-sized by
the user. The two lines added below the title modify the GUI's configuration to prevent resizing of the window and set
the background color to match the default for macOS.

Our GUI will also load with a default menubar selection much like any other standard macOS application. This can be
suppressed by creating an instance of Tkinter.Menu without any items and then adding it to our GUI's root configuration.

The subprocess call to 'osascript' is a solution to bringing the dialog window to the front and being the active window
for the user. It comes after the 'app' has been instantiated but before the 'mainloop' is called. While there is a way
to make the window come to the front as a part of Tkinter, that built-in method does not make the window active:

    ...
    self.master.call('wm', 'attributes', '.', '-topmost', True)
    ...

This can also be achieved by leveraging NSAppleScript opposed to relying upon subprocess:

    from Foundation import NSAppleScript
    ...
    applescript = 'tell app "Finder" to set frontmost of process "Python" to true'
    NSAppleScript.alloc().initWithSource_(applescript).executeAndReturnError_(None)
    ...
"""
