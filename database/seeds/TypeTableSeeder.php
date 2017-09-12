<?php

use Illuminate\Database\Seeder;

class TypeTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('type')->insert([
            [
        		'name' => 'Income',
            	'hexcolor' => '#18bc9c',
            	'icon' => ''
        	],
        	[
        		'name' => 'Expense',
            	'hexcolor' => '#e74c3c',
            	'icon' => ''
        	],
            [
                'name' => 'Owe me',
                'hexcolor' => '#444444',
                'icon' => ''
            ]
            ,
            [
                'name' => 'Owe you',
                'hexcolor' => '#444444',
                'icon' => ''
            ]
    	]);
    }
}
