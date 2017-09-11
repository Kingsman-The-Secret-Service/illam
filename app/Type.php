<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Type extends Model{

 	protected $table = 'type';
	protected $fillable = ['name','hexcolor','icon'];

	public function ledger(){

		return $this->hasMany('App\Ledger');
	}
}