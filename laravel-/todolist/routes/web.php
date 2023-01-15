<?php

use App\Models\Todo;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TodosController;

Route::get('/', function () {
    return view('index');
});

Route::get('/todos',[TodosController::class,'index'])->name('todos');

Route::post('/todoscreate',[TodosController::class,'store'])->name('todoscreate');
