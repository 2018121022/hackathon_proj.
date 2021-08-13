from django.contrib import admin
from .models import Love, Comment, Post, Question, Choice
from embed_video.admin import AdminVideoMixin
# , Question, Choice

# Register your models here.
admin.site.register(Love)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Choice)

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video')

admin.site.register(Post, PostAdmin)
