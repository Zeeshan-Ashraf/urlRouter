class InvalidInputException(Exception):
    def __init__(self, inp):
        print("invalid input: ",inp)