import random
#from formations.dict_formations import Formations
import constants.constants


class ChooseThings:

    def __init__(self):
        #self.formations = Formations()
        pass

    def choose_random_question(self, dictionary_element):
        length_dict = len(dictionary_element)
        chosen_question = random.randrange(0,length_dict,1)
        return chosen_question

    def choose_option(self):
        print("Please choose one option")
        print("1. I want to choose a letter/number")
        print("2. I want to give the definition")
        x = int(input(""))
        while x>2 or x<1:
            print("Not a correct option. Choose again")
            x = int(input(""))
        return x

    def choose_character(self):
        print("Please introduce a letter or a number", end="  ")
        x = input(" ")
        while not x.isalnum() and len(x)>1:
            print("Not correct character")
            x = input(" ")
        return x

    def choose_definition(self):
        x = input("Introduce the unknown word ")
        return x

    def create_hunger(self):
        matrix_hung = constants.constants.MATRIX_HUNG
        #create front row
        matrix_hung[0][0]= '-'; matrix_hung[0][1] = '-'; matrix_hung[0][2] = '-';  matrix_hung[0][3] = '-'; matrix_hung[0][4] = '-';matrix_hung[0][5]='-'
        #create first column
        matrix_hung[1][1] = '|';matrix_hung[2][1] = '|';matrix_hung[3][1] = '|';matrix_hung[4][1] = '|';matrix_hung[5][1] = '|';matrix_hung[6][1] = '|';matrix_hung[7][1]="|";matrix_hung[8][1]="|"
        #create body
        matrix_hung[1][5]=' |';matrix_hung[2][5]='O';matrix_hung[3][5]='+';matrix_hung[4][5]='+';matrix_hung[5][5]=' +';matrix_hung[6][5]=' +';matrix_hung[7][5]='+'
        #create arms and legs
        matrix_hung[4][4]='-';matrix_hung[4][3]='-';matrix_hung[5][3]='|';matrix_hung[4][6]='-';matrix_hung[4][7]='-';matrix_hung[5][7]=' |';matrix_hung[7][3]='-';matrix_hung[7][4]='-';matrix_hung[8][3]='|';matrix_hung[7][6]='-';matrix_hung[7][7]='-';matrix_hung[8][7]='  |'
        for i in range(0, len(matrix_hung)):
            for j in range(0, 8):
                print(matrix_hung[i][j], end=" ")
            print()








