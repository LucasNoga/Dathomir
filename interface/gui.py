'''Gui interface'''


import logging
from pathlib import Path
from tkinter import *

import helper
from config.constants import BACKGROUND_COLOR

from .interface import Interface

from .window import FrameBottom, FrameTop

log = logging.getLogger('dathomir')


class Gui(Interface):
    '''Handle gui interface'''
    window: Tk

    def launch(self):
        '''Launch application in console or gui'''
        log.info("Start GUI")
        window = Tk()

        window.title("Dathomir")

        logo_path: Path = helper.get_assets_path(__file__) / "logo.ico"
        window.iconbitmap(logo_path)
        window.config(background=BACKGROUND_COLOR)  # Background interface

        self.center(window, 960, 680)  # place to the center
        window.minsize(width=500, height=500)  # Min Size

        self.window = window

        # Create several frames
        FrameTop.create(self)

        # self.set_frame_name(gui)
        # self.set_frame_type(gui)

        FrameBottom.create(self)

        self.window.mainloop()

    def set_frame_name(self, window):
        '''Set TextField to set a name'''
        frame = Frame(window)

        name_label = Label(frame, text='Username',
                           font=('calibre', 10, 'bold'))
        name_label.pack(side=LEFT, padx=5, pady=5)

        name_var = StringVar()
        name_entry = Entry(frame, textvariable=name_var,
                           font=('calibre', 10, 'normal'))
        name_entry.pack(side=LEFT, padx=5, pady=5)
        frame.grid(row=0, column=1, pady=10)

    def set_frame_type(self, window):
        '''set radio button to chose git server'''
        frame = Frame(window)
        lbl1 = Label(frame, text="SALUT", width=6)
        lbl1.pack(side=LEFT)

        radio_frame = Frame(frame)
        i = 'radios'  # Basically Links Any Radiobutton With The Variable=i.
        rb1 = Radiobutton(radio_frame, text="GitHub",
                          value=1, variable=i, command=self.show_servers)
        rb1.pack(side=LEFT)
        rb2 = Radiobutton(radio_frame, text="GitLab",
                          value=2, variable=i, command=self.show_servers)
        rb2.pack(side=LEFT)
        radio_frame.pack(side=LEFT)

        frame.grid(row=1, column=1)

    def set_frame_token(self, window):
        '''Set frame for token'''
        # TODO - create password field or Entry

    def set_frame_file_chooser(self, window):
        '''File chooser'''
        # TODO - faire un fileChooser pour choisir le folder de destination
        # TODO # https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/?ref=lbp

    def show_about(self):
        '''Show modal for Dathomir metadata'''
        print("SHOW MODAL ABOUT")
        # TODO

    def show_servers(self):
        '''Show servers available'''

    def select_server(self):
        '''Select a server'''

    def add_server(self):
        '''Add a new server'''

    def remove_server(self):
        '''Remove a server'''

    def center(self, window, width: int, height: int):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        window.update_idletasks()
        height = window.winfo_height()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x_axis = window.winfo_screenwidth() // 2 - win_width // 2
        y_axis = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry(f"{width}x{height}+{x_axis}+{y_axis}")
        window.deiconify()
