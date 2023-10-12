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
  aaron_goodlund = Person('Aaron Goodlund', True)
  ajaydeep_singh = Person('Ajaydeep Singh', True)
  alonso_delatorre = Person('Alonso De La Torre', True)
  angel_ramirez = Person('Angel Ramirez', True)
  ava_brady = Person('Ava Brady', False)
  aye_myat_noe_khin = Person('Aye Myat Noe Khin', True)
  brandon_nguyen = Person('Brandon Nguyen', True)
  danica_galang = Person('Danica Galang', True)
  diego_serrano = Person('Diego Serrano', True)
  evan_callejo = Person('Evan Callejo', False)
  gary_kane = Person('Gary Kane', False)
  harmanjot_singh = Person('Harmanjot Singh', False)
  hector_yabes = Person('Hector Yabes', False)
  isabel_santoyogarcia = Person('Isabel Santoyo-Garcia', True)
  jenica_chu = Person('Jenica Chu', True)
  jomel_sotelo = Person('Jomel Sotelo', True)
  jose_vasquez = Person('Jose Vasquez', False)
  katy_chan = Person('Katy Chan', True)
  kevin_esquivel = Person('Kevin Esquivel', False)
  keyur_maru = Person('Keyur Maru', True)
  mansoor_ali = Person('Mansoor Ali', False)
  mia_brady = Person('Mia Brady', False)
  oscar_lu = Person('Oscar Lu', True)
  phong_ho = Person('Phong Ho', True)
  prabhnoor_kaur = Person('Prabhnoor Kaur', True)
  ricardo_torres = Person('Ricardo Torres', True)
  sasha_saaed = Person('Sasha Saaed',True)
  sheridan_lynch = Person('Sheridan Lynch', True)
  tony_tran = Person ('Tony Tran' ,True)
  wei_chong = Person('Wei Chong', True)
  william_lorence = Person('William Lorence', False)


  # List of people in our class (alphabetical order by first name)
  # Removed and merged the duplicate peer list. -SL
  peers = [ aaron_goodlund, ajaydeep_singh, alonso_delatorre, ava_brady, aye_myat_noe_khin, brandon_nguyen, danica_galang, diego_serrano, evan_callejo, gary_kane, harmanjot_singh, isabel_santoyogarcia, jenica_chu, jomel_sotelo,jose_vasquez, katy_chan, 
kevin_esquivel, keyur_maru, mansoor_ali, mia_brady, phong_ho, prabhnoor_kaur, ricardo_torres, sasha_saaed, sheridan_lynch, wei_chong, william_lorence]

  # Print out people in our class
  print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
  print("Peers: %s" % peers)

  # Logic to see who likes pineapple pizza (alphabetical order by first name)
  
  if aaron_goodlund.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % aaron_goodlund.name)
  else:
      print("%s DOES NOT like pineapple pizza" % aaron_goodlund.name) 
  
  if ajaydeep_singh.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % ajaydeep_singh.name)
  else:
      print("%s DOES NOT like pineapple pizza" % ajaydeep_singh.name)
  
  if alonso_delatorre.likes_pineapple_pizza:
    print("%s likes pineapple pizza" % alonso_delatorre.name)
  else:
    print("%s DOES NOT like pineapple pizza" % alonso_delatorre.name)
  
  if ava_brady.likes_pineapple_pizza:
    print("%s likes pineapple pizza" % ava_brady.name)
  else:
    print("%s DOES NOT like pineapple pizza" % ava_brady.name)
    
  if aye_myat_noe_khin.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % aye_myat_noe_khin.name)
  else:
      print("%s DOES NOT like pineapple pizza" % aye_myat_noe_khin.name)

  if brandon_nguyen.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % brandon_nguyen.name)
  else:
      print("%s DOES NOT like pineapple pizza" % brandon_nguyen.name)

  if danica_galang.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % danica_galang.name)
  else:
      print("%s DOES NOT like pineapple pizza" %danica_galang.name)
      
  if diego_serrano.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % diego_serrano.name)
  else:
      print("%s DOES NOT like pineapple pizza" %danica_galang.name)

  if evan_callejo.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % evan_callejo.name)
  else:
      print("%s DOES NOT like pineapple pizza" % evan_callejo.name)
      
  if gary_kane.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % gary_kane.name)
  else:
      print("%s DOES NOT like pineapple pizza" % gary_kane.name)
      
  if harmanjot_singh.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % harmanjot_singh.name)
  else:
      print("%s DOES NOT like pineapple pizza" % harmanjot_singh.name)
   
  if hector_yabes.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % hector_yabes.name)
  else:
      print("%s DOES NOT like pineapple pizza" % hector_yabes.name)

  if isabel_santoyogarcia.likes_pineapple_pizza:
    print("%s likes pineapple pizza" % isabel_santoyogarcia.name)
  else:
    print("%s DOES NOT like pineapple pizza" % isabel_santoyogarcia.name)
 
  if jenica_chu.likes_pineapple_pizza:
    print("%s likes pineapple pizza" % jenica_chu.name)
  else:
    print("%s DOES NOT like pineapple pizza" % jenica_chu.name)

  if jomel_sotelo.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % jomel_sotelo.name)
  else:
      print("%s DOES NOT like pineapple pizza" % jomel_sotelo.name)

  if jose_vasquez.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % jose_vasquez.name)
  else:
      print("%s DOES NOT like pineapple pizza" % jose_vasquez.name)

  if katy_chan.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % katy_chan.name)
  else:
      print("%s DOES NOT like pineapple pizza" % katy_chan.name)  

  if kevin_esquivel.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % kevin_esquivel.name)
  else:
      print("%s DOES NOT like pineapple pizza" % kevin_esquivel.name) 

  if keyur_maru.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % keyur_maru.name)
  else:
      print("%s DOES NOT like pineapple pizza" % keyur_maru.name)
      
  if mansoor_ali.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % mansoor_ali.name)
  else:
      print("%s DOES NOT like pineapple pizza" % mansoor_ali.name)
      
  if mia_brady.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % mia_brady.name)
  else:
      print("%s DOES NOT like pineapple pizza" % mia_brady.name)
  
  if oscar_lu.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % oscar_lu.name)
  else: 
      print("%s DOES NOT like pineapple pizza" % oscar_lu.name)

  if phong_ho.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % phong_ho.name)
  else:
      print("%s DOES NOT like pineapple pizza" % phong_ho.name)
  
  if prabhnoor_kaur.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % prabhnoor_kaur.name)
  else:
        print("%s DOES NOT like pineapple pizza" % prabhnoor_kaur.name)

  if ricardo_torres.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % ricardo_torres.name)
  else:
      print("%s DOES NOT like pineapple pizza" % ricardo_torres.name)
      
  if sasha_saaed.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % sasha_saaed.name)
  else:
      print("%s DOES NOT like pineapple pizza" % sasha_saaed.name)

  if sheridan_lynch.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % sheridan_lynch.name)
  else:
      print("%s DOES NOT like pineapple pizza" % sheridan_lynch.name) 

  if tony_tran.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % tony_tran.name)
  else:
      print("%s DOES NOT like pineapple pizza" % tony_tran.name)

  if wei_chong.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % wei_chong.name)
  else:
      print("%s DOES NOT like pineapple pizza" % wei_chong.name)

  if william_lorence.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % william_lorence.name)
  else:

      print("%s DOES NOT like pineapple pizza" % william_lorence.name)

  

if __name__ == "__main__":
  main()
