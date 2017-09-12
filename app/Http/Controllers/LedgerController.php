<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Hash;
use Illuminate\Http\Request;
use App\Family;
use App\User;

class LedgerController extends Controller
{

	/**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    public function index(Request $request){

    	$user = $request->user();
        // $user->family->ledger;
        // $user->ledger;

    	return response()->json(['status' => 'success', 'ledger' => $user], 200);
    }

    public function store(Request $request){

    	
    }

    public function update(Request $request, $id){

    
    }

    public function destory(Request $request, $id){
        
    }
}