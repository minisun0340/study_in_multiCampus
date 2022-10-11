from django_request_mapping import UrlPattern

from layout.views import MyView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);