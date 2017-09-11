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
        $user->ledger;

    	return response()->json(['status' => 'success', 'ledger' => $user], 200);
    }

    public function store(Request $request){

    	$this->validate($request, [
            'name'  => 'required|min:5',
            'hexcolor' => 'sometimes'
        ]); 

        try {
            $family   = new Family;
            $family->name  = $request->input('name');
            $family->hexcolor  = $request->input('hexcolor');
            $family->save();
        }
        catch (Exception $e){

            return response()->json(['status' => 'failed', 'message' => $e],401);
        }

        return response()->json(['status' => 'success', 'message' => 'Family has been created successfully', 'family' => $family ],200);
    }

    public function update(Request $request, $id){

        $this->validate($request, [
            'name'  => 'required|min:5',
            'hexcolor' => 'sometimes'
        ]);

        $family = Family::find($id);
        if($family->fill($request->all())->save()){

            return response()->json(['status' => 'success', 'message' => 'Family has been updated successfully', 'family' => $family], 200);
        }

        return response()->json(['status' => 'failed', 'message' => 'Family has not updated successfully'], 401);
    }
}