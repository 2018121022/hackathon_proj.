from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_3/', index_3, name="index_3"),
    path('detail_3/<str:love_id>', detail_3, name="detail_3"),
    path('write_3/', write_3, name="write_3"),
    path('update_3/<str:love_id>', update_3, name="update_3"),
    path('delete_3/<str:love_id>', delete_3, name="delete_3"),
    path('comment_3/<str:love_id>', add_comment_to_post_3, name = 'add_comment_to_post_3'),
    path('post_3/<str:love_id>', add_music_to_post_3, name="add_music_to_post_3"),
    path('question_3/<str:love_id>', add_poll_to_post_3, name="add_poll_to_post_3"),
    path('result_3/<str:question_id>', result_3, name="result_3"),
    path('vote_3/<str:question_id>', vote_3, name="vote_3"),
    path('detail_poll_3/<str:question_id>', detail_poll_3, name="detail_poll_3"),
    path('choices_3/<str:love_id>', add_choices_to_post_3, name="add_choices_to_post_3"),
    path('comment_delete_3/<str:comment_id>/', comment_delete_3, name="comment_delete_3"),
]
