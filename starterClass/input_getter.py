from starterClass.starter import Starter
class InputGetter:
    """Class containing all the methods to get data from the user"""
    possible_field_types = [
            {
                "type": "int",
                "lenght-min": 1,
                "lenght-max" : 25
            },
            {
                "type": "float",
                "lenght-min": 1,
                "lenght-max" : 7
            },
            {
                "type": "char",
                "lenght-min": 1,
                "lenght-max" : 255
            },
            {
                "type": "text",
                "lenght-min": -1,
                "lenght-max" : -1
            }
        ]

    def execute(self):
        """Connector for methods"""
        name = self.getNameOfPlugin()

        #initiate the class starter
        Obj = Starter(name)

        #add type of module
        Obj.plugintype = self.typeOfModule()

        #add languages
        Obj.addLanguage('en')
        lang_return = 1
        while lang_return == 1:
            lang_check = self.getLanguage()
            if lang_check != '':
                Obj.addLanguage(lang_check)
            else:
                lang_return = 0

        #ask for task
        task_return = 1
        while task_return == 1:
            task_check = self.getTasks()
            if task_check != '':
                Obj.addTask(task_check)
            else:
                task_return = 0
        
        #ask for copyright
        copyright_return = 1
        while copyright_return == 1:
            copyright_check = self.getCopyrigtText()
            if copyright_check != '':
                Obj.addCopyright(copyright_check)
            else:
                copyright_return = 0
        
        #ask for classes
        classes_return = 1
        while classes_return == 1:
            classes_check = self.getClass()
            if classes_check != '':
                Obj.addClass(classes_check["name"],classes_check["folder"])
            else:
                classes_return = 0

        #ask for tables
        table_return = 1
        while table_return == 1:
            table_check = self.getTable()
            if table_check != '':
                Obj.addTable(table_check["name"],table_check["fields"],table_check["primarykey"])
            else:
                table_return = 0
                print('it came to this')
       

        #print the whole content
        Obj.printTheContent()
        return Obj
        
        

    def getNameOfPlugin(self):
        output = input("Name of the plugin: ")
        return output


    def typeOfModule(self):
            possible = ['block','local','mod','quiz','customfield','filter','editor','atto','enrol','auth','tool','theme']
            output = input("Type of the plugin: ")
            if output in possible:
                return output
            else:
                raise ValueError('Plugin type is not valid.')

    def getLanguage(self):
        """Asks youser for 2-letter language shortcut and validates it"""
        output = input('ad new language (en is defautly added) and leave empty for next step: ')
        if(len(output) < 3):
            return output
        else:
            raise ValueError('Language code is only 2 string long ("en","es"...)')


    def getTasks(self):
        """asks user for input to create new task"""
        output = input('add name of your scheduled task (leave empty for the next step): ')
        return output

    def getCopyrigtText(self):
        """asks user for input for copyright text"""
        output = input('add one line of your copyright text (leave empty for the next step): ')
        return output

    def getClass(self):
        """asks user for input for classes, it returns dictionary"""
        output_name = input('add new class name(leave empty for the next step): ')
        if output_name == '':
            return output_name
        else:
            output_folder = input('add a name for a class folder(leave empty for leaving it in the /classes folder): ')
            output = {
                "name" : output_name,
                "folder" : output_folder
            }
        return output



    def getTable(self):
        """asks user for input for tables"""
        output_name = input('add new Table to create in install file(leave empty for the next step): ')
        output_fields = []
        output_fields_name_list = ''
        go_to_next = False
        output_table_field_names = ''

       
        if output_name == '':
            #skips to next step -> no table
            return output_name

        else:
            for i in self.possible_field_types:
                output_table_field_names = f'{output_table_field_names}{i["type"]},'


            while go_to_next == False:
                output_table_field = input('please state name of field: (leave blank to skipt to the next table)')
                if output_table_field == '':
                    #skips to next step -> no table
                    go_to_next = True
                else:
                    output_table_type = input(f'please state type of field: ({output_table_field_names})')
                    output_table_lenght = input('please state lenght of field: ')
                    output_table_null = input('please state can be this field null? (yes/no): ')
                    output_fields_to_push = {
                        "name" : output_table_field,
                        "type" : output_table_type,
                        "lenght" : output_table_lenght,
                        "notnull" : output_table_null
                    }
                    output_fields_name_list = f'{output_fields_name_list}{output_table_field},'
                    output_fields.append(output_fields_to_push)
                    print('-----next field-----')
                        


            output_primary_key = input(f'State the name of primary key from this list: {output_fields_name_list} :')
            output = {
                "name" : output_name,
                "primarykey" : output_primary_key,
                "fields" : output_fields
            }
        return output