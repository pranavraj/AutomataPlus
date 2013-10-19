'''
Created on 07-Dec-2010

@author: Naman
'''
import random

class pumping_game :

    choice = 0  # if choice = 1 user starts else 2 then computer
    word = ""    # word w that will be tested
    n = 0        # number n for a^n_b^n
    x = 0
    y = 0     # to reenter if it is input as 1
    z = 0
    Word_x = ""
    Word_y = ""
    Word_z = ""
    k = 0
    length = 0
    flag = 0     # if it is 1 computer has to decide the correct string

    @staticmethod
    def set_xy( ) :

        pumping_game.x = random.randrange(0,pumping_game.n-1)
        pumping_game.y = random.randrange(1,pumping_game.n-pumping_game.x)


    @staticmethod
    def set_z( ) :

        pumping_game.z = pumping_game.length - pumping_game.x - pumping_game.y


    @staticmethod
    def set_WordXYZ( ) :

        pumping_game.Word_x = pumping_game.word[0:pumping_game.x]
        pumping_game.Word_y = pumping_game.word[pumping_game.x :pumping_game.x+pumping_game.y]
        pumping_game.Word_z = pumping_game.word[pumping_game.y+pumping_game.x:]


    @staticmethod
    def set_k( ) : pumping_game.flag = 1


    @staticmethod
    def set_n( ) : pumping_game.n = random.randint( 3 , 10 )
