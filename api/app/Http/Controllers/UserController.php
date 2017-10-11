<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Hash;
use Illuminate\Http\Request;
use App\Family;
use App\User;

class UserController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        //  $this->middleware('auth:api');
        $this->middleware('auth', ['except' => [
            'store',
            'authenticate',
        ]]);
    }

    public function index(Request $request){

        $request->user()->family;

        return response()->json(['user' => $request->user()], 200);
    }

    public function store(Request $request){ 

        $this->validate($request, [
            'family_name'  => 'required|min:5',
            'hexcolor' => 'sometimes',
            'email'  => 'required|email|unique:users',
            'password' => 'required|min:6',
            'name'  => 'required|min:5',
            'phone' => 'required|min:11|numeric|unique:users',
            'image' => 'sometimes'
        ]); 

        try {

            $family   = new Family;
            $family->name  = $request->input('family_name');
            $family->hexcolor  = $request->input('hexcolor');
            $family->save();

            $user   = new User;
            $user->family_id = $family->id;
            $user->email  = $request->input('email');
            $user->password  = Hash::make($request->input('password'));
            $user->name  = $request->input('name');
            $user->phone  = $request->input('phone');
            $user->save();
        }
        catch (Exception $e){

            return response()->json(['error' => $e], 401);
        }

        $apiToken = $this->generateToken($user);
        return response()->json(['message' => 'User has been created successfully','user' => $user, 'family' => $family], 200);

    }

    public function update(Request $request, $id){

        $this->validate($request, [
            'family_name' => 'sometimes|min:5',
            'email'  => 'sometimes|email|unique:users,email,'.$id,
            'password' => 'sometimes|min:6',
            'name'  => 'sometimes|min:5',
            'phone' => 'sometimes|min:11|numeric|unique:users,phone,'.$id,
            'image' => 'sometimes',
        ]);

        $user = User::find($id);
        if($user->fill($request->all())->save()){

            return response()->json(['message' => 'User has been updated successfully', 'user' => $user], 200);
        }

        return response()->json(['error' => 'User has not updated successfully'], 401);
    }

    public function authenticate(Request $request)
    {
 
        $this->validate($request, [
           'email' => 'required|email',
           'password' => 'required|min:6'
        ]);
 
        $user = User::where('email', $request->input('email'))->first();
    
        if(!empty($user)){
            if(Hash::check($request->input('password'), $user->password)){
     
                $apiToken = $this->generateToken($user);
     
                return response()->json(['user' => $user], 200);
     
            }else{
     
              return response()->json(['error' => 'Invalid credentials'], 401);
            }
        }else{

            return response()->json(['error' => 'User doesn\'t exists'], 401);
        }

 
    }

    public function generateToken($user){

        $apiToken = base64_encode(str_random(40));

        $user->update(['api_token' => "$apiToken"]);

        return $apiToken;
    }
}
