<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Ledger extends Model{
	
	use SoftDeletes;

 	protected $table = 'ledger';
	protected $fillable = ['family_id','user_id','type_id','category_id','date','value','description'];
	protected $hidden = [
        'created_at', 'updated_at', 'deleted_at'
    ];

	public function family(){

		return $this->belongsTo('App\Family');
	}

	public function user(){

		return $this->belongsTo('App\User');
	}

	public function type(){

		return $this->belongsTo('App\Type');
	}
}