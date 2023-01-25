# in this file are a few lines of code to map and keep note of the class instances. 
# this should allow easily to access each instance when required to change something.

global control_reference
control_reference = {}

def addToControlReference(key, value):
    # this function will be called before creating an instance of a class.
    # it takes two arguments, a key and a value, which will be paired in the global dict.
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

def returnControlReference():
    # this function return the dict
    global control_reference
    return control_reference