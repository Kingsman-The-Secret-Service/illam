<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Category extends Model{

	use SoftDeletes;

 	protected $table = 'category';
	protected $fillable = ['family_id','user_id','category_id','name','description','hexcolor'];
	protected $hidden = [
        'created_at', 'updated_at', 'deleted_at'
    ];

	public function ledger(){

		return $this->hasMany('App\Ledger');
	}

    public function family(){

        return $this->belongsTo('App\Family');
    }
}