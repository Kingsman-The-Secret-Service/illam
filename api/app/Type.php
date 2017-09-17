<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Type extends Model{
	
	use SoftDeletes;

 	protected $table = 'type';
	protected $fillable = ['name','hexcolor','icon'];

	public function ledger(){

		return $this->hasMany('App\Ledger');
	}
}