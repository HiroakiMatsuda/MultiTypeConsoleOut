#!/usr/bin/env python
#coding:utf-8
# ver. 1.21117
# (C) 2012 Matsuda Hiroaki

import Tkinter as Tk
import ConfigParser as Conf
import ScrolledText as St

class TkController():
    
    def __init__(self):
        self.root = Tk.Tk()
        self.root.option_add('*font', ('Helvetica', 10))
        self.root.title('MutiTypeConsoleOut')

        self.tk_flag = 0

        icon_list = self.read_inifile('ini\consoleout.ini')
        self.set_img(icon_list)

        self.filename = Tk.StringVar()
        self.filename.set('input file name')
        ety_filename = Tk.Entry(self.root, textvariable = self.filename, width = 30)
        ety_filename.pack(side = Tk.LEFT)

        self.btn_write_data = Tk.Button(self.root, height = 24, image = self.img[0],
                                 bg = '#003366', command = lambda: self.logging_data())
        self.btn_write_data.pack(side = Tk.LEFT)
        
    def logging_data(self):
        if self.tk_flag == 0:
            self.tk_flag = 1
            self.btn_write_data.configure(bg = '#cc0033')
            self.set_comp_filename(self.filename.get()) 
            self.set_comp_flag(1)
            
            
        elif self.tk_flag == 1:
            self.tk_flag = 0
            self.btn_write_data.configure(bg = '#003366')
            self.set_comp_flag(0)
            

    def read_inifile(self, path):
        conf = Conf.SafeConfigParser()
        conf.read(path)

        icon_list = []
        icon_list.append(conf.get('ICON', 'write'))

        return icon_list

    def set_img(self, icon_list):
        self.img = []
        for i in range(len(icon_list)):
            self.img.append(Tk.PhotoImage(file = icon_list[i]))

    def set_icon(self, inifile):
        img = []
        for i in range(len(inifile[1])):
            img.append(Tk.PhotoImage(file = inifile[1][i][1]))
        return img
        
    def get_flag(self, func):
        self.set_comp_flag = func

    def get_filename(self, func):
        self.set_comp_filename = func

if __name__ == '__main__':
    import tkmtcocont
    tk = tkmtcocont.TkController()
    tk.root.mainloop()
