import tkinter as tk
class shape:
    def __init__(self,canvas):
        self.canvas=canvas
    def draw(self):
        print("hello world")
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
class rectangle(shape):
    def __init__(self,canvas1,x,y,l,b,color):
        self.Canvas=canvas1
        self.x=x
        self.y=y
        self.l=l
        self.b=b
        self.color=color
    def draw(self):
        x0=self.x-self.l
        y0=self.y-self.b
        x1=self.x+self.l
        y1=self.y+self.b
        self.Canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
class pentagon(shape):
    def __init__(self,canvas1,u,v,w,x,y,color):
        self.Canvas=canvas1
        self.u=u
        self.v=v
        self.w=w
        self.x=x
        self.y=y
        self.color=color
    def draw(self):
        x0=self.x-self.u
        x1=self.x-self.v
        x2=self.x-self.w
        x3=self.x-self.x
        x4=self.x-self.y
        y0=self.y-self.u
        y1=self.y-self.v
        y2=self.y-self.w
        y3=self.y-self.x
        y4=self.y-self.y
        self.Canvas.create_rectangle(x0,x1,x2,x3,x4,y0,y1,y2,y3,y4,fill=self.color)
app=tk.Tk()
app.title('circle drawing-inheritance')
canvas=tk.Canvas(app,bg="white",width=1000,height=1000)
canvas.pack() 
circle1=Circle(canvas,200,200,100,'pink')
#circle1.draw()
rectangle1=rectangle(canvas,600,200,100,30,'#87CEEB')
#rectangle1.draw()
pentagon1=pentagon(canvas,900,100,100,100,100,"cyan")
pentagon1.draw()
app.mainloop()
