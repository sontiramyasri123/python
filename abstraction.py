import  tkinter as tk
class shape:
    def draw(self):
         raise NotImplemetedError("subclasses implemented this")
class square(shape):
    def draw(self,side):
        pass
class Circle(shape):
    def __init__(self,canvas1,x,y,radius,color):
        self.Canvas=canvas1
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
    def draw(self):
        x0=self.x-self.radius
        y0=self.y-self.radius
        x1=self.x+self.radius
        y1=self.y+self.radius
        self.Canvas.create_oval(x0,y0,x1,y1,fill=self.color)
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def get_y(self):
        return self.y
    def set_radius(self,radius):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
app=tk.Tk()
app.title('circle drawing-encapsulation')
canvas=tk.Canvas(app,bg="white",width=1000,height=1000)
canvas.pack() 
circle1=Circle(canvas,200,200,100,'pink')
circle1.draw()
app.mainloop()
