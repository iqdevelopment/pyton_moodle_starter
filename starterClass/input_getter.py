from starterClass.starter import Starter
class InputGetter:
    """Class containing all the methods to get data from the user"""

    def execute(self):
        """Connector for methods"""
        name = self.getNameOfPlugin()
        Obj = Starter(name)
        Obj.plugintype = self.typeOfModule()
        print(Obj)



    def getNameOfPlugin(self):
        output = input("Name of the plugin: ")
        return output


    def typeOfModule(self):
            possible = ['block','local','mod','quiz','customfield','filter','editor','atto','enrol','auth','tool','theme']
            output = input("Type of the plugin: ")
            if output in possible:
                return output
            else:
                return 0
