import  tkinter as tk
class Circle:
    def __init__(self,canvas1,x,y,radius,color):
        self.Canvas=canvas1
        self.__x=x
        self.y=y
        self.radius=radius
        self.color=color
    def draw(self):
        x0=self.__x-self.radius
        y0=self.y-self.radius
        x1=self.__x+self.radius
        y1=self.y+self.radius
        self.Canvas.create_oval(x0,y0,x1,y1,fill=self.color)
class Application(tk.Tk):
  def __init__(self):
        super().__init__()
        self.title("circle drawing in OOp style")
        self.geometry('400x400')
        self.canvas=tk.Canvas(self,bg="white",width=400,height=400)
        self.canvas.pack() 
        circle1=Circle(self.canvas,100,200,100,'pink')
        circle1.draw()
        circle2=Circle(self.canvas,200,225,100,'yellow')
        circle2.draw()
if __name__=='__main__':
    app=Application()
    app.mainloop()
