import tkinter
from PIL import Image, ImageTk, ImageGrab
import random


def text_getter(name, x0, x1, y0, y1, destroyer):
    ImageGrab.grab().crop((x0, y0, x1, y1)).save('tech_paint\\{}.jpg'.format(name.get()))
    destroyer.destroy()


class Drawer:
    def __init__(self):
        self.height = 600
        self.width = 600
        self.line_start_point = [0, 0]
        self.dispersion_start_point = [0, 0]
        self.current_thickness = 2
        self.colors = ['black', 'red', 'blue', 'green', 'yellow', 'pink', 'orange', 'violet', 'brown', 'grey']
        self.color = 'black'
        self.instrument = 'pencil'
        self.root = tkinter.Tk()
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.canv = tkinter.Canvas(height=self.height, width=self.width, bg='white')
        self.canv.create_rectangle(0, 0, self.width, 102, fill='grey')
        self.create_colors()
        self.current_color = self.canv.create_rectangle(0, 0, self.width // len(self.colors), 50, outline='white',
                                                        width=2)
        self.create_instruments()
        self.current_instrument = self.canv.create_rectangle(0, 50, 52, 102, outline='black', width=2)
        self.thickness_box = self.canv.create_rectangle(self.width - 100, 52, self.width - 50,
                                                        102, outline='black', width=2)
        self.canv.bind('<1>', self.click)
        self.canv.pack()
        self.last_obj = [[self.canv.create_rectangle(0, 0, 0, 0)]]
        self.canv.bind('<B1-Motion>', self.motion)
        self.prev_line = self.canv.create_line(0, 0, 0, 0)
        self.root.mainloop()

    def create_colors(self):
        step = self.width // len(self.colors)
        for u in range(len(self.colors)):
            self.canv.create_rectangle(u * step, 0, (u + 1) * step, 50, fill=self.colors[u])

    def create_instruments(self):
        photo_pencil = Image.open('pencil.png')
        self.canv.pencil = ImageTk.PhotoImage(photo_pencil)
        self.canv.create_image(25, 77, image=self.canv.pencil)
        photo_eraser = Image.open('eraser.png')
        self.canv.eraser = ImageTk.PhotoImage(photo_eraser)
        self.canv.create_image(75, 77, image=self.canv.eraser)
        photo_line = Image.open('line.png')
        self.canv.line = ImageTk.PhotoImage(photo_line)
        self.canv.create_image(125, 77, image=self.canv.line)
        photo_one = Image.open('one.png')
        self.canv.one = ImageTk.PhotoImage(photo_one)
        self.canv.create_image(self.width - 125, 77, image=self.canv.one)
        photo_two = Image.open('two.png')
        self.canv.two = ImageTk.PhotoImage(photo_two)
        self.canv.create_image(self.width - 75, 77, image=self.canv.two)
        photo_three = Image.open('three.png')
        self.canv.three = ImageTk.PhotoImage(photo_three)
        self.canv.create_image(self.width - 25, 77, image=self.canv.three)
        photo_dispersion = Image.open('dispersion.png')
        self.canv.dispersion = ImageTk.PhotoImage(photo_dispersion)
        self.canv.create_image(175, 77, image=self.canv.dispersion)
        photo_undo = Image.open('undo.png')
        self.canv.undo = ImageTk.PhotoImage(photo_undo)
        self.canv.create_image(225, 77, image=self.canv.undo)
        photo_clear = Image.open('clear.png')
        self.canv.clear = ImageTk.PhotoImage(photo_clear)
        self.canv.create_image(275, 77, image=self.canv.clear)
        photo_save = Image.open('save.png')
        self.canv.save = ImageTk.PhotoImage(photo_save)
        self.canv.create_image(325, 77, image=self.canv.save)

    def saver(self):
        x0 = self.canv.winfo_rootx() + 2
        y0 = self.canv.winfo_rooty() + 104
        x1 = self.canv.winfo_rootx() + self.width
        y1 = self.canv.winfo_rooty() + self.height
        name = tkinter.Toplevel(self.root)
        name_str = tkinter.StringVar(name)
        ask = tkinter.Entry(name, textvariable=name_str)
        tkinter.Label(name, text='enter file name').grid(row=0, column=0, columnspan=2)
        ask.grid(row=1, column=0)

        submit = tkinter.Button(name, text='submit', command=lambda: text_getter(name_str, x0, x1, y0, y1, name))
        submit.grid(row=1, column=1)

    def click(self, event):
        if event.y <= 50:
            step = self.width // len(self.colors)
            for u in range(len(self.colors)):
                if step * u <= event.x <= step * (u + 1):
                    self.canv.delete(self.current_color)
                    self.current_color = self.canv.create_rectangle(u * step, 0, step * (u + 1), 50, outline='white',
                                                                    width=2)
                    self.color = self.colors[u]
                    break
            if self.width - step <= event.x <= self.width:
                self.color = self.colors[random.randint(0, len(self.colors) - 1)]
        elif event.y <= 102:
            if 0 <= event.x <= 52:
                self.instrument = 'pencil'
                self.canv.delete(self.current_instrument)
                self.current_instrument = self.canv.create_rectangle(0, 50, 52, 102, outline='black', width=2)
            elif 53 <= event.x <= 102:
                self.instrument = 'eraser'
                self.canv.delete(self.current_instrument)
                self.current_instrument = self.canv.create_rectangle(53, 50, 102, 102, outline='black', width=2)
            elif 103 <= event.x <= 152:
                self.instrument = 'line'
                self.canv.delete(self.current_instrument)
                self.current_instrument = self.canv.create_rectangle(106, 50, 152, 102, outline='black', width=2)
            elif self.width - 150 <= event.x <= self.width - 100:
                self.current_thickness = 0
                self.canv.delete(self.thickness_box)
                self.thickness_box = self.canv.create_rectangle(self.width - 150, 52, self.width - 100,
                                                                102, outline='black', width=2)
            elif self.width - 100 <= event.x <= self.width - 50:
                self.current_thickness = 2
                self.canv.delete(self.thickness_box)
                self.thickness_box = self.canv.create_rectangle(self.width - 100, 52, self.width - 50,
                                                                102, outline='black', width=2)
            elif self.width - 50 <= event.x <= self.width:
                self.current_thickness = 5
                self.canv.delete(self.thickness_box)
                self.thickness_box = self.canv.create_rectangle(self.width - 50, 52, self.width,
                                                                102, outline='black', width=2)
            elif 150 <= event.x <= 200:
                self.instrument = 'dispersion'
                self.canv.delete(self.current_instrument)
                self.current_instrument = self.canv.create_rectangle(150, 52, 200, 102, outline='black', width=2)
            elif 200 <= event.x <= 250:
                if len(self.last_obj) != 0:
                    for el in range(len(self.last_obj[len(self.last_obj) - 1]) - 1, -1, -1):
                        self.canv.delete(self.last_obj[len(self.last_obj) - 1][el])
                    self.last_obj = self.last_obj[:len(self.last_obj) - 1]
            elif 250 <= event.x <= 300:
                if len(self.last_obj) != 0:
                    for y in self.last_obj:
                        for el in y:
                            self.canv.delete(el)
                self.last_obj = []
            elif 300 <= event.x <= 350:
                self.saver()

        else:
            self.last_obj.append([])
            if self.instrument == 'line':
                self.line_start_point = [event.x, event.y]
                self.prev_line = self.canv.create_line(event.x, event.y, event.x, event.y)
                self.last_obj[len(self.last_obj) - 1].append(self.prev_line)
            elif self.instrument == 'dispersion':
                self.dispersion_start_point = [event.x, event.y]

    def motion(self, event):
        if event.y > 103:
            if self.instrument == 'pencil':
                self.last_obj[len(self.last_obj) - 1].append(self.canv.create_rectangle(
                                                                event.x - self.current_thickness,
                                                                event.y - self.current_thickness,
                                                                event.x + self.current_thickness,
                                                                event.y + self.current_thickness,
                                                                fill=self.color, outline=self.color))
            elif self.instrument == 'eraser' and event.y > 112:
                self.last_obj[len(self.last_obj) - 1].append(self.canv.create_rectangle(
                                                                event.x - 8 - self.current_thickness,
                                                                event.y - 8 - self.current_thickness,
                                                                event.x + 8 + self.current_thickness,
                                                                event.y + 8 + self.current_thickness,
                                                                fill='white', outline='white'))
            elif self.instrument == 'line':
                self.canv.delete(self.prev_line)
                self.last_obj[len(self.last_obj) - 1] = self.last_obj[len(self.last_obj) - 1][:len(self.last_obj) - 1]
                self.prev_line = self.canv.create_line(self.line_start_point[0], self.line_start_point[1], event.x,
                                                       event.y, fill=self.color, width=self.current_thickness)
                self.last_obj[len(self.last_obj) - 1].append(self.prev_line)
            elif self.instrument == 'dispersion':
                self.last_obj[len(self.last_obj) - 1].append(self.canv.create_line(self.dispersion_start_point[0],
                                                             self.dispersion_start_point[1],
                                                             event.x, event.y,
                                                             fill=self.color, width=self.current_thickness))


Drawer()
