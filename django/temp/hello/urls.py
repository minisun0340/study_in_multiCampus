from django_request_mapping import UrlPattern

from hello.views import MyView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);