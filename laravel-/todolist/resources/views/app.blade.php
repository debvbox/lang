@extends('layouts.base')

@section('content')
    <form action="{{ route('todoscreate') }}" method="POST">
        @csrf

        @if (session('success'))
            <h6 class="alert alert-success">{{ session('success') }}</h6>
        @endif
        @error('title')
            <h6 class="alert alert-danger">{{ $message }}</h6>
        @enderror
        <div class="mb-3">
            <label for="title" class="form-label">Title</label>
            <input type="text" name="title" class="form-control">
        </div>
        
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div class="container">
        <ul>
            @foreach ($todos as $todo )
            <li> {{ $todo['title'] }}</li>
            @endforeach
        </ul>
        

    </div>
@endsection
