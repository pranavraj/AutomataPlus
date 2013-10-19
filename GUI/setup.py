from distutils.core import setup
import py2exe


setup(  name = "Automata Plus" ,
        version = "1.0.0" ,
        description = "Runs the Automata Plus application" ,
        windows = [
            {
                "script" : "Automata+.pyw" ,
                "icon_resources" : [ (0 , "ArtWork\\AutPlusLogo.ico") ] ,
                "uac_info" : "requireAdministrator" ,
            }
                  ] ,
        zipfile = None )
