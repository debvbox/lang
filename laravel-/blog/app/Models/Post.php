<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    public function getRouteKeyName()
    {
        return 'slug';
    }

    protected $guarded = [];

    //add relationship

    public function category(){
        //hasOne, hasMany,belongsTo,belongsToMany
        return $this->belongsTo(Category::class);
    }
}
