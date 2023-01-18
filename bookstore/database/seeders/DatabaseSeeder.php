<?php

namespace Database\Seeders;

// use Illuminate\Database\Console\Seeds\WithoutModelEvents;

use App\Models\Book;
use \App\Models\User;
use \App\Models\Continent;
use \App\Models\Country;
use App\Models\Writer;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        //to dont repeat the same data when db:seed happen
        User::truncate();
        Continent::truncate();
        Country::truncate();

        User::factory(10)->create();
        /**
         * Continents
         */
        $asia = Continent::create([
            "name" => 'Asia',
            "slug" => 'asia'
        ]);

        $america = Continent::create([
            "name" => 'America',
            "slug" => 'america'
        ]);

        $europe = Continent::create([
            "name" => 'Europe',
            "slug" => 'europe'
        ]);

        $africa = Continent::create([
            "name" => 'Africa',
            "slug" => 'africa'
        ]);

        $oceanic = Continent::create([
            "name" => 'Oceanic',
            "slug" => 'oceanic'
        ]);
        /**
         * Countries
         */
        $england = Country::create([
            "name" => 'England',
            "slug" => 'england',
            "continent_id" => $europe->id
        ]);

        $elsalvador = Country::create([
            "name" => 'El Salvador',
            "slug" => 'el-salvador',
            "continent_id" => $america->id
        ]);

        $mongolia = Country::create([
            "name" => 'Mongolia',
            "slug" => 'mongolia',
            "continent_id" => $asia->id
        ]);

        $morocco = Country::create([
            "name" => 'Morocco',
            "slug" => 'morocco',
            "continent_id" => $africa->id
        ]);

        $australia = Country::create([
            "name" => 'Austalia',
            "slug" => 'australia',
            "continent_id" => $oceanic->id
        ]);

        $jane = Writer::create([
            "name" => 'Jane Austen',
            "slug" => 'jane-austen',
            "country_id" => $england->id
        ]);

        $claudia = Writer::create([
            "name" => 'Claudia Lars',
            "slug" => 'claudia-lars',
            "country_id" => $elsalvador->id
        ]);

        $emma = Book::create([
            "title" => 'Emma',
            "slug" => 'emma',
            "release_year" => 1815,
            "writer_id" => $jane->id
        ]);

        $pride = Book::create([
            "title" => 'Pride and Prejudice',
            "slug" => 'pride-and-prejudice',
            "release_year" => 1813,
            "writer_id" => $jane->id
        ]);

        $land = Book::create([
            "title" => 'Land of Chilhood',
            "slug" => 'land-of-childhood',
            "release_year" => 1958,
            "writer_id" => $claudia->id
        ]);

      
    }
}
