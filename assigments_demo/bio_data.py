"""
1) Design a class to take bio data:

    Consists of following Information

    a) Your name
    b) Your age
    c) Your school name
    d) Your Father name and occupation
    e) Your Mother name and occupation
    f) Your Hobbies
    g) Your Friends Name
    h) Your ambition

   Following Operation need to be done

  1) Print the instance it should provide the your details

  2) create a instance method to_json() it should return dictionary of key and    values

  3) Create a class method from_json(< params >) dictionary and return the object of the bio data

   if any of the key is missing then you throw custom exception stating message following keys are mission with key names
"""


# Create for bio data class
class BioDataException(Exception):
    """
    This class provide custom exception for bio data class
    """

    # Override constructor to accept message
    def __init__(self, message):
        """
        Instance required message
        :param message: This message for throwing error
        """
        super().__init__(message)


"""
Design a class to take bio data:

    Consists of following Information

    a) Your name
    b) Your age
    c) Your school name
    d) Your Father name and occupation
    e) Your Mother name and occupation
    f) Your Hobbies
    g) Your Friends Name
    h) Your ambition
    
    1) Print the instance it should provide the your details

  2) create a instance method to_json() it should return dictionary of key and    values

  3) Create a class method from_json(< params >) dictionary and return the object of the bio data
  
   if any of the key is missing then you throw custom exception stating message following keys are mission with key names
   
"""


# Step 2: Create a class for designing a bio data
class BioData:
    """
    This class helps us to template bio data
    """

    # Override constructor to initialize all the values
    def __init__(self):
        """
        Overridden constructor method to initialize all the bio data value
        """
        #  a) Your name
        #  b) Your age
        #  c) Your school name
        #  d) Your Father name and occupation
        #  e) Your Mother name and occupation
        #  f) Your Hobbies
        #  g) Your Friends Name
        #  h) Your ambition
        pass

    def __str__(self) -> str:
        """
        This method returns string representation of our class
        :return: representation string
        """
        pass

    def to_json(self):
        """
        This method returns json string from the values
        :return: json string from bio data
        """
        pass

    @staticmethod
    def from_json(param: dict):
        """
        This method helps to create a object from the dictionary
        :param param: dictionary param also called as json
        :return: created object from json
        """
        pass

