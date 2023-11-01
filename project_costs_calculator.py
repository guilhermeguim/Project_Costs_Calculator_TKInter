from tkinter import *
from tkinter import ttk


window = Tk()

class Application():
    def __init__(self):
        self.__background_color = '#e0e5ec'
        self.window = window
        self.tela()
        self.screen_frames()
        window.mainloop()
        
    def tela(self):
        self.window.title("PROJECT COSTS CALCULATOR")
        self.window.configure(background=self.__background_color)
        self.window.geometry('620x100')
        self.window.resizable(True,True)
        
    def screen_frames(self):
        lbl_sizex = 0.225
        lbl_sizey = 0.21
        y_step = 0.25
        
        x_start = 0.02
        y_start = 0.02
        
        result_y = 0.35
        result_x = 1 - lbl_sizex - (3*x_start)
        
        def start_posx(n):
            value = x_start+((lbl_sizex+x_start)*n)
            return value
        
        def start_posy(n):
            value = y_start+((lbl_sizey+y_start+y_step)*n)+y_step
            value2 = value - y_step
            return [value2, value]
        
        self.texto1 = Label(text="Unitary Value:",font=("Arial", 10),background=self.__background_color)
        self.texto1.place(relx = start_posx(0), rely = start_posy(0)[0])
        self.inputtxt1 = Text()
        self.inputtxt1.place(relx = start_posx(0), rely = start_posy(0)[1],relheight=lbl_sizey, relwidth=lbl_sizex)
        
        self.texto2 = Label(text="Quantity:",font=("Arial", 10),background=self.__background_color)
        self.texto2.place(relx = start_posx(1), rely = start_posy(0)[0])
        self.inputtxt2 = Text()
        self.inputtxt2.place(relx = start_posx(1), rely = start_posy(0)[1],relheight=lbl_sizey, relwidth=lbl_sizex)
        
        self.texto3 = Label(text="Planned Production:",font=("Arial", 10),background=self.__background_color)
        self.texto3.place(relx =start_posx(2), rely = start_posy(0)[0])
        self.inputtxt3 = Text()
        self.inputtxt3.insert(END,'70000')
        self.inputtxt3.place(relx = start_posx(2), rely = start_posy(0)[1],relheight=lbl_sizey, relwidth=lbl_sizex)
        
        self.texto4 = Label(text="Depreciation Time:",font=("Arial", 10),background=self.__background_color)
        self.texto4.place(relx = start_posx(3), rely = start_posy(0)[0])
        self.inputtxt4 = Text()
        self.inputtxt4.place(relx = start_posx(3), rely = start_posy(0)[1],relheight=lbl_sizey, relwidth=lbl_sizex)
        
        self.calculate = Button(text="CALCULATE", command=lambda: self.calculate_value())
        self.calculate.place(relx = start_posx(0), rely = start_posy(1)[0], relwidth=lbl_sizex,relheight=result_y)
        
        self.result = Text()
        #self.result.insert()
        self.result.place(relx = start_posx(1), rely = start_posy(1)[0],relheight=result_y, relwidth=result_x)
        
    def calculate_value(self):
        
        VEA = float(self.inputtxt1.get('1.0',END))
        amount = float(self.inputtxt2.get('1.0',END))
        prod = float(self.inputtxt3.get('1.0',END))
        dt = float(self.inputtxt4.get('1.0',END))
        
        formula = (VEA*amount) / (prod*dt)
        self.result.delete('1.0',END)
        self.result.insert(END, formula)
        print(formula)
        
Application()
