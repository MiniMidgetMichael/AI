#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time, inspect, pickle, os, AI

turtle_functions = turtle._tg_turtle_functions


class AI_goal_(object):
    def __init__(self, loc):
        ## 'loc' must be list with [xloc, yloc]
        assert (type(loc) is list),"loc must be <class 'list'>, not %s" % type(loc)
        assert (len(loc) == 2),"loc must contain x_cor and y_cor, not %s values" % len(loc)
        for i in loc:
            assert (type(i) is int),"coordinate must be <class 'int'> not %s" % type(i)

        x_cor = loc[0]
        y_cor = loc[1]
        self.loc = loc
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.Turtle = turtle.Turtle()
        self.Turtle.shape("circle")

    def _goto_coor(self):
        loc = self.loc
        x_cor = self.x_cor
        y_cor = self.y_cor
        turtle = self.Turtle
        turtle.pu()
        turtle.goto(x_cor, y_cor)
        


goal = AI_goal_([300,-360])
##goal >>> bottom-right corner



goal._goto_coor()
