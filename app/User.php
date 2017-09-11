<?php

namespace App;

use Illuminate\Auth\Authenticatable;
use Laravel\Lumen\Auth\Authorizable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
use Illuminate\Contracts\Auth\Access\Authorizable as AuthorizableContract;

class User extends Model implements AuthenticatableContract, AuthorizableContract
{
    use Authenticatable, Authorizable;

    protected $fillable = [
        'family_id','name', 'email','phone', 'password', 'image', 'api_token'
    ];

    protected $hidden = [
        'password', 'created_at', 'updated_at', 'deleted_at'
    ];

    public function family(){

        return $this->belongsTo('App\Family');
    }
}
