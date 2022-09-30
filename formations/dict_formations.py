import constants.constants
import os
from chooser.chooser import ChooseThings
import re

class Formations:

    def __init__(self):
        self.list_sentences =[]
        self.chooser = ChooseThings()

    def create_dictonary(self):
        game_dict =dict()
        global quiz
        try:
            file_path = constants.constants.OUTPUT_PATH
            os.chdir(file_path)
            file_name = constants.constants.FILE_NAME
            quiz = open(file=os.path.join(file_path,file_name), mode="r", encoding="utf-8")
            for text in quiz:
                self.list_sentences.append(text)
            for i in range (0, len(self.list_sentences)):
                if(self.list_sentences[i].__contains__('\n')):
                    self.list_sentences[i]= self.list_sentences[i][:-1] # "\n' practic este un singur caracter
            #//create the dictionary now
            for i in range (0,len(self.list_sentences)-1,2):
                game_dict.update({self.list_sentences[i]:self.list_sentences[i+1]})
            return game_dict
        except:
            raise FileNotFoundError
        finally:
            quiz.close()

    def create_resultSet(self, game_dict):
        result =""
        chosen_question =""
        for key in game_dict:
            game_dict[key]= game_dict[key].upper()
        question =self.chooser.choose_random_question(game_dict)
        for key in game_dict:
            if str(question) in key:
                result=game_dict[key]
                chosen_question= key
                break
        masked_result = result
        for character in masked_result:
          if character!=' ':
            masked_result = masked_result.replace(character,'_')
        return result, masked_result, chosen_question













