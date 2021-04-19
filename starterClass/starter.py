import os
class Starter:
    languages = []
    tasks = []
    tables = []
    classes = []
    plugintype=''
    copyright = ''


    """this class contains all you need to do to create moodle plugin"""
    def __init__(self,name):
        self.name = name

   


    
    def addLanguage(self,language = ''):
        """Add new language to create lang file"""
        if language == '':
            return 0
        self.languages.append(language)
        return 1

    def addTask(self,taskname=''):
        """Adding new task to create file"""
        if taskname == '':
            return 0
        self.tasks.append(taskname)
        return 1

    def addTable(self,tablename,fields,primary_key):
        """add table to make xml file"""
        final_object = {
            "name" : tablename,
            "fields" : fields,
            "key" : primary_key
        }
        self.tables.append(final_object)

    def addCopyright(self,text):
        """adds copyright text"""
        self.copyright = text

    def addClass(self,classname,folder = ''):
        obj = {
            "classname" : classname,
            "folder" : folder 
        }
        self.classes.append(obj)


    def printTheContent(self):
        print(self.tables)
        print(self.tasks)
        print(self.classes)
        print(self.copyright)
    
        