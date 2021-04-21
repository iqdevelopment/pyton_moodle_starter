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
 * @package     local_beta_test 
 * @copyright     Simon Zajicek
 * @copyright     2021
 * @copyright     IQdevelopment

*/




defined ( 'MOODLE_INTERNAL' ) || die(); 
 
$tasks = array( 

                
                        array(
                            'classname' => 'local_beta_test\task\task_one',
                            'blocking' => 0,
                            'minute' => '0',
                            'hour' => '0',
                            'day' => '*',
                            'dayofweek' => '*',
                            'month' => '*'
                        ), 
 

                
                        array(
                            'classname' => 'local_beta_test\task\kill_humans',
                            'blocking' => 0,
                            'minute' => '0',
                            'hour' => '0',
                            'day' => '*',
                            'dayofweek' => '*',
                            'month' => '*'
                        ), 
 

                
                        array(
                            'classname' => 'local_beta_test\task\rule_the_galagy',
                            'blocking' => 0,
                            'minute' => '0',
                            'hour' => '0',
                            'day' => '*',
                            'dayofweek' => '*',
                            'month' => '*'
                        ), 
 
); 
