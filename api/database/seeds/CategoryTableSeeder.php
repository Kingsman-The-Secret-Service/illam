<?php

use Illuminate\Database\Seeder;

class CategoryTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        
        DB::table('category')->insert([
            [
                'family_id' => 0,
                'user_id' => 0,
                'category_id' => 0,
                'name' => 'Category',
                'description' => 'Kanaku Puthagam Category (Main)',
                'hexcolor' => '#000000'
            ],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 1,
        		'name' => 'Savings',
        		'description' => 'PPF, FD, RD, MUTUAL FUND',
            	'hexcolor' => '#18bc9c'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 1,
        		'name' => 'Foods',
        		'description' => 'Foods',
            	'hexcolor' => '#cccccc'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 1,
        		'name' => 'Bills',
        		'description' => 'Bills',
            	'hexcolor' => '#eeeeee'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 2,
        		'name' => 'PPF',
        		'description' => 'PPF',
            	'hexcolor' => '#18bc9c'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 2,
        		'name' => 'FD',
        		'description' => 'FD & RD',
            	'hexcolor' => '#18bc9c'
        	]
        	,
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 2,
        		'name' => 'Mutual Fund',
        		'description' => 'MUTUAL FUND',
            	'hexcolor' => '#18bc9c'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 3,
        		'name' => 'Grocries',
        		'description' => 'Grocries',
            	'hexcolor' => '#cccccc'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 3,
        		'name' => 'Resturant',
        		'description' => 'Resturant',
            	'hexcolor' => '#cccccc'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 4,
        		'name' => 'Mobile',
        		'description' => 'Mobile',
            	'hexcolor' => '#eeeeee'
        	],
        	[
        		'family_id' => 1,
        		'user_id' => 1,
        		'category_id' => 4,
        		'name' => 'TNEB',
        		'description' => 'TNEB',
            	'hexcolor' => '#eeeeee'
        	]
        ]);
    }
}
