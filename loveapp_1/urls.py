from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index_1/', index_1, name="index_1"),
    path('detail_1/<str:love_id>', detail_1, name="detail_1"),
    path('write_1/', write_1, name="write_1"),
    path('update_1/<str:love_id>', update_1, name="update_1"),
    path('delete_1/<str:love_id>', delete_1, name="delete_1"),
    path('comment_1/<str:love_id>', add_comment_to_post_1, name = 'add_comment_to_post_1'),
    path('post_1/<str:love_id>', add_music_to_post_1, name="add_music_to_post_1"),
    path('question_1/<str:love_id>', add_poll_to_post_1, name="add_poll_to_post_1"),
    path('result_1/<str:question_id>', result_1, name="result_1"),
    path('vote_1/<str:question_id>', vote_1, name="vote_1"),
    path('detail_poll_1/<str:question_id>', detail_poll_1, name="detail_poll_1"),
    path('choices_1/<str:love_id>', add_choices_to_post_1, name="add_choices_to_post_1"),
    path('comment_delete_1/<str:comment_id>/', comment_delete_1, name="comment_delete_1"),
]