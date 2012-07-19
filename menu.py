'''File I decided to the programs in.'''
import euler
import string
import webbrowser

exit = False
selection = ""
PROOFURL = "http://projecteuler.net/profile/Shaggy-Rodgers.png"
EURLER = "http://projecteuler.net/"
ranBefore = False

def help (run):
    if run == False:
        print("Welcome to my interactive Project Euler Answer dispencer!\n") 
        print("Type the number of the problem you want the answer to. ")
        print("EX: \"one\" \n")
        print("Enter \"total\" to show total number of problems completed.\n")
        print("Enter \"Euler\" to visit Project Euler homepage.\n")
        print("Enter \"exit\" to exit.")

while not exit:
    
    help (ranBefore)
    selection = input(']> ')
    if selection.lower() == "exit":
        exit = True
    elif selection.lower() == "total":
        webbrowser.open_new_tab(PROOFURL)
    elif selection.lower() == "euler":
        webbrowser.open_new_tab(EURLER)
        
    else:
        selectionEnd = selection
        selection = "euler."
        selection = selection + selectionEnd
        selectionEnd = "()"
        selection = selection + selectionEnd
        '''I understand the risks of eval(), and in this case, found them 
           to be relitively negligable.'''
        eval(selection.lower())

    ranBefore = True