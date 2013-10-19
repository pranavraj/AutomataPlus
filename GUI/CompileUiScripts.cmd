@echo off
Call pyuic4 AutEnterWord.ui -o AutEnterWord.py
Call pyuic4 AutomataInterface.ui -o AutomataInterface.py
Call pyuic4 DispInterface.ui -o DispInterface.py
Call pyuic4 GrDisplay.ui -o GrDisplay.py
Call pyuic4 GrEnterWord.ui -o GrEnterWord.py
Call pyuic4 GrmInteractive.ui -o GrmInteractive.py
Call pyuic4 GrmInterface.ui -o GrmInterface.py
Call pyuic4 GrmWizard.ui -o GrmWizard.py
Call pyuic4 MainWindow.ui -o MainWindow.py
Call pyuic4 MoreInfo.ui -o MoreInfo.py
Call pyuic4 RegExpInterface.ui -o RegExpInterface.py
Call pyuic4 RPLEnterK.ui -o RPLEnterK.py
Call pyuic4 RPLEnterN.ui -o RPLEnterN.py 
Call pyuic4 RPLEnterWord.ui -o RPLEnterWord.py 
Call pyuic4 RPLEnterXYZ.ui -o RPLEnterXYZ.py 
Call pyuic4 RPLInterface.ui -o RPLInterface.py 
Call pyuic4 RPLPageOne.ui -o RPLPageOne.py 
Call pyuic4 RPLPageTwo.ui -o RPLPageTwo.py 
Call pyuic4 WizardPageOne.ui -o WizardPageOne.py 
Call pyuic4 WizardPageTwo.ui -o WizardPageTwo.py
pyrcc4 HelpIcon.qrc -o HelpIcon_rc.py
pyrcc4 MoreInfoIcon.qrc -o MoreInfoIcon_rc.py