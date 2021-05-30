from django.urls import path
from . import views
from .api import BlogAPI, BlogContentViewAPI, BlogContentViewAllAPI, BlogCategoryAPI, BlogDetailAPI, GetBlogCommentViewAPI, BlogCommentAPI, BlogByCategoryItem, DeleteBlog, BlogUpdate, LikeAndUnlikeApi, GetLikeAll, GetLikeByIdApi, GetBlogAllUser, UpdateComment, DeleteComment, GetBlogCommentViewByIdAPI
urlpatterns = [
    path('api/blog', BlogAPI.as_view()),
    path('api/blog/all', BlogContentViewAllAPI.as_view()),
    path('api/blog/get', BlogContentViewAPI.as_view()),
    path('api/blog/<int:pk>', BlogDetailAPI.as_view()),
    path('api/blog/category', BlogCategoryAPI.as_view()),
    path('api/blog/comment', BlogCommentAPI.as_view()),
    path('api/blog/comment/all/<int:pk>', GetBlogCommentViewAPI.as_view()),
    path('api/blog/content/category/<int:category_name>', BlogByCategoryItem.as_view()),
    path('api/blog/user', GetBlogAllUser.as_view()),
    # Delete or update blog
    path('api/blog/update/<int:pk>',BlogUpdate.as_view()),
    path('api/blog/delete/<int:pk>',DeleteBlog.as_view()),

    # Delete or update comment
    path('api/blog/comment/update/<int:pk>',UpdateComment.as_view()),
    path('api/blog/comment/delete/<int:pk>',DeleteComment.as_view()),
    path('api/blog/comment/get/<int:pk>',GetBlogCommentViewByIdAPI.as_view()),


    # Like
    path('api/blog/like/<int:pk>', LikeAndUnlikeApi.as_view()),
    path('api/blog/like', GetLikeAll.as_view()),
    path('api/like/<int:pk>', GetLikeByIdApi.as_view()),

    # view
    path('category-form', views.uploadFileCategory, name="category-form"),

]
