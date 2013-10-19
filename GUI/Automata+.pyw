__version__ = "1.0.0"


#Library Modules
import platform
import webbrowser
import shutil
import os
import sip
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Project Interface Modules
import MainWindow                   # main window of options - Automata,Grammar,Pumping lemma
import AutomataInterface            # functions of Automata
import GrmWizard                    # functions of Grammar
import GrmInterface                 # first page of Grammar
import GrEnterWord
import GrDisplay
import GrmInteractive
import RPLInterface                 # regular pumping lemma interface
import WizardPageOne                # taking the automata in text form
import WizardPageTwo                # displaying the automata
import RegExpInterface                 # first page of regular expression
import DispInterface                # drawing the image to QGraphicsScene
import RPLPageOne                   # page one of RPL
import RPLPageTwo                   # page two of RPL
import RPLEnterN                    # input N
import RPLEnterWord                 # input Word
import RPLEnterXYZ                  # input X,Y,Z
import RPLEnterK                    # input K
import AutEnterWord
import MoreInfo

#Project Core Modules
import Automata.Display_Automata_StateList as DISP
import Automata.Display_Automata_Dictionary as DISPdict
import Automata.Display_NFAtoDFA_StateList as DISP_NFA
import Automata.StateList_To_File as Conv2File
import Automata.AutomataRead as AutomataRead
import Regular_Expression.reTOnfa as RegExp
import Automata.Automata_complement as Comp
import Automata.Automata_reverse as Rev
import Automata.MinDFA as Min
import Automata.Detect_Nondeterminism as Non_Deter
import Automata.Detect_epsilon as Det_EPS
import Automata.Dfatogrammer as DFA2Gram
import Automata.NFAtoDFA as NFA_Convert
import Automata.Direct_word_accept_NFA as Word_Acc
import Automata.StateByState_Word_ACcept_NFA as State_Word_Acc
import Automata.State_Elimination as State
import Automata.Empty_language as Empty
import Automata.remove_Useless_States as Rem_Useless
import Automata.remove_Unreachable as Reachable
import Automata.ProductAutomata as Prod
import Automata.readmyfile as Dict2State
import Grammar.GrammarRead as GrammarRead
import Grammar.grammar_type as Type_Gr
import Grammar.grammar_to_PDA as Gr2PDA
import Grammar.identify_Left_Recursion as LRecurse
import Grammar.remove_Epsilon as Rem_Eps
import Grammar.CNF_Converter as CNF
import Grammar.RightLineartoFSA as Gr2FSA
import Grammar.CYK_Parser as CYK
import Grammar.grammar_reachable as ReachableGr
import Grammar.Derivation as Derive
from Regular_Pumping_Lemma.Game_Pumping import pumping_game as GPump
from Regular_Pumping_Lemma.AnBn import AnBn
from Regular_Pumping_Lemma.w_wreverse import WWr
from Regular_Pumping_Lemma.a_greater_than_b import AgB



class MainWin( QMainWindow ):

    HELP = "Default Help Message"
    MORE = "Default More Message"

    """
    CHOICE_FLAG :
    1 : AUTOMATA
    2 : GRAMMAR
    3 : REGULAR EXPRESSION
    4 : PUMPING LEMMA
    """
    CHOICE_FLAG = 0

    """
    AUTOMATA_NUM :
    1 : AUTOMATA ONE
    2 : AUTOMATA TWO
    """
    AUTOMATA_NUM = 0

    def __init__( self , parent=None ) :

        QWidget.__init__( self , parent )
        self.setWindowFlags( Qt.WindowMinimizeButtonHint )
        self.MainAppWin()


    def MainAppWin( self ) :

        self.UI = MainWindow.Ui_MainWindow()
        self.UI.setupUi( self )
        
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > An <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' > Automaton <font size= 5 face= 'Georgia, Arial' color= 'black ' >is a Finite State Machine that comprises of states and input letters and processes an input according to the transitions.<br> <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >Grammar <font size= 5 face= 'Georgia, Arial' color= ' black ' > is a set of rules for a given language.<br> A <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' > Regular Expression, <font size= 5 face= 'Georgia, Arial' color= ' black ' >often called a pattern, is an expression that describes a set of strings. <br> <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >Regular Pumping Lemma <font size= 5 face= 'Georgia, Arial' color= ' black ' >says that all sufficiently long words in a regular language may be pumped - that is, have a middle section of the word repeated an arbitrary number of times - to produce a new word which also lies within the same language.<br> "
        self.HELP = " <html> <body> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Select any option that you want to choose <\font><\body><\html>"

        QObject.connect( self.UI.actionAbout , SIGNAL("triggered()") , self.AboutCallback )
        QObject.connect( self.UI.actionExit , SIGNAL("triggered()") , self.ExitCallback )
        QObject.connect( self.UI.actionReport_a_Bug , SIGNAL("triggered()") , self.BugReportCallback )
        
        QObject.connect( self.UI.AutButton , SIGNAL("clicked()") , self.AutCallback )
        QObject.connect( self.UI.GrButton , SIGNAL("clicked()") , self.GrCallback )
        QObject.connect( self.UI.ReButton , SIGNAL("clicked()") , self.ReCallback )
        QObject.connect( self.UI.PLButton , SIGNAL("clicked()") , self.PLCallback )
        
        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def ExitCallback( self ) :

        splash_pix = QPixmap( os.path.join( "ArtWork" , "AutPlusLogo.png" ) )
        splash = QSplashScreen( splash_pix , Qt.WindowStaysOnTopHint )
        splash.setMask( splash_pix.mask() )
        splash.show()
        AppInit.processEvents()

        time.sleep( 1 )
        self.destroy()
        
        sys.exit( 0 )


    def AboutCallback( self ) :

        QMessageBox.about( self , "About Automata+" ,

    """<b>Automata<sup>+</sup></b> v %s
    <p>Copyright &copy; 2010 .
    All rights reserved.
    <p>Automata+ provides tools for performing various operatons related to Formal Languages and Automata Theory.
    <br>
    <br>
    <br>
    <b><u>Developers :</u></b>
    <br>
    <i>Naman Kohli</i> ( 2009027 , <FONT color="blue">naman09027@iiitd.ac.in</FONT> )
    <br>
    <i>Swetank Kumar Saha</i> ( 2009049 , <FONT color="blue">swetank09049@iiitd.ac.in</FONT> )
    <br>
    <i>Pranav Raj</i> ( 2009032 , <FONT color="blue">pranav09032@iiitd.ac.in</FONT> )

    <p>Python %s on %s""" % ( __version__ , platform.python_version() , platform.system() )
                         )


    def BugReportCallback( self ) : webbrowser.open( "http://automataplusapp.appspot.com/" )


    def AutCallback( self ) :

        self.UI = WizardPageOne.Ui_MainWindow()
        self.UI.setupUi( self )

        QObject.connect( self.UI.actionOpen_Existing_Automata , SIGNAL("triggered()") , self.OpenCallback )

        self.CHOICE_FLAG = 1
        self.AUTOMATA_NUM = 1
        
        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Enter the automata in this format <br><br> NoofAlphabets(always including epsilon) NumberofStates <br> InitialStates in curly bracket ({0}) <br> Transitions per each alphabet in the form of {} where {-1} shows no transition and the first is always for epsilon eg. {-1} {0} {2} for DFA <br> AcceptingStates in curly brackets eg {1,2,3}<\font><\body><\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Please make sure that the DFA will have only one entry per bracket in the transitions and {-1} as first entry for epsilon in transitions. <br>For NFA add multiple transitions in the form {1,2,3}<\font><\body><\html>"

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.MainAppWin )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , lambda : self.NextCallback("TempAutomata.aut","InputAutomata.png") )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def GrCallback( self ) :

        self.UI = GrmWizard.Ui_MainWindow()
        self.UI.setupUi( self )
        
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >  Enter the grammar in the following format <br> First line will have all the states <br> Second line will have all the terminals <br> For each state mentioned above there is a corresponding rule given after in the format S -> SS|AB|0 <\font><\body><\html>"
        self.CHOICE_FLAG = 2
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The grammar attribute has a left side and a right side. <br>We will mainly be working with grammars having one state at the left side.<\font><\body><\html>"

        QObject.connect( self.UI.actionOpen_Existing_Grammar , SIGNAL("triggered()") , self.OpenGrmCallback )
        QObject.connect( self.UI.actionSave_Grammar , SIGNAL("triggered()") , self.SaveGrmCallback )

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.MainAppWin )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , self.FinishCallback )

        QObject.connect( self.UI.HelpButton_2 , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def SaveGrmCallback( self ) :

        SaveWin = QFileDialog()
        FileName = SaveWin.getSaveFileName( )
        shutil.copy( "TempGrammar.grm" , FileName )
        

    def OpenGrmCallback( self ) :

        OpenWin = QFileDialog()
        FileName = OpenWin.getOpenFileName( )

        OpenFile = open( FileName , "r" )

        self.UI.textEdit.setText( OpenFile.read().rstrip('\n') )


    def ReCallback( self ) :

        self.UI = RegExpInterface.Ui_MainWindow()
        self.UI.setupUi( self )

        self.UI.lineEdit.setFocus()
        self.UI.lineEdit.selectAll()

        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Enter a regular expression that you want. <br> You can enter <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >^* <font size= 5 face= 'Georgia, Arial' color= ' black ' >for 0 or more , <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >^+ <font size= 5 face= 'Georgia, Arial' color= ' black' >for atleast one , <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >.<font size= 5 face= 'Georgia, Arial' color= ' black ' > for concatination and <font size= 5 face= 'Georgia, Arial' color= ' dark blue ' >+<font size= 5 face= 'Georgia, Arial' color= ' black ' > as an or operator <\font><\body><\html>"
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Each operator is splitted down to a set of states according to the rules set.<\font><\body><\html>"
        self.CHOICE_FLAG = 3

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.MainAppWin )
        QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , self.RegExpCallback )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def PLCallback( self ) :

        self.UI = RPLPageOne.Ui_MainWindow()
        self.UI.setupUi( self )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Enter who will start the game of Pumping Lemma <bt> Your motive is to prove that the language is not regular that is there is a word which if pumped does not lies in the language<\font><\body><\html>"
        self.UI.radioButton.setChecked(1)
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >You will compete against the computer in the game.<br> Select here to choose who starts the game<\font><\body><\html>"
        self.CHOICE_FLAG = 4

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.MainAppWin )
        QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , self.PLWizard )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def FinishCallback( self ) :

        TempGrm = open( "TempGrammar.grm" , "w" )

        doc = self.UI.textEdit.document()
        block = doc.begin()
        TempGrm.write( block.text() )

        for i in range( 1, doc.blockCount() ):

           TempGrm.write('\n')
           block = block.next()
           TempGrm.write( block.text() )

        TempGrm.write('\n')
        TempGrm.close()
        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Select an option to work on the grammar entered <\font><\body><\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >For viewing the grammar entered you can click the desired button  <\font><\body><\html>"
        self.UI = GrmInterface.Ui_MainWindow()
        self.UI.setupUi( self )

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.GrCallback )
        QObject.connect( self.UI.AutButton , SIGNAL("clicked()") , self.GrCallbackOne )  # type of grammar
        QObject.connect( self.UI.GrButton , SIGNAL("clicked()") , self.GrCallbackTwo )  # grammar to pda
        QObject.connect( self.UI.AutButton_2 , SIGNAL("clicked()") , self.GrCallbackThree )  # identify left recursion
        QObject.connect( self.UI.GrButton_2 , SIGNAL("clicked()") , self.GrCallbackFour )  # remove epsilon
        QObject.connect( self.UI.AutButton_3 , SIGNAL("clicked()") , self.GrCallbackFive )  # grammar to CFG
        QObject.connect( self.UI.GrButton_6 , SIGNAL("clicked()") , self.GrCallbackSix )  # right linear to FSA
        QObject.connect( self.UI.AutButton_4 , SIGNAL("clicked()") , self.GrWordCallback )  # CYK algorithm
        QObject.connect( self.UI.GrButton_8 , SIGNAL("clicked()") , self.GrCallbackEight )  # unreachable and generating states
        QObject.connect( self.UI.AutButton_5 , SIGNAL("clicked()") , self.GrCallbackNine ) # Interact with Grammar

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def GrCallbackOne( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        Message = Type_Gr.Type_Grammar(Grammar)
        QMessageBox.information( self, ' Type Of Grammar ' , Message  )

    def GrCallbackTwo( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        Message = Gr2PDA.convert2PDA(Grammar)
        QMessageBox.information( self, ' PDA ' , Message  )


    def GrCallbackThree( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        dictionary = LRecurse.identify_leftrecur(Grammar)
        Message = ''
        for state in dictionary:
            if dictionary[state] == True:
                mssg = str(state) + " has left recursion \n"
                Message = Message + mssg
        if Message == '':
            Message = " No Recursion in the Grammar "
        QMessageBox.information( self, ' Left Recursion ' , Message  )


    def GrCallbackFour( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        Grammar = Rem_Eps.remove_Epsilon(Grammar)
        QMessageBox.information( self, ' Epsilon Free Grammar ' , str( Grammar.display() )  )


    def GrCallbackFive( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        try:
            Grammar = CNF.convert_CNF(Grammar)
            QMessageBox.information( self, ' Chomsky Normal Form ' , str( Grammar.display() )  )
        except:
            QMessageBox.information( self, ' Chomsky Normal Form ' , " Grammar is Unrestricted " )


    def GrCallbackSix( self ) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        Message = Grammar.display()
        QMessageBox.information( self, ' Convert to FSA ' , Message )


    def GrCallbackSeven( self , Check_Str) :

        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        Message , DATA = CYK.cyk_Grammar(Grammar,Check_Str)
        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > This implements bottom top parsing CYK and tells you if the word entered can be produced using the grammar given <\font><\body><\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The table shown is the one given in the book and tells you how the algorithm works <\font><\body><\html>"
        QMessageBox.information( self, ' Convert to FSA ' , Message )
        self.GrammarDisplay( DATA )
        QMessageBox.information( self, ' Convert to FSA ' , Message )


    def GrCallbackEight( self ) :

        Grammar = GrammarRead.read_grammar( "TempGrammar.grm" )
        Message = ReachableGr.reachable_Grammar(Grammar)
        QMessageBox.information( self, ' Reachability ' , Message )

    def GrCallbackNine( self ):

        self.UI = GrmInteractive.Ui_MainWindow()
        self.UI.setupUi( self )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Interact with the rules to derive your own strings using the productions of grammar<\font><\body><\html>"
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Choose the correct rule number that you want and then choose the correct location of the state that you want to change and click on apply rule to do changes<\font><\body><\html>"
        Grammar = GrammarRead.read_grammar('TempGrammar.grm')
        DispGrm , GrmDict = Derive.Show_Rules( Grammar )

        self.UI.textBrowser.setHtml( DispGrm )

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.GrWindow )
        QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , lambda: self.GrInteract(GrmDict) )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def GrInteract( self , GrmDict ):

        RuleNum = self.UI.spinBox.value()
        Location = self.UI.spinBox_2.value()
        String = str( self.UI.label.text() )

        RetString = Derive.Derivation( GrmDict , RuleNum , Location , String )

        self.UI.label.setText( RetString )


    def ReadAutomata( self , Filename , Imagename ) :

        TempAut = open( Filename , "w" )

        doc = self.UI.textEdit.document()
        block = doc.begin()
        TempAut.write( block.text() )

        for i in range( 1, doc.blockCount() ):

           TempAut.write('\n')
           block = block.next()
           TempAut.write( block.text() )

        TempAut.write('\n')
        TempAut.close()

        StateList,Accepted,Initial = AutomataRead.FileRead( Filename )
        DISP.display( StateList , Imagename )


    def NextCallback( self , Filename , Imagename ) :

        self.ReadAutomata( Filename , Imagename )
        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Observe that the automata given has now been made . Press Next to work on this automata <\font><\body><\html>"
        self.UI = WizardPageTwo.Ui_MainWindow()
        self.UI.setupUi( self )
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >If the picture is not clean or is not distinguishable please report it.<\font><\body><\html>"
        Canvas = QGraphicsScene()
        Canvas.addPixmap( QPixmap(Imagename) )
        self.UI.graphicsView.setScene( Canvas )

        self.UI.graphicsView.show()

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.AutCallback )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , self.AutOptionsCallback )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def AutOptionsCallback( self ) :

        self.UI = AutomataInterface.Ui_MainWindow()
        self.UI.setupUi( self )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Select a choice that you want<\font><\body><\html>"
        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.AutCallback )
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > For viewing the automata entered you can press the desired button and then come back.<\font><\body><\html>"
        QObject.connect( self.UI.AutButton , SIGNAL("clicked()") , self.CallbackOne )
        QObject.connect( self.UI.GrButton , SIGNAL("clicked()") , self.CallbackTwo )
        QObject.connect( self.UI.GrButton_3 , SIGNAL("clicked()") , self.CallbackThree )
        QObject.connect( self.UI.AutButton_2 , SIGNAL("clicked()") , self.CallbackFour )
        QObject.connect( self.UI.GrButton_2 , SIGNAL("clicked()") , self.CallbackFive )
        QObject.connect( self.UI.GrButton_4 , SIGNAL("clicked()") , self.CallbackSix )
        QObject.connect( self.UI.AutButton_3 , SIGNAL("clicked()") , self.CallbackSeven )
        QObject.connect( self.UI.GrButton_6 , SIGNAL("clicked()") , self.CallbackEight )
        QObject.connect( self.UI.GrButton_5 , SIGNAL("clicked()") , self.CallbackNine )
        QObject.connect( self.UI.AutButton_4 , SIGNAL("clicked()") , self.CallbackTen )
        QObject.connect( self.UI.GrButton_8 , SIGNAL("clicked()") , self.CallbackEleven )
        QObject.connect( self.UI.GrButton_7 , SIGNAL("clicked()") , self.CallbackTwelve )
        QObject.connect( self.UI.AutButton_5 , SIGNAL("clicked()") , self.CallbackThirteen )
        QObject.connect( self.UI.GrButton_10 , SIGNAL("clicked()") , self.CallbackFourteen )
        QObject.connect( self.UI.GrButton_9 , SIGNAL("clicked()") , self.CallbackFifteen )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def RegExpCallback( self ) :

        RegExpression = self.UI.lineEdit.text()
        Dictionary,MySET,String = RegExp.myfunc( str(RegExpression) )
        Dict2State.changeformat(Dictionary,['Q1'],'Q0')
        print "there" , Dictionary
        DISPdict.display( Dictionary , MySET , "OutputAutomata.png" )
        self.DrawAutomata()
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The given automata inputs the regular expression you entered. <\font><\body><\html>"
        self.MORE = String

    def CallbackOne( self ) :
        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        non_deter_list = Non_Deter.detect_Nondet(StateList)
        Messg = ''
        for state in non_deter_list:
            for transition in non_deter_list[state]:
                message = str(state) + " has non deterministic transition for letter " + str(transition)
                Messg = Messg + '\n' + message
        if Messg == '':
            Messg = " The Automaton has no multiple transitions for same letter "
        QMessageBox.information( self, ' Acceptance Information ' , Messg  )


    def CallbackTwo( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        eps_states = Det_EPS.detect_Epsilon(StateList)
        Messg = ''
        for state in eps_states:
            for transition in eps_states[state]:
                message = str(state) + " has epsilon transition to " + str(transition)
                Messg = Messg + '\n' + message
        if Messg == '':
            Messg = " The Automaton has no epsilon transition "
        QMessageBox.information( self, ' Acceptance Information ' , Messg  )


    def CallbackThree( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        StList,Accept,Init,String = Comp.automata_Complement( StateList,Accepted,Initial )
        Conv2File.convertfile(StList,Init,Accept,"Temp.aut")
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The Automata shown accepts the compliment of the automata given <\font><\body><\html>"
        self.MORE = String
        DISP.display( StList , "OutputAutomata.png" )
        self.DrawAutomata()


    def CallbackFour( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        StList,Accept,Init,String = Rev.automata_Reverse( StateList,Accepted,Initial )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The automata shown gives the reverse of automata provided <\font><\body><\html>"
        self.MORE = String
        DISP.display( StList , "OutputAutomata.png" )
        self.DrawAutomata()


    def CallbackFive( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        grammar = DFA2Gram.convert_Dfa2grammar(StateList)
        QMessageBox.information( self, ' Acceptance Information ' , str(grammar)  )


    def CallbackSix( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        StList , self.MORE = Min.MinimDFA( StateList,Accepted,Initial )
        DISP_NFA.display( StList , "OutputAutomata.png" )
        self.DrawAutomata()


    def CallbackSeven( self ) :
        """
        self.UI = WizardPageOne.Ui_MainWindow()
        self.UI.setupUi( self )

        self.CHOICE_FLAG = 1
        self.AUTOMATA_NUM = 2

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.AutOptionsCallback )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , lambda : self.InpChEqAut("TempAutomataOne.aut","InputAutomataOne.png") )
        """
        QMessageBox.information( self, ' Equivalence ' , " Coming Soon " )


    def CallbackEight( self ) :
        """
        self.UI = WizardPageOne.Ui_MainWindow()
        self.UI.setupUi( self )

        self.CHOICE_FLAG = 1
        self.AUTOMATA_NUM = 2

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.AutOptionsCallback )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , lambda : self.InpSecondAut("TempAutomataOne.aut","InputAutomataOne.png") )
        """
        QMessageBox.information( self, ' Product Automata ' , " Coming Soon " )


    def CallbackNine( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        DFA_list,String = NFA_Convert.transform_Dfa(StateList,Initial,Accepted)
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black '> Converts an epsilon-NFA to a DFA <\font><\body><\html>"
        self.MORE = String
        DISP_NFA.display( DFA_list , "OutputAutomata.png" )
        self.DrawAutomata()


    def CallbackTen( self ) :

        self.UI = AutEnterWord.Ui_MainWindow()
        self.UI.setupUi( self )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Checks if the automata accepts the word entered <\font> <\body> <\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Starting from the initial state the automata considers the word entered. Do note that the word entered contains the alphabets entered initially in the automata <\font> <\body> <\html>"
        QObject.connect( self.UI.pushButton , SIGNAL('clicked()') , self.AutOptionsCallback )
        QObject.connect( self.UI.commandLinkButton , SIGNAL('clicked()') , self.AutAcceptOne )

        QObject.connect( self.UI.pushButton , SIGNAL('clicked()') , self.AutOptionsCallback )
        QObject.connect( self.UI.commandLinkButton , SIGNAL('clicked()') , self.AutAcceptOne )


    def CallbackEleven( self ) :

        self.UI = AutEnterWord.Ui_MainWindow()
        self.UI.setupUi( self )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Checks if the automata accepts the word entered giving a detailed output<\font> <\body> <\html> "
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Starting from the initial state the automata considers the word entered. Do note that the word entered contains the alphabets entered initially in the automata<\font> <\body> <\html>"

        QObject.connect( self.UI.pushButton , SIGNAL('clicked()') , self.AutOptionsCallback )
        QObject.connect( self.UI.commandLinkButton , SIGNAL('clicked()') , self.AutAcceptTwo )

        QObject.connect( self.UI.pushButton , SIGNAL('clicked()') , self.AutOptionsCallback )
        QObject.connect( self.UI.commandLinkButton , SIGNAL('clicked()') , self.AutAcceptOne )


    def CallbackTwelve( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )

        String = State.state_elimination(StateList,Accepted,Initial)

        QMessageBox.information( self, ' DFA to RE ' , String )


    def CallbackThirteen ( self ):

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        message = Empty.check_Empty(StateList,Accepted,Initial)
        QMessageBox.information( self, ' Acceptance Information ' , message )


    def CallbackFourteen( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Shows the automata by removing useless states <\font> <\body> <\html>"
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Shows the automata by removing unreachable as well as trap states<\font><\body><\html>"
        Stlist = Rem_Useless.removeUseless_State(StateList,Accepted,Initial)
        DISP.display( Stlist , "OutputAutomata.png" )
        self.DrawAutomata()


    def CallbackFifteen( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( "TempAutomata.aut" )
        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >The Automata entered by you <\font><\body><\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Click on back for doing operations on this automata <\font><\body><\html>"
        DISP.display( StateList , "OutputAutomata.png" )
        self.DrawAutomata()


    def PLWizard( self ) :

        """
        SELECT :
        1 : HUMAN
        2 : AI
        """
        SELECT = 0

        if ( self.UI.radioButton_3.isChecked() ) : SELECT = 1

        if ( self.UI.radioButton.isChecked() ) : SELECT = 2

        GPump.choice = SELECT
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Select a language of your choice so that the game can start. <\font><\body><\html>"
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >This language is what you will be trying to prove not regular. <br><font size= 5 face= 'Georgia, Arial' color= ' red ' > Do note that your losing does not mean that the language is regular. It only means that for all the constraints set the language is regular. Press next to learn more. <\font><\body><\html>"
        self.UI = RPLPageTwo.Ui_MainWindow()
        self.UI.setupUi( self )

        self.UI.radioButton.setChecked(1)

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.PLCallback )
        QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , lambda : self.SelectLang(SELECT) )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def SelectLang( self , BEGIN ) :

        """
        LANGUAGE :
        AnBn : a^nb^n
        WWr : ww^r
        AgB : N(a) > N(b)
        """
        LANGUAGE = None

        if( self.UI.radioButton.isChecked() ) : LANGUAGE = AnBn()

        if( self.UI.radioButton_3.isChecked() ) : LANGUAGE = WWr()

        if( self.UI.radioButton_4.isChecked() ) : LANGUAGE = AgB()

        self.SelectN( BEGIN , LANGUAGE )


    def SelectN( self , BEGIN , LANG ) :

        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Select N that is the minimum length of the word <\font><\body><\html> "

        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >The word that will be selected depends on this length <\font><\body><\html>"

        if( BEGIN == 1 ) :

            self.UI = RPLEnterN.Ui_MainWindow()
            self.UI.setupUi( self )

            self.UI.spinBox.setMinimum(3)
            self.UI.spinBox.setMaximum(20)

            QObject.connect( self.UI.buttonBox , SIGNAL("accepted()") , lambda : self.InitN(BEGIN,LANG) )
            QObject.connect( self.UI.buttonBox , SIGNAL("rejected()") , self.PLCallback )

            QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
            QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )

        else :
            GPump.set_n()
            self.SelectWord( BEGIN , LANG )


    def SelectWord( self , BEGIN , LANG ) :

        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >Select a word that belongs in the language that you had selected. This word will be pumped and checked.<\font><\body><\html>"

        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >The N has been decided by the computer and is shown on the screen. you need to enter a word whose length is more than <font size= 5 face= 'Georgia, Arial' color= ' red ' >" + str(GPump.n) + "<\font><\body><\html>"

        if( BEGIN == 2 ) :

            self.UI = RPLEnterWord.Ui_MainWindow()
            self.UI.setupUi( self )

            self.UI.label_5.setText( "<b>"+str(GPump.n)+"</b>" )

            QObject.connect( self.UI.buttonBox , SIGNAL("accepted()") , lambda : self.InitWord(BEGIN,LANG) )
            QObject.connect( self.UI.buttonBox , SIGNAL("rejected()") , self.PLCallback )

            QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
            QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )

        else :

            GPump.word = LANG.get_word()
            self.SelectXYZ( BEGIN , LANG )


    def SelectXYZ( self , BEGIN , LANG ) :

        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The word has been randomly chosen by the computer. You need to divide this word into 3 parts X , Y and Z where length of X + length of Y <  " + str(GPump.n) + "\n Do remember to click on Split Word after selecting X and Y <\font><\body><\html>"
        self.MORE = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Here the word in Y portion will be pumped and concatinated to see if it exists in the language or not. So decide carefully the value of Y <\font><\body><\html>"
        if( BEGIN == 1 ) :

            self.UI = RPLEnterXYZ.Ui_MainWindow()
            self.UI.setupUi( self )

            self.UI.label.setText( "<b>"+GPump.word+"</b>" )
            self.UI.label_5.setText( "<b>"+str(GPump.n)+"</b>" )

            self.UI.horizontalSlider.setMaximum( len(GPump.word) )
            self.UI.horizontalSlider_2.setMaximum( len(GPump.word) )

            QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , self.DispXYZ )
            QObject.connect( self.UI.buttonBox , SIGNAL("accepted()") , lambda : self.InitXYZ(BEGIN,LANG) )
            QObject.connect( self.UI.buttonBox , SIGNAL("rejected()") , lambda : self.SelectN(BEGIN,LANG) )

            QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
            QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )

        else :
            GPump.set_xy()
            GPump.set_z()
            GPump.set_WordXYZ()
            self.SelectK( BEGIN , LANG )


    def SelectK( self , BEGIN , LANG ) :

        self.HELP = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > Computer has split the word you entered into 3 parts.<br> Enter the value of K for which the y portion will be pumped.<\font><\body><\html>"

        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The value you enter will be then used to form the new word and see if it exists in the language.<br>If it does then you lose else you win<\font><\body><\html>"

        if( BEGIN == 2 ) :

            self.UI = RPLEnterK.Ui_MainWindow()
            self.UI.setupUi( self )

            self.UI.label.setText( "<b>"+GPump.word+"</b>" )
            self.UI.label_3.setText( "<b>"+GPump.Word_x+"</b>" )
            self.UI.label_4.setText( "<b>"+GPump.Word_y+"</b>" )
            self.UI.label_5.setText( "<b>"+GPump.Word_z+"</b>" )

            QObject.connect( self.UI.buttonBox , SIGNAL("accepted()") , lambda : self.InitK(BEGIN,LANG) )
            QObject.connect( self.UI.buttonBox , SIGNAL("rejected()") , lambda : self.SelectWord(BEGIN,LANG) )

            QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
            QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )

        else :
            GPump.set_k()
            self.RunPL( LANG )


    def InitN( self , BEGIN , LANG ) :

        GPump.n = self.UI.spinBox.value()
        self.SelectWord( BEGIN , LANG )


    def InitWord( self , BEGIN , LANG ) :

        WORD = self.UI.lineEdit.text()

        if( not(LANG.in_Lang( WORD ))) :
            QMessageBox.information( self, ' Regular Pumping Lemma ' , "Entered word not in the selected language"  )

        elif(( len(WORD) < GPump.n ) ):
            QMessageBox.information( self, ' Regular Pumping Lemma ' , " Length of word should be greater than value of n"  )

        else :
            GPump.word = WORD
            GPump.length = len( WORD )
            self.SelectXYZ( BEGIN , LANG )


    def DispXYZ( self ) :

        GPump.x = self.UI.horizontalSlider.value()
        GPump.y = self.UI.horizontalSlider_2.value()
        GPump.z = GPump.set_z()
        GPump.set_WordXYZ()

        self.UI.label_3.setText( "<b>"+GPump.Word_x+"</b>" )
        self.UI.label_4.setText( "<b>"+GPump.Word_y+"</b>" )
        self.UI.label_6.setText( "<b>"+GPump.Word_z+"</b>" )


    def InitXYZ( self , BEGIN , LANG ) :

        GPump.x = self.UI.horizontalSlider.value()
        GPump.y = self.UI.horizontalSlider_2.value()
        GPump.z = GPump.set_z()
        GPump.set_WordXYZ()

        if( GPump.x + GPump.y >= GPump.n ) :
            QMessageBox.information( self, ' Regular Pumping Lemma ' , "Combined length of X and Y should be less than N"  )
            #Display Error Message

        else :
            self.SelectK( BEGIN , LANG )


    def InitK( self , BEGIN , LANG ) :

        GPump.k = self.UI.spinBox.value()
        self.RunPL( LANG )


    def RunPL( self , LANG ) :

        RetMessage = LANG.start()
        self.HELP = "<html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > The game has finished and the result will be displayed by clicking on OK <\font><\body><\html>"
        self.MORE = " <html> <body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' > If you win then the language is not regular.<br> However if you lose then it does'nt mean that the language is regular as there exists a possibility that you did not find the correct combination of x,y,z and k for which the language was not regular<\font><\body><\html>"
        QMessageBox.information( self , ' Regular Pumping Lemma ' , RetMessage )


    def DrawAutomata( self ) :

        self.UI = DispInterface.Ui_MainWindow()
        self.UI.setupUi( self )
        Canvas = QGraphicsScene()

        Canvas.addPixmap( QPixmap("OutputAutomata.png") )
        self.UI.graphicsView.setScene( Canvas )
        self.UI.graphicsView.show()

        QObject.connect( self.UI.actionSave_Automata , SIGNAL("triggered()") , self.SaveCallback )

        if( self.CHOICE_FLAG == 1 ) :
            QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.AutOptionsCallback )

        if( self.CHOICE_FLAG == 2 ) :
            QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.GrCallback )

        if( self.CHOICE_FLAG == 3 ) :
            QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.ReCallback )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def GrWordCallback( self ) :

        self.UI = GrEnterWord.Ui_MainWindow()
        self.UI.setupUi( self )

        QObject.connect( self.UI.commandLinkButton , SIGNAL("clicked()") , self.WordEntry )
        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.GrWindow )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def GrWindow( self ) :

        self.UI = GrmInterface.Ui_MainWindow()
        self.UI.setupUi( self )

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.GrCallback )
        QObject.connect( self.UI.AutButton , SIGNAL("clicked()") , self.GrCallbackOne )  # type of grammar
        QObject.connect( self.UI.GrButton , SIGNAL("clicked()") , self.GrCallbackTwo )  # grammar to pda
        QObject.connect( self.UI.AutButton_2 , SIGNAL("clicked()") , self.GrCallbackThree )  # identify left recursion
        QObject.connect( self.UI.GrButton_2 , SIGNAL("clicked()") , self.GrCallbackFour )  # remove epsilon
        QObject.connect( self.UI.AutButton_3 , SIGNAL("clicked()") , self.GrCallbackFive )  # grammar to CFG
        QObject.connect( self.UI.GrButton_6 , SIGNAL("clicked()") , self.GrCallbackSix )  # right linear to FSA
        QObject.connect( self.UI.AutButton_4 , SIGNAL("clicked()") , self.GrWordCallback )  # CYK algorithm
        QObject.connect( self.UI.GrButton_8 , SIGNAL("clicked()") , self.GrCallbackEight )  # unreachable and generating states
        QObject.connect( self.UI.AutButton_5 , SIGNAL("clicked()") , self.GrCallbackNine ) # Interact with Grammar
        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def WordEntry( self ) :

        WORD = self.UI.lineEdit.text()
        self.GrCallbackSeven(WORD)


    def InpChEqAut( self , Filename , Imagename ) :

        self.ReadAutomata( Filename , Imagename )

        self.UI = WizardPageTwo.Ui_MainWindow()
        self.UI.setupUi( self )

        Canvas = QGraphicsScene()
        Canvas.addPixmap( QPixmap(Imagename) )
        self.UI.graphicsView.setScene( Canvas )

        self.UI.graphicsView.show()

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.CallbackSeven )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , self.CheckEqualAut )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def CheckEqualAut( self ) :

        print "Call check equal automata! and display result"


    def InpSecondAut( self , Filename , Imagename ) :

        self.ReadAutomata( Filename , Imagename )

        self.UI = WizardPageTwo.Ui_MainWindow()
        self.UI.setupUi( self )

        Canvas = QGraphicsScene()
        Canvas.addPixmap( QPixmap(Imagename) )
        self.UI.graphicsView.setScene( Canvas )

        self.UI.graphicsView.show()

        QObject.connect( self.UI.pushButton , SIGNAL("clicked()") , self.CallbackEight )
        QObject.connect( self.UI.pushButton_2 , SIGNAL("clicked()") , self.ProductAut )

        QObject.connect( self.UI.HelpButton , SIGNAL("clicked()") , self.HelpCallback )
        QObject.connect( self.UI.MoreButton , SIGNAL("clicked()") , self.MoreCallback )


    def ProductAut( self ) :

        DFA_List = Prod.product_Automata("TempAutomataOne.aut","TempAutomata.aut")
        DISP.display( DFA_List , "OutputAutomata.png" )
        self.DrawAutomata()

    def AutAcceptOne( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( 'TempAutomata.aut' )

        word = str( self.UI.lineEdit.text() )

        message = Word_Acc.word_Accept(StateList,Accepted,Initial,word)
        QMessageBox.information( self, ' Acceptance Information ' , message )


    def AutAcceptTwo( self ) :

        StateList,Accepted,Initial = AutomataRead.FileRead( 'TempAutomata.aut' )

        word = str( self.UI.lineEdit.text() )

        message = State_Word_Acc.word_Accept(StateList,Accepted,Initial,word)
        QMessageBox.information( self, ' Acceptance Information ' , message )


    def HelpCallback( self ) :

        QMessageBox.information( self , ' HELP !! ' , self.HELP)


    def MoreCallback( self ) :

        MoreDialog = QDialog()
        UI = MoreInfo.Ui_Dialog()
        UI.setupUi( MoreDialog )

        UI.textBrowser.setHtml( self.MORE )

        MoreDialog.show()
        MoreDialog.exec_()


    def GrammarDisplay( self , DATA ) :

        DisplayDialog = QDialog()

        UI = GrDisplay.Ui_Dialog()
        UI.setupUi( DisplayDialog )

        UI.tableWidget.setColumnCount( len(DATA[0]) )
        UI.tableWidget.setRowCount( len(DATA) )

        row = 0
        for ROW in DATA :
            col = 0
            for data in ROW :

                DataItem = QTableWidgetItem( str(data) )
                UI.tableWidget.setItem( row , col , DataItem )
                col = col + 1

            row = row + 1

        UI.tableWidget.show()

        DisplayDialog.show()
        DisplayDialog.exec_()


    def SaveCallback( self ) :

        SaveWin = QFileDialog()
        FileName = SaveWin.getSaveFileName( )
        shutil.copy( "Temp.aut" , FileName )
        os.remove('Temp.aut')

    def OpenCallback( self ) :

        OpenWin = QFileDialog()
        FileName = OpenWin.getOpenFileName( )

        OpenFile = open( FileName , "r" )

        self.UI.textEdit.setText( OpenFile.read().rstrip('\n') )


if __name__ == "__main__":

    import sys , time

    #sys.stderr = open( "Errors.errlog" , "w" ) #Comment this line during active developement

    AppInit = QApplication( sys.argv )
    AppInit.setOrganizationName( "IIIT Delhi" )
    AppInit.setOrganizationDomain( "http://www.iiitd.ac.in" )
    AppInit.setApplicationName( "Automata Plus" )

    splash_pix = QPixmap( os.path.join( "ArtWork" , "SplashScreen.png" ) )
    splash = QSplashScreen( splash_pix , Qt.WindowStaysOnTopHint )
    splash.setMask( splash_pix.mask() )
    splash.show()
    splash.showMessage( (u"Starting.....") , Qt.AlignCenter | Qt.AlignBottom , Qt.yellow )
    AppInit.processEvents()

    time.sleep( 2 )

    AppWindow = MainWin()
    AppWindow.show()
    splash.finish( AppWindow )
    AppInit.exec_()
