#Python 2.5 Library
import os

#Google App Engine SDK
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class BugReportForm( webapp.RequestHandler ) :

    def get( self ) :

        self.response.headers["Content-Type"] = "text/html"

        FilePath = os.path.join( os.path.dirname(__file__) , "BugReport.html" )
        self.response.out.write( template.render( FilePath , {} ) )


BugWebForm = webapp.WSGIApplication( [( '/' , BugReportForm )] , debug=True )

def main(): run_wsgi_app( BugWebForm )

if __name__ == "__main__":
    main()
