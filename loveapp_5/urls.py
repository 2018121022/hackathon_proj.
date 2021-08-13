from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_5/', index_5, name="index_5"),
    path('detail_5/<str:love_id>', detail_5, name="detail_5"),
    path('write_5/', write_5, name="write_5"),
    path('update_5/<str:love_id>', update_5, name="update_5"),
    path('delete_5/<str:love_id>', delete_5, name="delete_5"),
    path('comment_5/<str:love_id>', add_comment_to_post_5, name = 'add_comment_to_post_5'),
    path('post_5/<str:love_id>', add_music_to_post_5, name="add_music_to_post_5"),
    path('question_5/<str:love_id>', add_poll_to_post_5, name="add_poll_to_post_5"),
    path('result_5/<str:question_id>', result_5, name="result_5"),
    path('vote_5/<str:question_id>', vote_5, name="vote_5"),
    path('detail_poll_5/<str:question_id>', detail_poll_5, name="detail_poll_5"),
    path('choices_5/<str:love_id>', add_choices_to_post_5, name="add_choices_to_post_5"),
    path('comment_delete_5/<str:comment_id>/', comment_delete_5, name="comment_delete_5"),
]
