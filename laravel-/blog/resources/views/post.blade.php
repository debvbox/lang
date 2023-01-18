<x-layout>
    <h1>
        {{ $post->title }}
    </h1>
    
    <p>
        <a href="/categories/{{ $post->category->slug }}">{{ $post->category->name }}</a>
    </p>
    {{ $post->excertp }}
    <div>
        
        <p>{{ $post->body }}</p>
    </div>
    
    <a href="{{ route('home') }}">Go back</a>
    
</x-layout>




