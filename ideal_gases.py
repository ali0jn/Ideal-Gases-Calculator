from Tkinter import *
from PIL import ImageTk, Image
import os


class UI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.header = Label(self, text='Ideal Gases Calculator', font=('Helvetica', 18, 'bold'), bg='teal', fg='white', width=200, height=2)
        self.header.grid()
        self.frame_0 = Frame(self)
        self.frame_0.grid(row=1, column=0)
        self.note = Label(self.frame_0, text='Note: Please provide your values with respect to pre-defined units in below', font=('Helvetica', 13, 'bold'))
        self.note.grid(column=0, row=0, pady=5, padx=5)
        self.about_writer = Button(self.frame_0, text='About Application', font=('Helvetica', 13, 'bold'), command=self.display_about)
        self.about_writer.grid(column=1, row=0, padx=20, pady=5)
        self.frame_1 = Frame(self)
        self.frame_1.grid(row=2, column=0)
        self.solve_for = Label(self.frame_1, text='Select the unknown you want to solve for:', font=('Calibri', 12, 'bold'))
        self.solve_for.grid(padx=10)
        self.var = StringVar()
        self.var.set('E')
        self.pressure_cb = Checkbutton(self.frame_1, text='Pressure', variable=self.var, onvalue='Pressure', font=('Calibri', 12, 'bold'))
        self.pressure_cb.grid(row=0, column=1)
        self.volume_cb = Checkbutton(self.frame_1, text='Volume', variable=self.var, onvalue='Volume', font=('Calibri', 12, 'bold'))
        self.volume_cb.grid(row=0, column=2)
        self.mole_cb = Checkbutton(self.frame_1, text='Mole', variable=self.var, onvalue='Mole', font=('Calibri', 12, 'bold'))
        self.mole_cb.grid(row=0, column=3)
        self.temp_cb = Checkbutton(self.frame_1, text='Temprature', variable=self.var, onvalue='Temperature', font=('Calibri', 12, 'bold'))
        self.temp_cb.grid(row=0, column=4)
        self.leave = Label(self.frame_1, text='Please leave the entry for your unknown blank:', font=('Calibri', 12, 'bold'))
        self.leave.grid(column=0, row=1, pady=10)
        self.formula = Label(self.frame_1, text='PV=nRT', font=('Helvetica', 18, 'bold'))
        self.formula.grid(row=1, column=2)
        self.frame_2 = Frame(self)
        self.frame_2.grid()
        self.pressure_label = Label(self.frame_2, text='       Pressure (Pa):  ', font=('Calibri', 12, 'bold'))
        self.pressure_label.grid(column=0, row=0)
        self.volume_label = Label(self.frame_2, text='        Volume (m^3):  ', font=('Calibri', 12, 'bold'))
        self.volume_label.grid(column=0, row=1)
        self.mole_label = Label(self.frame_2, text='   Mole (mol):  ', font=('Calibri', 12, 'bold'))
        self.mole_label.grid(column=0, row=2)
        self.temp_label = Label(self.frame_2, text='            Temperature (K):  ', font=('Calibri', 12, 'bold'))
        self.temp_label.grid(column=0, row=3)
        self.pressure_entry = Entry(self.frame_2)
        self.pressure_entry.grid(column=1, row=0)
        self.volume_entry = Entry(self.frame_2)
        self.volume_entry.grid(column=1, row=1)
        self.mole_entry = Entry(self.frame_2)
        self.mole_entry.grid(column=1, row=2)
        self.temp_entry = Entry(self.frame_2)
        self.temp_entry.grid(column=1, row=3)
        self.calculate = Button(self.frame_2, text='Calculate', font=('Calibri', 12, 'bold'), command=self.make_calculation)
        self.calculate.grid(column=2, row=0, padx=100)
        self.clear = Button(self.frame_2, text='Clear Entries', font=('Calibri', 12, 'bold'), command=self.clear_entry)
        self.clear.grid(column=2, row=1)
        self.exit = Button(self.frame_2, text='Close', font=('Calibri', 12, 'bold'), command=self.master.destroy)
        self.exit.grid(column=2, row=2)
        self.answer = Label(self, text='Answer: ', font=('Helvetica', 20, 'bold'))
        self.answer.grid(pady=10)
        self.info_message = Label(self, text='Info message: all messages related to functionality of application will be displayed here')
        self.info_message.grid()
        self.columnconfigure(0, weight=1)
        self.grid()

    def clear_entry(self):
        self.pressure_entry.delete(0, END)
        self.mole_entry.delete(0, END)
        self.volume_entry.delete(0, END)
        self.temp_entry.delete(0, END)
        self.answer.configure(text='Answer: ')
        self.info_message.configure(text='Info message: entry fields have been cleared')

    def make_calculation(self):
        try:
            if self.var.get() == 'Pressure':
                volume = float(self.volume_entry.get())
                mole = float(self.mole_entry.get())
                temp = float(self.temp_entry.get())
                r = 8.3144598
                pressure = (mole*r*temp) / volume
                self.answer.configure(text='Answer: '+str(round(pressure, 3))+' pascal')
                self.info_message.configure(text='Info message: your pressure value has been calculated')
            elif self.var.get() == 'Volume':
                mole = float(self.mole_entry.get())
                temp = float(self.temp_entry.get())
                r = 8.3144598
                pressure = float(self.pressure_entry.get())
                volume = (mole*r*temp) / pressure
                self.answer.configure(text='Answer: ' + str(round(volume, 3)) + ' m^3')
                self.info_message.configure(text='Info message: your volume value has been calculated')
            elif self.var.get() == 'Mole':
                temp = float(self.temp_entry.get())
                r = 8.3144598
                pressure = float(self.pressure_entry.get())
                volume = float(self.volume_entry.get())
                mole = (pressure*volume) / (r*temp)
                self.answer.configure(text='Answer: ' + str(round(mole, 3)) + ' mol')
                self.info_message.configure(text='Info message: your mole value has been calculated')
            elif self.var.get() == 'Temperature':
                r = 8.3144598
                pressure = float(self.pressure_entry.get())
                volume = float(self.volume_entry.get())
                mole = float(self.mole_entry.get())
                temp = (pressure*volume) / (r*mole)
                self.answer.configure(text='Answer: ' + str(round(temp, 3)) + ' kelvin')
                self.info_message.configure(text='Info message: your temperature value has been calculated')
        except: pass

    def display_about(self):
        self.top = Toplevel(self.parent)
        self.top.resizable(False, False)
        self.top.geometry('440x290+500+200')
        self.top.title('About Product')
        img = Image.open(os.getcwd()+'\karahan.jpg')
        resized = img.resize((100, 133), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized)
        self.kaan_picture = Label(self.top, image=resized_image)
        self.kaan_picture.grid(row=0, column=0)
        self.kaan_name = Label(self.top, text='Dr. Kaan Karahan')
        self.kaan_name.grid(row=1, column=0, sticky=N)
        img_2 = Image.open(os.getcwd()+r'\ali.jpg')
        resized_2 = img_2.resize((100, 100), Image.ANTIALIAS)
        resized_image_2 = ImageTk.PhotoImage(resized_2)
        self.ali_picture = Label(self.top, image=resized_image_2)
        self.ali_picture.grid(row=2, column=0, sticky=N)
        self.ali_name = Label(self.top, text='Ali Reza Ibrahimzada')
        self.ali_name.grid(row=3, column=0, sticky=N)
        self.frame_info = Frame(self.top, borderwidth=2, relief=SUNKEN)
        self.frame_info.grid(row=0, column=1, rowspan=4, sticky=N+S+E+W)
        self.about = Label(self.frame_info, text='This software is prepared by Ali Reza Ibrahimzada, currently\n'
                                                 'studying Computer Engineering in Istanbul Sehir University.\n'
                                                 'Dr. Kaan Karahan is supervising this software as an essential\n'
                                                 'tool for Chemistry students as their Ideal Gases Calculator.\n'
                                                 'This version only supports SI units system, this software will\n'
                                                 'be updated frequently for better improvements. In near -  \n'
                                                 'future nice features like OCR, Image Recognition, etc... will\n'
                                                 'be added to this application.                                                     \n\n\n'
                                                 'For technical problems, please email:\n'
                                                 'aliibrahimzada@std.sehir.edu.tr')
        self.about.grid()
        self.top.mainloop()

def main():
    root = Tk()
    root.title('Ideal Gases Calculator')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.geometry('800x400')
    obj = UI(root)
    root.mainloop()


main()
