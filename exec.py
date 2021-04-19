from starterClass.starter import Starter
from starterClass.input_getter import InputGetter
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
x.addTable('newtable','','id')
#x.addLanguage('en')
print(vars(x))
x.printTheContent() """

y = InputGetter()
y.execute()