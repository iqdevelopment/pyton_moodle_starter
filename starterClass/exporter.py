import os
import xml.etree.ElementTree as ET
from datetime import datetime


class Exporter:    
    """This class executes the export of data itself"""
    moodle_text = """// This file is part of Moodle - http://moodle.org/
        //
        // Moodle is free software: you can redistribute it and/or modify
        // it under the terms of the GNU General Public License as published by
        // the Free Software Foundation, either version 3 of the License, or
        // (at your option) any later version.
        //
        // Moodle is distributed in the hope that it will be useful,
        // but WITHOUT ANY WARRANTY; without even the implied warranty of
        // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        // GNU General Public License for more details.
        //
        // You should have received a copy of the GNU General Public License
        // along with Moodle.  If not, see <http://www.gnu.org/licenses/>.
        
        """

    def createFolderTree(self,obj):
        base_dir = os.getcwd()
        sub_dir = obj.name
        full_base_name = os.path.join(base_dir,sub_dir)
        #makes default_dir
        os.makedirs(full_base_name, exist_ok=True)
        self.full_base_folder_name = full_base_name

        #db folder
        db_folder =  os.path.join(full_base_name,'db')
        os.makedirs(db_folder, exist_ok=True)
        self.db_folder = db_folder

        #assets folder (+ JS a CSS + img) 
        assets_folder =  os.path.join(full_base_name,'assets')
        os.makedirs(assets_folder, exist_ok=True)
        js_folder = os.path.join(assets_folder,'js')
        os.makedirs(js_folder, exist_ok=True)
        css_folder = os.path.join(assets_folder,'css')
        os.makedirs(css_folder, exist_ok=True)
        img_folder = os.path.join(assets_folder,'img')
        os.makedirs(img_folder, exist_ok=True)
        


    def initiateFile(self,obj,namespace = False):
        """Initiate head in head of every file"""
        complete_string = '<?php \n'
        complete_string = complete_string + self.moodle_text
        complete_string = complete_string + '\n' + '/** \n'
        complete_string = complete_string + f' * @package     {obj.plugintype}_{obj.name} \n'

        for copyright_line in obj.copyright:
            complete_string = complete_string + f' * @copyright     {copyright_line}' '\n'
        complete_string = complete_string + '\n' + '*/'
        complete_string = complete_string + '\n'
        complete_string = complete_string + '\n'
        if(namespace):
            complete_string = complete_string + f'namespace {namespace}; \n'
        complete_string = complete_string + '\n'
        complete_string = complete_string + '\n'
        complete_string = complete_string + '\n'
        return complete_string



    def exportXml(self,obj):
        """Method to export xml to /db/install.xml"""
       # ET.tostring(encoding="unicode",pretty_print=True)
        data = ET.Element('XMLDB')
        #sem docpat plugin atd..
        data.set('path',f'{obj.plugintype}_{obj.name}/db')
        data.set('version',f'{obj.version}')
        data.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
        data.set('xsi:noNamespaceSchemaLocation','../../../lib/xmldb/xmldb.xsd')
        data.tail = "\n" 

        tables = ET.SubElement(data, 'TABLES')
        n = 0
        for table_obj in obj.tables:
            globals()[f'table{n}'] = ET.SubElement(tables, 'TABLE')
            globals()[f'table{n}'].set('NAME', table_obj['name'])

            globals()[f'keys{n}'] = ET.SubElement(globals()[f'table{n}'], 'KEYS')
            globals()[f'key{n}'] = ET.SubElement(globals()[f'keys{n}'], 'KEY')
            globals()[f'key{n}'].set('NAME', 'primary')
            globals()[f'key{n}'].set('TYPE', 'primary')
            globals()[f'key{n}'].set('FIELDS', table_obj['key'])
            
            print(table_obj['key'])
            for index in range(len(table_obj['fields'])):
                q = f'{n}{index}'
                globals()[f'fields{q}'] = ET.SubElement(globals()[f'table{n}'], 'FIELDS')
                globals()[f'field{q}'] = ET.SubElement(globals()[f'fields{q}'], 'FIELD')

                globals()[f'field{q}'].set('NAME', table_obj['fields'][index]['name'])
                globals()[f'field{q}'].set('TYPE', table_obj['fields'][index]['type']) 
                #text type of field does not need a lenght so test
                if table_obj['fields'][index]['type'] != 'text':
                    globals()[f'field{q}'].set('LENGTH', table_obj['fields'][index]['lenght'])
                #transfer form yes and not to true/false
                if table_obj['fields'][index]['notnull'] == 'yes':
                    globals()[f'field{q}'].set('NOTNULL', 'false')
                else:
                    globals()[f'field{q}'].set('NOTNULL', 'true')
                #if name of the key = name of primary key -> SEQUENCE == TRUE
                if table_obj['key'] == table_obj['fields'][index]['name']:
                    globals()[f'field{q}'].set('SEQUENCE', 'true')
                else:
                    globals()[f'field{q}'].set('SEQUENCE', 'false')
                
            n+=1
        mydata = ET.tostring(data)
        file_path = os.path.join(self.db_folder,'install.xml')
        with open(file_path,'wb') as output_file:
            output_file.write(mydata)
        
        """myfile = open("install.xml", "wb")
        myfile.write(mydata) """




    def exportSetting(self,obj):
        """Export setting file"""

        example_head = (f"$ADMIN->add('courses',new admin_externalpage('{obj.plugintype}_{obj.name}', get_string('plugin_advanced', '{obj.plugintype}_{obj.name}'),new moodle_url('/{obj.plugintype}/{obj.name}/index.php')));"
	                    f"$settings = new admin_settingpage('{obj.plugintype}_{obj.name}_settings',get_string('modulename','{obj.plugintype}_{obj.name}'));"
                        "$ADMIN->add('localplugins',$settings );")

        example_checkbox = ("//example checkbox \n"
        f"//$settings->add(new admin_setting_configcheckbox('{obj.plugintype}_{obj.name}/type_1', get_string('one_day', '{obj.plugintype}_{obj.name}'),'', 0));")

        example_multiselect = """//example multiselect (multiselect of all visible categories) \n
            /*$catlist = $DB->get_records_sql("SELECT * FROM {course_categories} WHERE visible = 1");
            $categories = array();
            foreach ($catlist as $category) {
                $categories[$category->id] = $category->name;
            }

            $settings->add(
                new admin_setting_configmultiselect(
                    'local_custom_notification/categories',
                    get_string('categories_enabled', 'local_custom_notification'),
                    '',
                    1,
                    $categories
                )
            );*/""".replace('local_custom_notification',f'{obj.plugintype}_{obj.name}')
        
        example_text_area = """
           /*
            example textarea
            $settings->add(new admin_setting_configtextarea(
            'local_custom_notification/default_text_periodical',
            get_string('default_text_periodical_title', 'local_custom_notification'),
            '',
            get_string('default_text_periodical', 'local_custom_notification')));
            */""".replace('local_custom_notification',f'{obj.plugintype}_{obj.name}')

        return_object = self.initiateFile(obj)
        return_object = return_object + example_head + '\n \n'
        return_object = return_object + example_checkbox + '\n \n'
        return_object = return_object + example_multiselect + '\n \n'
        return_object = return_object + example_text_area + '\n \n'

        #myfile = open("settings.php", "w")
        file_path = os.path.join(self.full_base_folder_name,'settings.php')
        with open(file_path,'w') as output_file:
            output_file.write(return_object)



    def exportIndex(self,obj):
        """exports index.php"""
        return_object = self.initiateFile(obj,f'{obj.plugintype}_{obj.name}')
        #return_object = return_object + f'namespace {obj.plugintype}_{obj.name};' + '\n \n'
        return_object = return_object + "require_once '../../config.php';" + '\n'
        return_object = return_object + "require_login();" + '\n'
        return_object = return_object + 'global $USER,$DB,$CFG;'+ '\n \n'
        return_object = return_object + f"$PAGE->set_url('/{obj.plugintype}/{obj.name}/index.php');" + '\n'
        return_object = return_object + f"$PAGE->set_title(get_string('modulename','{obj.plugintype}_{obj.name}'));" + '\n'
        return_object = return_object + "$PAGE->navbar->add($PAGE->title, $PAGE->url);" + '\n'
        return_object = return_object + "echo $OUTPUT->header();" + '\n '
        return_object = return_object + f"//if needed JS $PAGE->requires->js('/{obj.plugintype}/{obj.name}/assets/js/custom.js');" + '\n '
        return_object = return_object + f"//if needed JS $PAGE->requires->css('/{obj.plugintype}/{obj.name}/assets/css/custom.css');" + ' \n'
        return_object = return_object + '\n \n \n' +"//your code" + '\n \n \n'
        return_object = return_object + "echo $OUTPUT->footer();" + '\n'
        file_path = os.path.join(self.full_base_folder_name,'index.php')
        with open(file_path,'w') as output_file:
            output_file.write(return_object)
        """myfile = open("index.php", "w")
        myfile.write(return_object) """


    def exportVersion(self,obj):
        """export version file"""
        return_object = self.initiateFile(obj)
        dateTimeObj = datetime.now()
        timestamp = dateTimeObj.strftime("%Y%m%d")
        return_object = return_object + f"$plugin->version = {timestamp}; //this is just for me" + '\n \n'
        return_object = return_object + f"$plugin->requires = {obj.version}; \n //requred moodle version (this is for 3.6) more here: https://docs.moodle.org/dev/Releases" + '\n \n'
        return_object = return_object + f"$plugin->component = '{obj.plugintype}_{obj.name}'; \n \n"
        #var_exists = 'obj.task' in locals() or 'obj.task' in globals()
        if obj.tasks:
            return_object = return_object + f"$plugin->cron = 60;'; //enables cron \n \n"  
        return_object = return_object + f"$plugin->release = '1.0'; \n \n"
        return_object = return_object + f"$plugin->maturity = MATURITY_STABLE; \n \n"
        file_path = os.path.join(self.full_base_folder_name,'version.php')
        with open(file_path,'w') as output_file:
            output_file.write(return_object)
        """ myfile = open("version.php", "w")
        myfile.write(return_object) """
        

    def exportLanguages(self,obj):
        """exports languages into /lang folder"""
        return_object = self.initiateFile(obj)
        return_object = return_object + (f"$string['modulename'] = '{obj.name}';\n"
                    f"$string['pluginname'] = '{obj.name}';\n"
                    f"$string['plugin_advanced'] = '{obj.name}';\n")

        for language in obj.languages:
            #global /lang folder
            lang_folder = os.path.join(self.full_base_folder_name,'lang')
            os.makedirs(lang_folder, exist_ok=True)
            #custom /lang/en
            lang_sub_folder = os.path.join(lang_folder,language)
            os.makedirs(lang_sub_folder, exist_ok=True)
            #create content
            file_path = os.path.join(lang_sub_folder,f'{obj.plugintype}_{obj.name}.php')
            with open(file_path,'w') as output_file:
                output_file.write(return_object)

    def exportAccess(self,obj):
        return_object = self.initiateFile(obj)
        return_object = return_object + """defined ( 'MOODLE_INTERNAL' ) || die();

                $capabilities = array(
                    'local/kopere_dashboard:view' => array(
                        'captype' => 'write',
                        'contextlevel' => CONTEXT_SYSTEM,
                        'archetypes' => array(
                            'manager' => CAP_ALLOW
                        )
                    ),
                    'local/kopere_dashboard:manage' => array(
                        'captype' => 'write',
                        'contextlevel' => CONTEXT_SYSTEM,
                        'archetypes' => array(
                            'manager' => CAP_ALLOW
                        )
                    )
                );
                """.replace('local/kopere_dashboard',f'{obj.plugintype}/{obj.name}')
        file_path = os.path.join(self.full_base_folder_name,'db')
        file_path = os.path.join(file_path,'access.php')
        with open(file_path,'w') as output_file:
                output_file.write(return_object)




    def exportTasks(self,obj):
        """Fills up the task in /db and creates class files within class/task"""
        return_file_text = self.initiateFile(obj)
        return_file_text = return_file_text + "defined ( 'MOODLE_INTERNAL' ) || die(); \n \n"
        return_file_text = return_file_text + "$tasks = array( \n"
       # var_exists = 'obj.task' in locals() or 'obj.task' in globals()
        if not obj.tasks:
            print('nupe')
            return 0
            
        else:
            print('yup')
            #creates also classes folder
            folder_path = os.path.join(self.full_base_folder_name,'classes')
            os.makedirs(folder_path, exist_ok=True)
            folder_path = os.path.join(folder_path,'task')
            os.makedirs(folder_path, exist_ok=True)

            for task in obj.tasks:
                #create in tasks new entry
                return_file_text = return_file_text + """
                
                        array(
                            'classname' => 'class_file',
                            'blocking' => 0,
                            'minute' => '0',
                            'hour' => '0',
                            'day' => '*',
                            'dayofweek' => '*',
                            'month' => '*'
                        ), \n \n""".replace('class_file',f'{obj.plugintype}\\{obj.name}\\{task}')

                #filling for the task class file

                return_object = self.initiateFile(obj,f'{obj.plugintype}_{obj.name}\\task')
                return_object = return_object + "defined ( 'MOODLE_INTERNAL' ) || die(); \n \n"
                return_object = return_object + """
                class task_tmp  extends \\core\\task\\scheduled_task {
                    
                    public function get_name() {
                        return get_string('crontask_tmp', 'module_path');
                    }

                    /**
                    *
                    */
                    public function execute() {
                        global $CFG;

                        

                    }

                }"""

                return_object = return_object.replace('crontask_tmp',f'{task}')
                return_object = return_object.replace('task_tmp',f'{task}')
                return_object = return_object.replace('module_path',f'{obj.plugintype}_{obj.name}')

            
                #also creates new class for the task
                file_path = os.path.join(folder_path,f'{task}.php')
                with open(file_path,'w') as output_file:
                    output_file.write(return_object)
            return_file_text = return_file_text + "); \n"
            #write the tasks.php into db
            file_path = os.path.join(self.db_folder,'tasks.php')
            with open(file_path,'w') as output_file:
                output_file.write(return_file_text)


    def exportClasses(self,obj):
        """creates new class files and automaticly creates namespaces"""
        for class_obj in obj.classes:
            folder_path = os.path.join(self.full_base_folder_name,'classes')
            if class_obj["folder"] != '':
                #if in folder create folder
                folder_path_class = os.path.join(folder_path,class_obj["folder"])
                os.makedirs(folder_path_class, exist_ok=True)
                file_namespace = f'{obj.plugintype}_{obj.name}/{class_obj["folder"]}'
            else:
               folder_path_class = folder_path
               file_namespace = f'{obj.plugintype}_{obj.name}'
            #test of the file
            return_file_text = self.initiateFile(obj,file_namespace)
            return_file_text = return_file_text + "defined ( 'MOODLE_INTERNAL' ) || die(); \n \n"
            return_file_text = return_file_text + f"""class {class_obj['name']} ## \n \n \n \n #$# """
            return_file_text = return_file_text.replace('##',"{")
            return_file_text = return_file_text.replace('#$#',"}")

            #creating the file
            file_path = os.path.join(folder_path_class,f'{class_obj["name"]}.php')
            with open(file_path,'w') as output_file:
                output_file.write(return_file_text)
            

                









