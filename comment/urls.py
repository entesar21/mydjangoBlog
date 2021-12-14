from django.urls import path

import comment.views


urlpatterns = [
    path('', comment.views.comments),
    #path('comments/', comment.views.comments),
    path('new_comment/', comment.views.new_comment),

]
