from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # Index View
    url(r'^$', views.index, name="index"),
    url(r'^index.html$', RedirectView.as_view(url="/")),

    # Login View
    url(r'^login/$', views.login, name="login"),
    url(r'^login.html$', RedirectView.as_view(url="/login/")),
]