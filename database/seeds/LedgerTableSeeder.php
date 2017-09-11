<?php

use Illuminate\Database\Seeder;

class LedgerTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('ledger')->insert(
        	[[
        		'family_id' => 1,
            	'user_id' => 1,
            	'type_id' => 1,
            	'category_id' => 1,
            	'date' => date("Y-m-d H:i:s"),
            	'value' => rand(10, 100000),
            	'description' => 'Sample Data'
        	],
        	[
        		'family_id' => 1,
            	'user_id' => 1,
            	'type_id' => 2,
            	'category_id' => 1,
            	'date' => date("Y-m-d H:i:s"),
            	'value' => rand(10, 100000),
            	'description' => 'Sample Data'
        	],
            [
                'family_id' => 1,
            	'user_id' => 1,
            	'type_id' => 1,
            	'category_id' => 3,
            	'date' => date("Y-m-d H:i:s"),
            	'value' => rand(10, 100000),
            	'description' => 'Sample Data'
            ],
        	[
        		'family_id' => 1,
            	'user_id' => 2,
            	'type_id' => 2,
            	'category_id' => 2,
            	'date' => date("Y-m-d H:i:s"),
            	'value' => rand(10, 100000),
            	'description' => 'Sample Data'
        	],
            [
                'family_id' => 1,
            	'user_id' => 2,
            	'type_id' => 2,
            	'category_id' => 1,
            	'date' => date("Y-m-d H:i:s"),
            	'value' => rand(10, 100000),
            	'description' => 'Sample Data'
            ]
        	]
    	);
    }
}
