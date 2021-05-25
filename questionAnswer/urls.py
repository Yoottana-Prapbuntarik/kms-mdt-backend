from django.urls import path
# from . import views
from .api import PostQuestionAPI, QuestionContentViewAllAPI , QuestionCommentAPI, GetCommentQuestionViewAPI
urlpatterns = [
    path('api/question', PostQuestionAPI.as_view()),
    path('api/question/all', QuestionContentViewAllAPI.as_view()),
    path('api/question/comment', QuestionCommentAPI.as_view()),
    path('api/question/comment/all/<int:pk>', GetCommentQuestionViewAPI.as_view()),
]