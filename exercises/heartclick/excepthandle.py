import sys
def print_and_wait(type,value,traceback):
    sys.__excepthook__(type,value,traceback)
    raw_input("Press <enter> to close: ")
sys.excepthook = print_and_wait

raise RuntimeError("Moo")
