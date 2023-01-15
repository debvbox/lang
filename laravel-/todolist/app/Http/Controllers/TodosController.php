<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Todo;

class TodosController extends Controller
{
    /**
     * index para mostrar todo
     * store para guatdar un todo
     * Update para actualizar todo
     * Destory para eliminar todo
     * edit para mostrar el formulario en modo edicion
     */

    public function store(Request $request){
        $request->validate([
            'title' => 'required|min:3'
        ]);

        $todo = new Todo;
        $todo->title = $request->title;
        $todo->save();

        return redirect()->route('todos')->with('success','Tara creada correctamente');
    }

    public function index(){
        $todos = Todo::all();

        return view('app',[
            'todos' => $todos 
        ]);
    }
}
