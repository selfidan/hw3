# Your name: Selin Fidan
# Your student id: 02064320
# Your email: selfidan@umich.edu
# List who you have worked with on this homework: Julia Couch and Michelle Karis

# import the random module for use in this program
import random

# Create the class Animal_Fact_Generator
class Animal_Fact_Generator:
    # create the constructor (__init__) method
    # it takes as input:
    #   a list of possible facts and
    #   a list of animals those facts belong to
    # it sets this object's fact_list (instance variable) to the passed list of facts
    # it sets this object's animal_list (instance variable) to the passed list of animals
    # it sets this object's fact_history_list to an empty list (instance variable)

    def __init__(self, facts, animals):
        self.fact_list = facts
        self.animal_list = animals 
        self.fact_history_list = []
    
    # create the __str__ method
    # It should return a string with all animals
    # in animal_list separated by commas
    # For example : "elephant, cat, wolf, giraffe, panda, tiger"

    def __str__(self):
       # return ("Animals: {}".format(self.animal_list))
        return (",").join(self.animal_list)

    # create the random_fact method
    # it randomly picks an index from 0 to the number of items in the fact_list minus one
    # it adds that index to the end of the fact_history_list
    # it returns a string combining the fact and the animal at that index in this object's fact_list
    # "fact - animal"

    def random_fact(self):
        indx = random.randint(0, len(self.fact_list) - 1)
        self.fact_history_list.append(indx)
        return self.fact_list[indx] + ' - ' + self.animal_list[indx]
        #output = ""
        #for fact in rand.range(self.fact_list[0:-1]):
        #    output += fact.facts + "-"
        #return output



    # create the get_fact_for_animal method
    # it takes as input:
    #    the name of the animal
    # if there exists a fact for that animal, it returns the fact
    # else it returns "Sorry! I do not have any facts for {name_of_animal}"

    def get_fact_for_animal(self, animal_name):
       if animal_name in self.animal_list:
            return "Sorry! I do not have any facts for {}".format(animal_name)
        else:
#            return self.fact_history_list[animal_name]



    # create the print_history method
    # prints "[index] fact - animal" for each of the indicies in the fact_history_list
    # from the first to the last with each on a single line
    # it does not return anything!
    
    def print_history(self):
        for fact in self.fact_history_list:
            print() 

    # EXTRA POINTS
    # create the generate_n_facts method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random fact n times
    # then returns the index and length of the longest consecutive run for an animal index
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 facts generated are [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4"





def main():
    # You are welcome to replace the facts and names with your favorite facts and animals
     fact_list = ["These animals are the only animals that can't jump.", \
     "This animal's tail contains nearly 10 percent of all the bones in its body.", \
     "This animal can go for more than a week without eating.", \
     "This animal's heart weighs about 25 pounds.", \
     "This animal eats half the day.", \
     "These animals are the only big cats that can't roar."]

     animal_list = ["elephant", "cat", "wolf", "giraffe", "panda", "tiger"]

     print("Testing the first animal_fact_generator:")
     fact_bot = Animal_Fact_Generator(fact_list, animal_list)
     print("\nGenerating a random fact")
     print("\nfact : " + fact_bot.random_fact())
     print("\nTesting __str__ method")
     print(fact_bot.__str__())
     print("\nTesting that it can get fact for given animal : panda")
     print(fact_bot.get_fact_for_animal("panda"))
     print("\nPrinting the full history:")
     fact_bot.print_history()

     print("\n===================================================================================================\n")

    #Create another fact-generator
     print("Testing the second animal_fact_generator:")
     fact_bot2 = Animal_Fact_Generator(fact_list, animal_list)

     print("\nTesting when no facts have been generated yet")
     print(fact_bot2.print_history())

     print("\nGetting a cat fact")
     print("\nfact : " + fact_bot.get_fact_for_animal("cat"))

     print("\nGetting a dog fact")
     print("\nfact : " + fact_bot.get_fact_for_animal("dog"))

     print("\nGenerating five facts randomly")
     for x in range(5):
         print("fact : " + fact_bot2.random_fact())
     print("\nPrinting the full history:")
     fact_bot2.print_history()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
     print("\nTesting generate_n_facts method with 200 facts")
     print(fact_bot2.generate_n_facts(200))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
