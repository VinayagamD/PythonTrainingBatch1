class Bmw:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']

        # A normal print function

    def out_models(self):
        print('These are the available models for BMW')
        for model in self.models:
            print('\t%s ' % model)


# Python code to illustrate the Module
class Audi:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['q7', 'a6', 'a8', 'a3']

        # A normal print function

    def out_models(self):
        print('These are the available models for Audi')
        for model in self.models:
            print('\t%s ' % model)


# Python code to illustrate the Module
class Nissan:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue']

        # A normal print function

    def out_models(self):
        print('These are the available models for Nissan')
        for model in self.models:
            print('\t%s ' % model)
