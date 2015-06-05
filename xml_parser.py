
import xml.sax

class ReuterHandler( xml.sax.ContentHandler ):
    #count = 0
    
    def __init__(self):
        self.currentData = ""
        self.DATE = ""
        self.PLACES = ""
        self.PEOPLE = ""
        self.ORGS = ""
        self.EXCHANGES = ""
        self.COMPANIES = ""
        self.UNKNOWN = ""
        self.TEXT = ""
        self.TITLE = ""
        self.DATELINE = ""
        self.BODY = ""

    def startElement(self,tag,attributes):
        #self.count += 1
        self.CurrentData = tag
        if tag == "REUTERS":
            print ("*****REUT*****")
            TOPICS = attributes["TOPICS"]
            print("TOPICS:" %TOPICS)
            LEWISSPLIT = attributes["LEWISSPLIT"]
            print("LEWISSPLIT:" %LEWISSPLIT)
            CGISPLIT = attributes["CGISPLIT"]
            print("CGISPLIT:" %CGISPLIT)
            OLDID = attributes["OLDID"]
            print("OLDID:" %OLDID)
            NEWID = attributes["NEWID"]
            print("NEWID:" %NEWID)
            

    def endElement(self,tag):
        if self.CurrentData == "DATE":
            print("DATE: {0}" .format(self.DATE))
        elif self.CurrentData == "TOPICS":
            print("TOPICS: {0}" .format(self.TOPICS))
        elif self.CurrentData == "TITLE":
            print("TITLE: {0}" .format(self.TITLE))
        elif self.CurrentData == "DATELINE":
            print("DATELINE: {0}" .format(self.DATELINE))
        elif self.CurrentData == "BODY":
            print("BODY: {0}" .format(self.BODY))
        self.CurrentData = ""

    def characters(self,content):
        if self.CurrentData == "DATE":
            self.DATE = content
        elif self.CurrentData == "TOPICS":
            self.TOPICS = content
        elif self.CurrentData == "TITLE":
            self.TITLE = content
        elif self.CurrentData == "DATELINE":
            self.DATELINE = content
        elif self.CurrentData == "BODY":
            self.BODY = content




parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = ReuterHandler()
parser.setContentHandler(handler)
parser.parse("reut2.xml")