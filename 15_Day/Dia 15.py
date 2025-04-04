def isPythonVariable(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(isPythonVariable(variable='variable1'))