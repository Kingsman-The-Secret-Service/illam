<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return $router->app->version();
});


$router->group(['prefix' => 'api'], function () use ($router) {

	// Authenticate
	$router->get('authenticate', 'UserController@authenticate');

	// User
	$router->get('user', 'UserController@index');
    $router->post('user', 'UserController@store');
    $router->put('user/{id}/', 'UserController@update');

    // Family
    $router->get('family', 'FamilyController@index');
    $router->post('family', 'FamilyController@store');
    $router->put('family/{id}/', 'FamilyController@update');

    // People
    $router->get('people', 'PeopleController@index');
    $router->post('people', 'PeopleController@store');
    $router->put('people/{id}/', 'PeopleController@update');
    $router->delete('people/{id}/', 'PeopleController@destory');

    // Category
    $router->get('category', 'CategoryController@index');
    $router->post('category', 'CategoryController@store');
    $router->put('category/{id}/', 'CategoryController@update');
    $router->delete('category/{id}/', 'CategoryController@destory');

    // Ledger
    $router->get('ledger', 'LedgerController@index');
    $router->post('ledger', 'LedgerController@store');
    $router->put('ledger/{id}/', 'LedgerController@update');
    $router->delete('ledger/{id}/', 'LedgerController@destory');
});