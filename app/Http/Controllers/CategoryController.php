<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Hash;
use Illuminate\Http\Request;
use App\Family;
use App\User;
use App\Category;

class CategoryController extends Controller
{

    public function __construct()
    {
        $this->middleware('auth');
    }

    public function index(Request $request){

    	$user = $request->user();
        $family = $user->family;
        $category = $family->category;

    	return response()->json(['status' => 'success', 'category' => $category], 200);
    }

    public function store(Request $request){

        $this->validate($request, [
            'family_id'  => 'required|exists:family,id|int',
            'user_id' => 'required|exists:users,id|int',
            'category_id' => 'required|exists:category,id|int|unique_with:category,family_id,user_id,name',
            'name' => 'required|min:5',
            'description' => 'sometimes',
            'hexcolor' => 'sometimes'
        ]); 

        try {
            $category   = new Category;
            $category->family_id  = $request->input('family_id');
            $category->user_id  = $request->input('user_id');
            $category->category_id  = $request->input('category_id');
            $category->name  = $request->input('name');
            $category->description  = $request->input('description');
            $category->hexcolor  = $request->input('hexcolor');
            $category->save();
        }
        catch (Exception $e){

            return response()->json(['status' => 'failed', 'message' => $e],401);
        }

        return response()->json(['status' => 'success', 'message' => 'Category has been created successfully', 'category' => $category ],200);
    	
    }

    public function update(Request $request, $id){

       $this->validate($request, [
            'family_id'  => 'sometimes|exists:family,id|int',
            'user_id' => 'sometimes|exists:users,id|int',
            'category_id' => 'sometimes|exists:category,id|int|unique_with:category,family_id,user_id,name,'.$id,
            'name' => 'sometimes|min:5',
            'description' => 'sometimes',
            'hexcolor' => 'sometimes'
        ]);

        $category = Category::find($id);
        if($category->fill($request->all())->save()){

            return response()->json(['status' => 'success', 'message' => 'Category has been updated successfully', 'category' => $category], 200);
        }

        return response()->json(['status' => 'failed', 'message' => 'Category has not updated successfully'], 401);
    }

    public function destory(Request $request, $id){
        
        $category = Category::find($id);

        if(!empty($category)){

            $category->delete();

            return response()->json(['status' => 'success', 'message' => 'Category has been deleted successfully', 'category' => $category], 200);
        }

        return response()->json(['status' => 'failed', 'message' => 'Category has not deleted successfully'], 401);
    }
}