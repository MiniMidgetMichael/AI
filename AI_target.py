#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time, inspect, pickle, os, AI

turtle_functions = turtle._tg_turtle_functions


class AI_goal_(object):
    def __init__(self, loc):
        ## 'loc' must be list with [xloc, yloc]
        assert (type(loc) is tuple),"loc must be <class 'tuple'>, not %s" % type(loc)
        assert (len(loc) == 2),"loc must contain x_cor and y_cor, not %s values" % len(loc)
        for i in loc:
            assert (type(i) is int),"coordinate must be <class 'int'> not %s" % type(i)

        x_cor = loc[0]
        y_cor = loc[1]
        self.loc = loc
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.Turtle = turtle.Turtle()
        self.Turtle.hideturtle()
        self.Turtle.shape("circle")

        self._goto_coor()

    def _goto_coor(self):
        loc = self.loc
        x_cor = self.x_cor
        y_cor = self.y_cor
        turtle = self.Turtle
        turtle.pu()
        turtle.goto(x_cor, y_cor)
        turtle.showturtle()
        

    def get_coor(self):
        turtle = self.Turtle
        loc = [0,0]
        loc[0] = turtle.xcor()
        loc[1] = turtle.ycor()
        return loc






if not(__name__) == "__main__":
    goal = AI_goal_((300,-365))
    ##goal >>> circle
    ##goal >>> bottom-right corner

    print (goal.get_coor())
