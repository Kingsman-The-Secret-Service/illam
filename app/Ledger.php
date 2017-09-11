<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Ledger extends Model{

 	protected $table = 'ledger';
	protected $fillable = ['family_id','user_id','type_id','category_id','date','value','description'];
}