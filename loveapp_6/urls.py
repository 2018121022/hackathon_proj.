from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_6/', index_6, name="index_6"),
    path('detail_6/<str:love_id>', detail_6, name="detail_6"),
    path('write_6/', write_6, name="write_6"),
    path('update_6/<str:love_id>', update_6, name="update_6"),
    path('delete_6/<str:love_id>', delete_6, name="delete_6"),
    path('comment_6/<str:love_id>', add_comment_to_post_6, name = 'add_comment_to_post_6'),
    path('post_6/<str:love_id>', add_music_to_post_6, name="add_music_to_post_6"),
    path('question_6/<str:love_id>', add_poll_to_post_6, name="add_poll_to_post_6"),
    path('result_6/<str:question_id>', result_6, name="result_6"),
    path('vote_6/<str:question_id>', vote_6, name="vote_6"),
    path('detail_poll_6/<str:question_id>', detail_poll_6, name="detail_poll_6"),
    path('choices_6/<str:love_id>', add_choices_to_post_6, name="add_choices_to_post_6"),
    path('comment_delete_6/<str:comment_id>/', comment_delete_6, name="comment_delete_6"),
]