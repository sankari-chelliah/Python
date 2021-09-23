#Tower of Hanoi

def printMove(fr,to):

    """Input: Source and destination pole names
        Output: Prints the disc movement step """

    print('move from '+str(fr)+' move to '+ str(to))


def Towers(n,fr,to,spare):

    """ Solve Tower of Hanoi
    Input: number of disc(int), from_Pole(str), to_pole (str), spare_pole (str)
    Output: Prints the disc movement step"""

    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)

n = int(input("Enter the no. of discs to be moved: "))
print(Towers(n,'A','B','sp'))
