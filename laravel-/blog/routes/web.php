<?php

use App\Models\Category;
use App\Models\Post;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('posts', [
        'posts' => Post::with('category')->get()
    ]);
})->name('home');

// Route::get('/posts/{post:slug}', function (Post $post) { //Post::where('slug',$post)->firstOrFail()
//     return view('post', [
//         'post' => $post
//     ]);
// });

//must be addedd in model Post.php the function
/**
 * public function getRouteKeyName()
 *  {
 *      return 'slug'; 'field to be the route key
 *  }
 */
Route::get('/posts/{post}', function (Post $post) { //Post::where('slug',$post)->firstOrFail()
    return view('post', [
        'post' => $post
    ]);
});

Route::get('categories/{category:slug}',function (Category $category){
    return view('posts',[
        'posts' => $category->posts
    ]);
});
