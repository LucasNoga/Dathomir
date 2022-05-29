'''Tk module'''

from tkinter import BOTTOM, LEFT, SUNKEN, Button, Frame

from config.constants import BACKGROUND_COLOR


class FrameBottom:
    '''Frame for bottom window of Dathomir'''

    @classmethod
    def click_about(cls):
        '''click on about button'''
        # TODO faire un bouton a propos qui ouvre un modal
        # avec la version / description / lien guithhub voir rpcs.exe
        cls.gui.show_about()

    @classmethod
    def click_add_config(cls):
        '''click on add config button'''
        cls.gui.click_add_config()

    @classmethod
    def click_create_backup(cls):
        '''click on create backup button'''
        cls.gui.create_backup()

    @classmethod
    def create(cls, gui):
        '''Setup title for window'''
        cls.gui = gui
        frame: Frame = Frame(gui.window,
                             background=BACKGROUND_COLOR,
                             border=1,
                             relief=SUNKEN
                             )
        button_about: Button = Button(frame,
                                      text="About",
                                      font=("Arial", 16),
                                      background=BACKGROUND_COLOR,
                                      foreground='white',
                                      border=1,
                                      relief=SUNKEN,
                                      command=cls.click_about
                                      )
        button_add_config: Button = Button(frame,
                                           text="Add config",
                                           font=("Arial", 16),
                                           background=BACKGROUND_COLOR,
                                           foreground='white',
                                           border=1,
                                           relief=SUNKEN,
                                           command=cls.click_add_config
                                           )
        button_create_backup: Button = Button(frame,
                                              text="Create backup",
                                              font=("Arial", 16),
                                              background=BACKGROUND_COLOR,
                                              foreground='white',
                                              border=1,
                                              relief=SUNKEN,
                                              command=cls.click_create_backup
                                              )
        button_about.pack(side=LEFT, padx=50)
        button_add_config.pack(side=LEFT, padx=50)
        button_create_backup.pack(side=LEFT, padx=50)
        frame.pack(side=BOTTOM, pady=15)

        # TODO - faire un bouton "show repo" pour afficher la list des repo
        # close_button = Button(gui, text="Close", command=gui.quit)
        # close_button.pack(side=RIGHT, padx=1, pady=1)
