from chooser.chooser import ChooseThings
from formations.dict_formations import Formations
import time

class Executer:

    def __init__(self):
        self.chooser = ChooseThings()
        self.formations = Formations()

    # def replace_characters(self, list_index, chosen_string, new_character):
    #     result=""
    #     for i in range(0, len(chosen_string)):
    #         if i in list_index:
    #             result+=new_character
    #         else:
    #             result+=chosen_string[i]
    #     return result

    def replace_characters(self, list_index, chosen_string, new_character):
        for index in list_index:
            chosen_string= chosen_string[:index]+new_character+chosen_string[index+1:]
        return chosen_string





    def create_execution(self):
        nr_mistakes =0
        nr_permited_mistakes =4
        list_substitutions = []
        list_chosen_characters = [];list_wrong_characters =[]
        game_dictionary = self.formations.create_dictonary()
        result, masked_result, question = self.formations.create_resultSet(game_dictionary)
        splitted_list_questions = question.split(".")
        marked_question = splitted_list_questions[1]
        print("""Welcome to the "Spanzuratoarea" game""" )
        time.sleep(1.5)
        while(True):
            if(masked_result==result):
                print(masked_result)
                print("Congratiulations! The word is correct")
                break
            if(nr_mistakes>3):
                print("Sorry you lost the game. Too many wrong characters or bad definition attempts")
                time.sleep(1)
                self.chooser.create_hunger()
                time.sleep(1)
                print("The solution is: ", result)
                break
            print(marked_question)
            print(masked_result)
            if len(list_wrong_characters)>0:
                print("Characters used: ", list_wrong_characters)
            player_option = self.chooser.choose_option()
            if(player_option==1):
                introduced_character = self.chooser.choose_character().upper()
                while introduced_character in list_chosen_characters:
                    print("You already chose this letter/number. Choose again")
                    introduced_character = self.chooser.choose_character()
                if introduced_character in result:
                    for i in range(0, len(result)):
                        if result[i]==introduced_character:
                            list_substitutions.append(i)
                    masked_result= self.replace_characters(list_substitutions,masked_result,introduced_character)
                    list_chosen_characters.append(introduced_character)
                    list_substitutions.clear()
                    time.sleep(1)
                if introduced_character not in result:
                    print("Sorry! The word does not contain this letter/number!")
                    nr_mistakes+=1
                    if nr_mistakes<4:
                        print("You have {} wrong attempts left before you are hung!".format(nr_permited_mistakes-nr_mistakes))
                    list_wrong_characters.append(introduced_character)
                    time.sleep(1)
            if player_option==2:
                introduced_definition = self.chooser.choose_definition().upper()
                if introduced_definition==result:
                    print(result)
                    time.sleep(1)
                    print("Congratiulations! Your solution is correct!")
                    break
                else:
                    nr_mistakes+=1
                    if nr_mistakes<4:
                        print("The solution is not the correct one")
                        print("You have {} wrong attempts left before you are hung!".format(nr_permited_mistakes - nr_mistakes))
                    time.sleep(1)






