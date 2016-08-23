#! /usr/bin/python3
import random, math, turtle, time, inspect, pickle, os, sys
from AI_target import *
from itertools import permutations as perm
from itertools import combinations as comb
from modules import functions

turtle_functions = turtle._tg_turtle_functions
bad_functions = ['undobufferentries', 'setundobuffer', 'getscreen', 'ht', 'onclick', 'onrelease', 'ondrag', 'clearstamp', 'clearstamps', 'radians', 'shapesize', 'shape', 'width', 'resizemode', 'shearfactor', 'shapetransform', 'turtlesize']#, ...etc.
for i in turtle_functions:
    if i in bad_functions:
        turtle_functions.remove(i)
        ##print ("Removing %s from turtle_functions" % i)

class AI_(turtle.Turtle):
    def __init__(self, chance, screen):
        assert ((type(chance) is int) and (chance > 0) and (chance < 100)), "chance must be int, and 0 < chance < 100"
        assert (type(screen) is turtle._Screen),"screen must be <class 'turtle.Screen>, not %s" % type(screen)
        self.screen = screen
        self.chance = chance
        __turtle_ = turtle.Turtle()
        self.Turtle = __turtle_
        actions = {}
        self.actions = actions
        func_params = {}
        good_functions = {}
        prefs = {}
        self.prefs = prefs
        self.good_functions = good_functions
        self.func_params = func_params
        rec_positions = []
        self.rec_positions = rec_positions
        self.cycles = {}

    def _smart_gen_values(self):
        actions = self.actions
        prefs = self.prefs
        freq = range(self.chance, 100)
        if not(bool(actions)):
            for i in turtle_functions:
                actions[random.choice(freq)] = i

    def _param_needed(self, fun):
        if not(inspect.getargspec(fun)[0]) is None:
            needed_param = inspect.getargspec(fun)[0]
            return needed_param
        else:
            return False

    def _file_empty(self, file):
        return False if os.path.isfile(file) and os.path.getsize(file) > 0 else True

    def _new_working_param(self, fun, params):
        func_params = self.func_params
        param_dict = {}
        """EX:
            fun = circle
            params = ['radius', 'degrees'] >>> [<class 'int'>, <class 'int'>]

            circle(radius,degrees=360)
        """
        self_none = 0
        for p in params:
            if not ((p == 'self') and (p == None)):
                param_dict.setdefault(p)
            else:
                self_none += 1
        if self_none == len(params) - 1:
            print ("All params were 'self' or 'None', returning ...")
            return params

        params = param_dict

        none_run = 0

        
        """print (values) >>> {
            'param_0' : [012, 'abc', True],
            'param_1' : [345, 'def', False]
            }
        """
        """print (params) >>> {
            'param_0' : None,
            'param_1' : None
            }
        """

        """print (total_values) >>> [012, 'abc', True, 345, 'def', False]"""
        ##permutations(iterable[, r]) --> permutations object
        ##combinations(iterable[, r]) --> combinations object
        g_params = self.__gen_params(params)
        while g_params == 'break':
            g_params = self.__gen_params(params)
        else:
            return g_params

    def __gen_params(self, params):
        strings = [i for i in range(0b01100001,0b01111010)]
        values = {}
        working_perms = False
        total_values = []
        n_perms = []
        n_params = len(params)
        
        for i in params:
            values.setdefault(i, [0, 0, 0])
            for typ in range(3):
                ## 0 >>> int
                ## 1 >>> bool
                ## 2 >>> str
                if typ == 0:
                    ## int
                    int_value = random.choice(range(-90,90))
                    values[i][0] = int_value
                elif typ == 1:
                    ## bool
                    bools = [True, False]
                    bool_value = random.choice(bools)
                    values[i][1] = bool_value
                elif typ == 2:
                    ## str
                    len_ = random.choice(range(3,10))
                    str_value = ""
                    for s in range(len_):
                        str_value += chr(random.choice(strings))
                    values[i][2] = str_value

        ## values == {
        ##            'param'   : [123, True, 'abc'],
        ##            'param_1' : [345, False, 'def'], ...
        ##           }

        p_dict = {}
        p_loc = 0
        ## create perm of values[k] for parameters







##        for v in values.values():
##            for i in v:
##                total_values.append(i)
##
##        perms = perm(total_values,n_params-1)
##
##        perms = list(perms)
##
##        has_str = False
##
##        for index, i in enumerate(perms):
##            for p_index, p in enumerate(i):
##                if (type(p) is str):
##                    has_str = True
##                    n_perms.append(i)
##                if (p_index == len(i) - 1) and not(has_str):
##                    n_perms.insert(0, i)

        for p in n_perms:
            p = list(p)
            try:
                fun(*p)
                working_perms = True
                return [*p]
            except:
                ##print ("%s did not work" % [*p])
                pass
            
        #print ("\n", "P : %s |" % p, " type(p) : %s" % type(p), "\n")
        return 'break' # didn't working, returning to _new_working_param

    def get_ran_fun(self):
        if not(self._file_empty("memory.txt")):
            with open("memory.txt", "rb") as f:
                ran_functs = pickle.load(f)
                return ran_functs

    def get_prefs(self):
        if not(self._file_empty("prefs.txt")):
            with open("prefs.txt", "rb") as p:
                prefs = pickle.load(p)
                self.prefs.update(prefs)
                return prefs
        else:
            print ("prefs.txt file is empty")
            return self.prefs

    def get_params(self):
        if not(self._file_empty("params.txt")):
            with open("prefs.txt", "rb") as f:
                params = pickle.load(f)
                self.func_params.update(params)
                return self.func_params
        elif bool(self.func_params):
            return self.func_params
        else:
            print ("Please run AI at least once to get function parameters")

    def save_stats(self, f_params=None, prefs=None, cycles=None):
        assert (not((f_params is None) and (prefs is None) and (cycles is None))),"Please specify object to save"
        if not(f_params is None):
            with open(f_params, "wb") as f:
                pickle.dump(self.func_params, f)
        if not(prefs is None):
            with open(prefs, "wb") as p:
                pickle.dump(self.prefs, p)
        if not(cycles is None):
            with open(cycles, "wb") as p:
                pickle.dump(self.cycles, p)

    def erase_stats(self, f_params=False, prefs=False, cycles=False, all_=False):
        assert (not((f_params is False) and (prefs is False) and (cycles is False) and (all_ is False))),"Please specify object to erase"
        if f_params:
            certain = functions.good_input("Are you sure you want to erase 'f_params'?: [y] or [n]\n", values=['y', 'n']).casefold()
            if certain == 'y':
                print ("Erasing 'params'... \n")
                open("params.txt", "wb").close()
            else:
                print ("Not erasing 'f_params'... \n")
        if prefs:
            certain = functions.good_input("Are you sure you want to erase 'prefs'?: [y] or [n]\n", values=['y', 'n']).casefold()
            if certain == 'y':
                print ("Erasing 'prefs'... \n")
                open("prefs.txt", "wb").close()
            else:
                print ("Not erasing 'prefs'... \n")
        if cycles:
            certain = functions.good_input("Are you sure you want to erase 'cycles'?: [y] or [n]\n", values=['y', 'n']).casefold()
            if certain == 'y':
                print ("Erasing 'cycles'... \n")
                open("cycles.txt", "wb").close()
            else:
                print ("Not erasing 'cycles'... \n")
        if all_:
            certain = functions.good_input("Are you sure you want to erase EVERYTHING?: [y] or [n]\n", values=['y', 'n']).casefold()
            if certain == 'y':
                print ("Erasing EVERYTHING... \n")
                open("params.txt", "wb").close()
                open("prefs.txt", "wb").close()
                open("cycles.txt", "wb").close()
                open("memory.txt", "wb").close()
                open("last_acts.txt", "wb").close()
            else:
                print ("Not erasing EVERYTHING... \n")

    def _run_again(self, act):
        ##print ("\n", "#ACT: ", act, "\n")
        chance = self.chance
        ## >>> [1, 0, 0, 1, etc.]
        ##print ("\n", "RANGE(ACT, (101-CHANCE)): ", range(act, (101-chance)), "\n")
        again = random.choice(range(act - 1, (101-chance)))
        if again == act:
            ##prefers that option
            return True

    def _good_cycle(self, cycle, positions):
        assert (type(cycle) is list),"cycle must be of <class 'list'> with structure: [['func', ['param']], ['func1', ['param1']]], not %s" % type(cycle)
        assert (type(positions) is list),"positions must be of <class 'list'> with structure: [['func', [x_cor, y_cor]]], not %s" % type(positions)
        goal_loc = goal.get_coor()
        goal_x = goal_loc[0]
        goal_y = goal_loc[1]
        cycle_pref = {}
        self.cycle_pref = cycle_pref
        if len(positions) == 0:
            return
        for index, i in enumerate(cycle):
            cycle_pref[index] = [i, 0]
            ##print ("\n", "#cycle_pref :", cycle_pref, "\n")
            """ {0 : ['func', ['param']],
                 1 : ['func_1', ['param_1']]
                } """
        print ("\n", "#CYCLE: ", cycle, "\n")
        print ("\n", "#POSITIONS: ", positions, "\n")
        prev_loc = [0, 0]
        prev_x_diff = abs(positions[0][1][0] - goal_x)
        prev_y_diff = abs(positions[0][1][1] - goal_y)
        good_cycle = False
        for index, i in enumerate(positions):
            fun = i[0]
            loc = i[1]
            x_cor = loc[0]
            y_cor = loc[1]
            prev_x = prev_loc[0]
            prev_y = prev_loc[1]
            x_diff = abs(int(x_cor) - int(goal_x))
            y_diff = abs(int(y_cor) - int(goal_y))
            if (x_diff < prev_x_diff) and (y_diff < prev_y_diff):
                cycle_pref[index][1] += 1
                good_cycle = True
                #print ("#x < prev_x; y < prev_y")
            elif (x_diff < prev_x_diff) and (y_diff == prev_y_diff):
                cycle_pref[index][1] += 1
                good_cycle = True
                #print ("#x < prev_x; y == prev_y")
            elif (y_diff < prev_y_diff) and (x_diff == prev_x_diff):
                cycle_pref[index][1] += 1
                good_cycle = True
                #print ("#x == prev_x; y < prev_y")
            prev_loc = loc
            prev_x_diff = x_diff
            prev_y_diff = y_diff
        if good_cycle:
            print ("\n", "#GOOD_CYCLE", "\n")

        print ("\n", "#CYCLE_PREF: ", cycle_pref, "\n")
            
            
            
        

    def smart_act(self, t):
        working_param = None
        prefs = self.prefs
        screen = self.screen
        cyles = self.cycles
        self._smart_gen_values()
        actions = self.actions # {fun_int: 'func_name'}
        action_keys = actions.keys() # [fun_int]
        action_values = actions.values() # ['func_name']
        prev_x = self.Turtle.xcor()
        prev_y = self.Turtle.ycor()
        func_params = self.func_params
        chance = self.chance
        pos_with_fun = []
        times = 0
        again = False
        cycle = list()
        screen.listen()
        screen.update()
        if not(self._file_empty("params.txt")):
            with open("params.txt", "rb") as f:
                f_func_params = pickle.load(f)
                func_params.update(f_func_params)
        if not(self._file_empty("prefs.txt")):
            with open("prefs.txt", "rb") as f:
                f_prefs = pickle.load(f)
                prefs.update(f_prefs)
        if not(self._file_empty("cycles.txt")):
            with open("cycles.txt", "rb") as f:
                f_cycles = pickle.load(f)
                cycles.update(f_cycles)

        rec_positions = self.rec_positions
        prev_x = self.Turtle.xcor()
        prev_y = self.Turtle.ycor()
        while (times < t):
            working_param = None
            curr_x = None
            curr_y = None
            again = False


            for k,v in prefs.items():
                
                if v >= 1:
                    if self._run_again(v) == True:
                        print ("#DO AGAIN: ")
                        action = k
                        if not(self._param_needed(getattr(self.Turtle, action)) is False):
                            needed_param = self._param_needed(getattr(self.Turtle, action))
                            fun = getattr(self.Turtle, action)
                            working_param = self._new_working_param(fun, needed_param)
                            print (action, working_param)
                            curr_x = self.Turtle.xcor()
                            curr_y = self.Turtle.ycor()
                            curr_pos = [curr_x, curr_y]
                            if not(curr_pos in rec_positions):
                                if (curr_pos != [0, 0]):
                                    ##if self.Turtle hasn't been in current pos, record it
                                    rec_positions.append(curr_pos)
                                    pos_with_fun.append([action, curr_pos])
                                    ##print ("#MOVED")
                                    print ("COORDINATES: ",self.Turtle.xcor(), self.Turtle.ycor())
                                    prefs[action] += 1

                        times += 1
                        again = True
            if again == True:
                cycle.append([action, working_param])
                ##print ("#CYCLE IN 'smart_act': ", cycle)
                if not(working_param is None):
                    func_params[action] = working_param
                continue
                        
            
            action = random.choice(range(chance, 100))
            ##print (action)
            if (action in action_keys):
                action_val = action
                action = actions[action]
                ##cycle.append([action, working_param])
                if ((action == 'hideturtle') or (action == 'ht')):
                    print ("\n", "#PREVENTING AI FROM HIDING", "\n")
                    times -= 1
                    continue
                elif (action == 'shearfactor'):
                    print ("\n", "#PREVENTING AI FROM SHEARING", "\n")
                    times -= 1
                    continue
                if not(self._param_needed(getattr(self.Turtle, action)) is False):
                    needed_param = self._param_needed(getattr(self.Turtle, action))
                    fun = getattr(self.Turtle, action)
                    working_param = self._new_working_param(fun, needed_param)
                    print (action, working_param)
                    curr_x = self.Turtle.xcor()
                    curr_y = self.Turtle.ycor()
                    curr_pos = [curr_x, curr_y]
                    if not(curr_pos in rec_positions):
                        ##if self.Turtle hasn't been in current pos, record it
                        rec_positions.append(curr_pos)
                        pos_with_fun.append([action, curr_pos])
                        ##print ("#MOVED")
                        print ("COORDINATES: ",self.Turtle.xcor(), self.Turtle.ycor())
                        if not(action in prefs):
                            prefs.setdefault(action, 0)
                        else:
                            prefs[action] += 1
                    if not(action in cycle):
                        cycle.append([action, working_param])
                    ##print ("#CYCLE IN 'smart_act': ", cycle)
                    if not(working_param is None):
                        func_params[action] = working_param

            func_params[action] = working_param
            if not(again):
                time.sleep(0.25)
                times += 1
            else:
                time.sleep(0.25)

            prev_x = curr_x
            prev_y = curr_y
        self._good_cycle(cycle, pos_with_fun)
        


"""
    END OF CLASS
"""


def cycle(cycles):
    acts = 30
    c = 0
    while (c != cycles):
        print ("\n", "PREFS: ",AI.get_prefs(), "\n")
        AI.smart_act(acts)
        AI.save_stats(f_params="params.txt", prefs="prefs.txt")
        print ("\n", "PREFS: ",AI.get_prefs(), "\n")
        print ("\n", "REC_POSITIONS: ", AI.rec_positions, "\n")
        c += 1
        print ("\n", "END OF CYCLE #%s" % c, "\n")
        print ("\n", "RESETTING TURTLE", "\n")
        AI.Turtle.reset()


if __name__ == "__main__":
    screen = turtle.Screen()
    AI = AI_(10, screen)
    ##acts = int(functions.good_input("How many actions per cycle? [up to 50]:", values=[str(i) for i in range(1,51)]))
    cycles = int(functions.good_input("How many cycles? [up to 10]:", values=[str(i) for i in range(1,11)]))
    cycle(cycles)

