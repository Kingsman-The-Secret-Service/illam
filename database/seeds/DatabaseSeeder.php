<?php

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $this->call(TypeTableSeeder::class);
        $this->call(UserTableSeeder::class);
        $this->call(FamilyTableSeeder::class);
        $this->call(LedgerTableSeeder::class);
        // $this->call(CategoryTableSeeder::class);
    }
}
