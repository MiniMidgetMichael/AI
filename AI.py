#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time, inspect, pickle, os

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
                ##func_params[fun] = i
                ##print (i, 'i')
                return i
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
                return prefs
        else:
            return self.prefs

    def save_stats(self, f_params=None, prefs=None):
        assert (not(f_params is None) or not(prefs is None)),"Please specify object to save"
        if not(f_params is None):
            with open("params.txt", "wb") as f:
                pickle.dump(self.func_params, f)
        elif not(prefs is None):
            with open("prefs.txt", "wb") as p:
                pickle.dump(self.prefs, p)

    def _run_again(self, act):
        chance = self.chance
        prefs = self.prefs
        ## >>> [1, 0, 0, 1, etc.]
        again = random.choice(range(act, (100-chance)))
        if again == act:
            ##prefers that option
            return True

    def smart_act(self, t):
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

        while (times < t):
            again = False
            prev_x = self.Turtle.xcor()
            prev_y = self.Turtle.ycor()
            for k,v in prefs.items():
                if v >= 1:
                    if self._run_again(v) == True:
                        print ("#DO AGAIN: ")
                        action = k
                        if not(self._param_needed(getattr(self.Turtle, action)) is False):
                            needed_param = self._param_needed(getattr(self.Turtle, action))
                            fun = getattr(self.Turtle, action)
                            working_param = self._working_param(fun, needed_param)
                            print (action, working_param)
                            if type(self._working_param(fun, needed_param)) is int:
                                if ((self.Turtle.xcor() != prev_x) or (self.Turtle.ycor() != prev_y)):
                                    ##print ("#MOVED")
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
                    working_param = self._working_param(fun, needed_param)
                    print (action, working_param)
                    if type(self._working_param(fun, needed_param)) is int:
                        if ((self.Turtle.xcor() != prev_x) or (self.Turtle.ycor() != prev_y)):
                            ##print ("#MOVED")
                            prefs[action] += 1

            func_params[action] = working_param
            if not(again):
                time.sleep(0.5)
                times += 1
            else:
                time.sleep(0.5)


screen = turtle.Screen()
AI = AI_(10)
##AI.act(10)
print (AI.get_prefs(), "\n")
AI.smart_act(15)
AI.save_stats(prefs="prefs.txt", f_params="params.txt")
print ("\n", AI.get_prefs())
print ("\n" * 2, AI.get_ran_fun())
