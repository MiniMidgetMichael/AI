#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time, inspect, pickle, os, sys
from AI_target import *
from itertools import permutations as perm
from modules import functions

turtle_functions = turtle._tg_turtle_functions


class AI_(turtle.Turtle):
    def __init__(self, chance):
        assert ((type(chance) is int) and (chance > 0) and (chance < 100)), "chance must be int, and 0 < chance < 100"
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

    def _gen_values(self):
        actions = self.actions
        freq = range(self.chance, 100)
        if not(bool(actions)):
            for i in turtle_functions:
                actions[i] = random.choice(freq)
        options = {}
        for i, k in actions.items():
            options[i] = [0, "UK"]
        self.options = options
        ##print (actions)
        ##print (options)

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

    def act(self, t):
        self._gen_values()
        ##print(self.func_params)
        if not(self._file_empty("memory.txt")):
            with open("memory.txt", "rb") as f:
                func_params = pickle.load(f)
                self.func_params.update(func_params)
        ##print(self.func_params)
        func_params = self.func_params
        r_time = 0
        actions = self.actions
        chance = self.chance
        options = self.options
        func_params = self.func_params
        ##print (actions.values())
        ##values = list(actions.values())
        values = dict.fromkeys(actions.values())
        k = 0
        for i in values:
            values[i] = list(actions.keys())[k]
            k += 1
        ##print (values)
        action = random.choice(range(chance, 100))
        while r_time < t:
            action = random.choice(range(chance, 100))
            if (action in values):
                print (action, values[action])
                action = values[action]
                if not(self._param_needed(getattr(self.Turtle, action)) is False):
                    needed_param = self._param_needed(getattr(self.Turtle, action))
                    options[action][0] += 1
                    options[action][1] = needed_param
                    func_params[action] = self._working_param(getattr(self.Turtle, action), needed_param)
            else:
                print (action)
            time.sleep(0.5)
            r_time += 0.5

        with open("memory.txt", "wb") as f:
            func_params = self.func_params
            pickle.dump(func_params, f)

    def _working_param(self, fun, params):
        ##  IF FUN HAS 2 PARAMS, IT GENERATES 2 PARAMS, THEN DOES FUN(PARAM_0), FUN(PARAM_1), PASSING ONLY 1 PARAM AT A TIME
        ##  USE: '_new_working_param'
        func_params = self.func_params
        rnd_value = random.choice(range(100))
        types = ['str', 'int', 'bool']
        values = []
        strings = [i for i in range(0b01100001,0b01111010)]
        good_type = False
        for i in params:
            for index, i in enumerate(types):
                if index == 0:
                    ##type == str
                    len_ = random.choice(range(3, 10))
                    value = ""
                    for i in range(len_):
                        value += chr(random.choice(strings))
                    values.append(value)
                elif index == 1:
                    ##type == int
                    value = random.choice(range(1, 50))
                    values.append(value)
                else:
                    ##type == bool
                    value = random.choice(range(0,1))
                    ##choose either 1 or 0
                    value = bool(value)
                    ##convert value to bool [i.e. 1 ==> True, 0 ==> False]
                    values.append(value)
        for index, i in enumerate(values):
            try:
                fun(i)
                return i
            except:
                pass
                

    def _new_working_param(self, fun, params):
        func_params = self.func_params
        param_dict = {}
        n_params = len(params)
        strings = [i for i in range(0b01100001,0b01111010)]
        values = {} # for each param, gen: str, int, bool value
        total_values = []
        ##print ("fun: ", fun, "# of params: ",n_params)
        """EX:
            fun = circle
            params = ['radius', 'degrees'] >>> [<class 'int'>, <class 'int'>]

            circle(radius,degrees=360)
        """
        for p in params:
            if (p != 'self') and (p != None):
                param_dict.setdefault(p)
        params = param_dict
        
        for i in params:
            values.setdefault(i, [None, None, None])
            for typ in range(3):
                ## 0 >>> str
                ## 1 >>> int
                ## 2 >>> bool
                if typ == 0:
                    ## str
                    len_ = random.choice(range(3,10))
                    str_value = ""
                    for s in range(len_):
                        str_value += chr(random.choice(strings))
                    values[i][0] = str_value
                if typ == 1:
                    ## int
                    int_value = random.choice(range(1,50))
                    values[i][1] = int_value
                elif typ == 2:
                    ## bool
                    bool_value = bool(random.choice(range(2)))
                    values[i][2] = bool_value
        
        """print (values) >>> {
            'param_0' : ['abc', 012, True],
            'param_1' : ['cde', 345, False]
            }
        """
        """print (params) >>> {
            'param_0' : None,
            'param_1' : None
            }
        """
        for v in values.values():
            for i in v:
                total_values.append(i)

        """print (total_values) >>> ['abc',012,True,'cde',345,False]"""
        ##permutations(iterable[, r]) --> permutations object
        ##print (list(perm(total_values,2)))
        perms = perm(total_values,n_params-1)
        ##DON'T PRINT PERMUTATIONS!!!!
        for p in perms:
            try:
                fun(*p)
                return [*p]
            except:
                pass
        
        



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

    def save_stats(self, f_params=None, prefs=None):
        assert (not((f_params is None) and (prefs is None))),"Please specify object to save"
        with open(f_params, "wb") as f:
            pickle.dump(self.func_params, f)
        with open(prefs, "wb") as p:
            pickle.dump(self.prefs, p)

    def _run_again(self, act):
        chance = self.chance
        prefs = self.prefs
        ## >>> [1, 0, 0, 1, etc.]
        again = random.choice(range(act, (100-chance)))
        if again == act:
            ##prefers that option
            return True

    def _good_cycle(self, cycle):
        assert (type(cycle) is dict),"cycle must be of <class 'dict'> with structure: {'func' : 'param'}, not %s" % type(cycle)


    def smart_act(self, t):
        working_param = None
        prefs = self.prefs
        self._smart_gen_values()
        actions = self.actions # {fun_int: 'func_name'}
        action_keys = actions.keys() # [fun_int]
        action_values = actions.values() # ['func_name']
        prev_x = self.Turtle.xcor()
        prev_y = self.Turtle.ycor()
        func_params = self.func_params
        chance = self.chance
        times = 0
        again = False
        if not(self._file_empty("params.txt")):
            with open("params.txt", "rb") as f:
                f_func_params = pickle.load(f)
                func_params.update(f_func_params)
        if not(self._file_empty("prefs.txt")):
            with open("prefs.txt", "rb") as f:
                f_prefs = pickle.load(f)
                prefs.update(f_prefs)

        rec_positions = self.rec_positions
        prev_x = self.Turtle.xcor()
        prev_y = self.Turtle.ycor()
        while (times < t):
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
                                    ##print ("#MOVED")
                                    print ("COORDINATES: ",self.Turtle.xcor(), self.Turtle.ycor())
                                    prefs[action] += 1

                        times += 1
                        again = True
            if again == True:
                func_params[action] = working_param
                continue
                        
            
            action = random.choice(range(chance, 100))
            ##print (action)
            if (action in action_keys):
                action_val = action
                action = actions[action]
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
                        ##print ("#MOVED")
                        print ("COORDINATES: ",self.Turtle.xcor(), self.Turtle.ycor())
                        if not(action in prefs):
                            prefs.setdefault(action, 0)
                        else:
                            prefs[action] += 1

            func_params[action] = working_param
            if not(again):
                time.sleep(0.5)
                times += 1
            else:
                time.sleep(0.5)

            prev_x = curr_x
            prev_y = curr_y


"""
    END OF CLASS
"""


def cycle(acts, cycles):
    c = 0
    while (c != cycles):
        print ("PREFS: ",AI.get_prefs())
        AI.smart_act(acts)
        AI.save_stats(f_params="params.txt", prefs="prefs.txt")
        print ("PREFS: ",AI.get_prefs())
        print ("REC_POSITIONS: ", AI.rec_positions)
        c += 1
        print ("END OF CYCLE #%s" % c)


if __name__ == "__main__":
    screen = turtle.Screen()
    AI = AI_(10)
    acts = int(functions.good_input("How many actions per cycle? [up to 50]:", values=[str(i) for i in range(1,51)]))
    cycles = int(functions.good_input("How many cycles? [up to 10]:", values=[str(i) for i in range(1,11)]))
    cycle(acts, cycles)

