#MadLib.py
#Name: Lukas Gibbs
#Date: 8/28/24
#Assignment: MadLib1

def main():
  print("Madlib")
  #Ask user for words
  name1 = input("Please enter any name: ")
  word1 = input("Please enter a silly word: ")
  adjective1 = input("Please enter an adjective. An adjective is a word that modifies a noun. : " )
  noun1 = input("Please enter a noun. A noun is a person, place, or thing. : ")
  adjective2 = input("Please enter another adjective: ")
  relative1 = input("Please enter a relative. Please use their relation to you and not their name. For example, grandma and not Suzie. : ")
  adjective3 = input("Please enter another adjective: ")
  verb1 = input("Please enter a verb. A verb is an action. : ")
  adjective4 = input("Please enter another adjective: ")
  adjective5 = input("Please enter another adjective: ")
  #Print the story with the user supplied words.
  print("Hello my name is astronaut", name1,"." )
  print("I am on my way to planet", word1,"." )
  print("I am very",adjective1, "about the trip but I will miss my" ,noun1,".")
  print("I have heard that the atmosphere there is", adjective2,".")
  print("Luckily my" , relative1, "packed me a jacket to keep me", adjective3,".") 
  print("When I land on the planet I will" , verb1,"for joy.")
  print("I am",adjective4,"to walk on another planet.")
  print("I could not be more",adjective5,"for this trip.")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
