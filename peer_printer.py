# Fall 2023 CSC 131-06
# Welcome to Coding using Git! We all must edit this same file.

# Create a Person object under 'Person objects'.
# Keep the list of persons in alphabetical by first name order. Example:
# john_doe = Person('John Doe', True)

# Update peers list with your Person object alphabetical order by
# first name. This list will increase as more students make commits.
# Example: peers = [fiz_ban, foo_bar, john_doe]

# Add an if-statement to print a message on whether you like pineapple pizza.
# Keep the if-statements alphabetical order by first name.
# See my example.

# Run the program and make sure it works!
# You can use a simple online IDE if you don't have a Python3 environment
# Example: https://ideone.com/l/python-3

COURSE = ['CSC 131-06']
SEMESTER = ['Fall 2023']


class Person:
    '''
    This class is the Person class. It represents basic person info.
    Attributes
    ----------
    name : str
        a string for a person's full name (first and last) used to print
    likes_pineapple_pizza : bool
        whether this person likes pineapple on pizza or not
    '''
    # Python constructor to initialize attributes (fields in Java)

    def __init__(self, name: str, likes_pineapple_pizza: bool):
        self.name = name
        self.likes_pineapple_pizza = likes_pineapple_pizza

    # Special Python method used to represent a class's objects as a string
    def __repr__(self):
        return self.name


def main():
    # Person objects (alphabetical order by first name)
<<<<<<< HEAD
    aaron_goodlund = Person('Aaron Goodlund', True)
=======
    aye_myat_noe_khin = Person('Aye Myat Noe Khin', True)
>>>>>>> 696db3d4bdd5973393f6410d491cabed7aad3922
    danica_galang = Person('Danica Galang', True)
    gary_kane = Person('Gary Kane', False)
    isabel_santoyogarcia = Person('Isabel Santoyo-Garcia', True)
    jomel_sotelo = Person('Jomel Sotelo', True)
    mansoor_ali = Person('Mansoor Ali', True)
    mia_brady = Person('Mia Brady', False)


    # List of people in our class (alphabetical order by first name)
<<<<<<< HEAD
    peers = [aye_myat_noe_khin, danica_galang, gary_kane, isabel_santoyogarcia, jomel_sotelo, mansoor_ali, mia_brady]
=======
<<<<<<< HEAD
    peers = [aaron_goodlund, danica_galang, gary_kane, isabel_santoyogarcia, jomel_sotelo, mia_brady]
=======
    peers = [aye_myat_noe_khin, danica_galang, gary_kane, isabel_santoyogarcia, jomel_sotelo, mia_brady]
>>>>>>> 696db3d4bdd5973393f6410d491cabed7aad3922
>>>>>>> 0c4038ab320b68e32b1568de335e968244ec91a7

    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
<<<<<<< HEAD
    if aaron_goodlund.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % aaron_goodlund.name)
    else:
        print("%s DOES NOT like pineapple pizza" %danica_galang.name)    
=======
    if aye_myat_noe_khin.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % aye_myat_noe_khin.name)
    else:
        print("%s DOES NOT like pineapple pizza" % aye_myat_noe_khin.name)

>>>>>>> 696db3d4bdd5973393f6410d491cabed7aad3922
    if danica_galang.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % danica_galang.name)
    else:
        print("%s DOES NOT like pineapple pizza" %danica_galang.name)
    if gary_kane.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % gary_kane.name)
    else:
        print("%s DOES NOT like pineapple pizza" % gary_kane.name)

    if isabel_santoyogarcia.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % isabel_santoyogarcia.name)
    else:
        print("%s DOES NOT like pineapple pizza" % isabel_santoyogarcia.name)

    if jomel_sotelo.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % jomel_sotelo.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jomel_sotelo.name)
        
    if mansoor_ali.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % mansoor_ali.name)
    else:
        print("%s DOES NOT like pineapple pizza" % mansoor_ali.name)
        
    if mia_brady.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % mia_brady.name)
    else:
        print("%s DOES NOT like pineapple pizza" % mia_brady.name)




if __name__ == "__main__":
    main()
