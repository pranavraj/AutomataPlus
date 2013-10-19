'''
Created on 08-Dec-2010

@author: Naman
'''
import Game_Pumping
from Exceptions import PumpingLemma_Exception

class AnBn(Game_Pumping.pumping_game) :
    
    lang = " AnBn "

    def get_word( self ):

        if(self.choice==1):
            temp = self.n
            self.word = 'a'*temp + 'b'*temp

        self.length = len(self.word)
        return self.word


    def start( self ):

        if(self.flag == 1):
            return self.pump_String()

        else:
            
            Message = ""
            word_check = self.Word_x + (self.Word_y * self.k) + self.Word_z
            Message = Message + " Concatinating " + self.Word_x + " + " + self.Word_y * self.k + " + " + self.Word_z + " = " + word_check
            if ( self.in_Lang(word_check) == False ):
                Message = Message +'\n' + " You Won as the word is not in language" + self.lang
                return Message
                
            else:
                Message = Message +'\n' +  "You Lost as the word is in the language" + self.lang
                return Message

        
    def pump_String( self ):
        #Decide a value of k when player starts. If a word is not in the language then player wins
        Message = ''
        for val in range(self.n+2):

            temp = self.Word_x + self.Word_y * val + self.Word_z

            if(self.in_Lang(temp)==False):

                Message = Message + " Concatinating " + self.Word_x + " + " + self.Word_y * val + " + " + self.Word_z + " = " + temp

                Message = Message + '\n' + " You lost as the word "+ temp + " is not in the language " + self.lang

                return Message

        return "You won as no matter the pumping values word stays in the language " + self.lang

    
    def in_Lang(self,word_check):
        count_a = word_check.count('a')
        if(word_check == ('a'*count_a + 'b'*count_a)):
            return True
        else:
            return False

