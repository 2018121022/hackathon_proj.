from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_4/', index_4, name="index_4"),
    path('detail_4/<str:love_id>', detail_4, name="detail_4"),
    path('write_4/', write_4, name="write_4"),
    path('update_4/<str:love_id>', update_4, name="update_4"),
    path('delete_4/<str:love_id>', delete_4, name="delete_4"),
    path('comment_4/<str:love_id>', add_comment_to_post_4, name = 'add_comment_to_post_4'),
    path('post_4/<str:love_id>', add_music_to_post_4, name="add_music_to_post_4"),
    path('question_4/<str:love_id>', add_poll_to_post_4, name="add_poll_to_post_4"),
    path('result_4/<str:question_id>', result_4, name="result_4"),
    path('vote_4/<str:question_id>', vote_4, name="vote_4"),
    path('detail_poll_4/<str:question_id>', detail_poll_4, name="detail_poll_4"),
    path('choices_4/<str:love_id>', add_choices_to_post_4, name="add_choices_to_post_4"),
    path('comment_delete_4/<str:comment_id>/', comment_delete_4, name="comment_delete_4"),
]
