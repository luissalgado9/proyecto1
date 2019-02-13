from django.conf.urls import url, include
from pagina1.views import home

urlpatterns = [
	url(r'^$', home, name='home'),
]