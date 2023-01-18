<x-layout>
    <h1>My Blog</h1>
    @foreach ($posts as $post)
        
        <article>
            <p>
                <a href="/categories/{{ $post->category->slug }}">{{ $post->category->name }}</a>
            </p>

            <h1>
                <a href="/posts/{{ $post->slug }}">
                    {{ $post->title }}
                </a>
            </h1>
           
            <div>
                {{ $post->excerpt }}
            </div>
        </article>
    @endforeach
    
</x-layout>