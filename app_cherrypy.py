import cherrypy

class FisrtPage(object):
    def HandleData(self,data=None):
        return data
    HandleData.exposed = True

    def index(self):
        return """ <form action="HandleData" method="post">
                      <label for="fname">User Input:</label><br>
                      <input type="text" name="data">
                      <input type="submit" value="Submit">
                      <p>
                   """
    index.exposed = True

cherrypy.quickstart(FisrtPage())
