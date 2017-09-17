<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Family extends Model{
	
	use SoftDeletes;

 	protected $table = 'family';
	protected $fillable = ['name','hexcolor'];
	protected $hidden = [
        'created_at', 'updated_at', 'deleted_at'
    ];

	public function user(){

		return $this->hasMany('App\User');
	}

	public function ledger(){

		return $this->hasMany('App\Ledger');
	}

	public function category(){

		return $this->hasMany('App\Category');
	}
}