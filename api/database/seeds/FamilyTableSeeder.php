<?php

use Illuminate\Database\Seeder;

class FamilyTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('family')->insert(
        	[[
        		'name' => 'KalKi',
            	'hexcolor' => '#18bc9c'
        	]
        ]);
    }
}
