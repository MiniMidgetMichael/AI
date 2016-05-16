#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
from inspect import isclass



def good_input(prompt, typ=None, values=None):
        assert (type(prompt) is str),"prompt must be <class 'str'>, not %s" % type(prompt)
        assert (not(typ is None) or not(values is None)),"must be one of either 'typ' or 'values'"
        if not(typ is None):
            assert (isclass(typ)),"typ must be a class type"
        if not(values is None):
            assert (type(values) is list),"values must be <class 'list'>, not %s" % type(values)

        is_good = False
        while not(is_good):
            ans = input(prompt).casefold()
            if not(typ is None):
                try:
                    typ(ans)
                    is_good = True
                    return ans
                except:
                    print ("%s is not a valid response" % ans)
            elif not(values is None):
                if ans in values:
                    is_good = True
                    return ans
                else:
                    print ("Please only answer with one of %s, not %s" % (values, ans))
