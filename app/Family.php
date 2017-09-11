<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Family extends Model{

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
}