import os
import xml.etree.ElementTree as ET


class Exporter:    
    """This class executes the export of data itself"""

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
        myfile = open("install.xml", "wb")
        myfile.write(mydata)


        



