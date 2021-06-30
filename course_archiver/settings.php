<?php 
// This file is part of Moodle - http://moodle.org/
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
        
        
/** 
 * @package     local_course_archiver 
 * @copyright     Simon Zajicek
 * @copyright     IQdevelopment.cz
 * @copyright     2021

*/




$ADMIN->add('courses',new admin_externalpage('local_course_archiver', get_string('plugin_advanced', 'local_course_archiver'),new moodle_url('/local/course_archiver/index.php')));$settings = new admin_settingpage('local_course_archiver_settings',get_string('modulename','local_course_archiver'));$ADMIN->add('localplugins',$settings );
 
//example checkbox 
//$settings->add(new admin_setting_configcheckbox('local_course_archiver/type_1', get_string('one_day', 'local_course_archiver'),'', 0));
 
//example multiselect (multiselect of all visible categories) 

            /*$catlist = $DB->get_records_sql("SELECT * FROM {course_categories} WHERE visible = 1");
            $categories = array();
            foreach ($catlist as $category) {
                $categories[$category->id] = $category->name;
            }

            $settings->add(
                new admin_setting_configmultiselect(
                    'local_course_archiver/categories',
                    get_string('categories_enabled', 'local_course_archiver'),
                    '',
                    1,
                    $categories
                )
            );*/
 

           /*
            example textarea
            $settings->add(new admin_setting_configtextarea(
            'local_course_archiver/default_text_periodical',
            get_string('default_text_periodical_title', 'local_course_archiver'),
            '',
            get_string('default_text_periodical', 'local_course_archiver')));
            */
 
