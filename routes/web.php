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

    // Ledger
    $router->get('ledger', 'LedgerController@index');
    $router->post('ledger', 'LedgerController@store');
    $router->put('ledger/{id}/', 'LedgerController@update');
    $router->delete('ledger', 'LedgerController@destory');
});