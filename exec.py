from starterClass.starter import Starter
from starterClass.input_getter import InputGetter
from starterClass.exporter import Exporter
#from starter.exporter import Exporter
def input_selection():
    """This function controls the input selection"""
    print('i Asked')
""" 
x = Starter('local','plugin')
x.addLanguage('cs')
x.addClass('next')
x.addCopyright('Simon Zajicek')
x.addTask('newTast')
x.addTable('newtable','','id')sad
#x.addLanguage('en')
print(vars(x))
x.printTheContent() """
if(__name__) == '__main__':
    y = InputGetter()
    returned = y.execute()
    print(returned.tables)
    x = Exporter()
    x.createFolderTree(returned)
    x.exportXml(returned)
    x.exportSetting(returned)
    x.exportVersion(returned)
    x.exportIndex(returned)
    x.exportLanguages(returned)
    x.exportAccess(returned)
    x.exportTasks(returned)
    x.exportClasses(returned)
