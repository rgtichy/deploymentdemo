from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^push$', views.randomWordButton),
	url(r'^', views.randomWord),
	url(r'^isplay$', views.index)
]
    # url(r'^users', views.show_users)
    # url(r'^admin/', admin.site.urls),
