"""Problem
Write a function called avg that takes two parameters. Return the average of these two parameters. If the parameters are not numbers, return the string, Please use two numbers as parameters.
Expected Output
If the function call is avg(10,25), then the function would return 17.5
If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters"""

def avg(par1, par2):
    try:
        return (par1 + par2) / 2
    except TypeError:
        return "Please use two numbers as parameters"
      
""" Don't call the function when submitting """
