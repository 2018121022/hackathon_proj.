from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_2/', index_2, name="index_2"),
    path('detail_2/<str:love_id>', detail_2, name="detail_2"),
    path('write_2/', write_2, name="write_2"),
    path('update_2/<str:love_id>', update_2, name="update_2"),
    path('delete_2/<str:love_id>', delete_2, name="delete_2"),
    path('comment_2/<str:love_id>', add_comment_to_post_2, name = 'add_comment_to_post_2'),
    path('post_2/<str:love_id>', add_music_to_post_2, name="add_music_to_post_2"),
    path('question_2/<str:love_id>', add_poll_to_post_2, name="add_poll_to_post_2"),
    path('result_2/<str:question_id>', result_2, name="result_2"),
    path('vote_2/<str:question_id>', vote_2, name="vote_2"),
    path('detail_poll_2/<str:question_id>', detail_poll_2, name="detail_poll_2"),
    path('choices_2/<str:love_id>', add_choices_to_post_2, name="add_choices_to_post_2"),
    path('comment_delete_2/<str:comment_id>/', comment_delete_2, name="comment_delete_2"),
]
