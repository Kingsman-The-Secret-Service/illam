<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('users')->insert([
            [	
            	'family_id' => 1,
        		'name' => 'Kaviarasan K K',
        		'email' => 'kaviarasankk@gmail.com',
        		'phone' => '9789231303',
        		'password' => Hash::make('secret'),
            	'api_token' => 'UHRrNXN2SzUxMmlqc2ZNb3MxVjUyR1g3RTlEU3JSaFlFMndKb0ZNWA=='
        	],
        	[
        		'family_id' => 1,
        		'name' => 'Kavi',
        		'email' => 'kavikk@gmail.com',
        		'phone' => '9789231333',
        		'password' => Hash::make('secret'),
            	'api_token' => ''
        	]
    	]);
    }
}
