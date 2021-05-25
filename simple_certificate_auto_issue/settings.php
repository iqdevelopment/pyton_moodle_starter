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
 * @package     local_simple_certificate_auto_issue 
 * @copyright     Simon Zajicek
 * @copyright     2021
 * @copyright     IQdevelopment

*/




$ADMIN->add('courses',new admin_externalpage('local_simple_certificate_auto_issue', get_string('plugin_advanced', 'local_simple_certificate_auto_issue'),new moodle_url('/local/simple_certificate_auto_issue/index.php')));$settings = new admin_settingpage('local_simple_certificate_auto_issue_settings',get_string('modulename','local_simple_certificate_auto_issue'));$ADMIN->add('localplugins',$settings );
 
//example checkbox 
//$settings->add(new admin_setting_configcheckbox('local_simple_certificate_auto_issue/type_1', get_string('one_day', 'local_simple_certificate_auto_issue'),'', 0));
 
//example multiselect (multiselect of all visible categories) 

            /*$catlist = $DB->get_records_sql("SELECT * FROM {course_categories} WHERE visible = 1");
            $categories = array();
            foreach ($catlist as $category) {
                $categories[$category->id] = $category->name;
            }

            $settings->add(
                new admin_setting_configmultiselect(
                    'local_simple_certificate_auto_issue/categories',
                    get_string('categories_enabled', 'local_simple_certificate_auto_issue'),
                    '',
                    1,
                    $categories
                )
            );*/
 

           /*
            example textarea
            $settings->add(new admin_setting_configtextarea(
            'local_simple_certificate_auto_issue/default_text_periodical',
            get_string('default_text_periodical_title', 'local_simple_certificate_auto_issue'),
            '',
            get_string('default_text_periodical', 'local_simple_certificate_auto_issue')));
            */
 
