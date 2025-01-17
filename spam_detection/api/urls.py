from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from . views import SpamReportViewSet 


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'spam', views.SpamReportViewSet)

urlpatterns = [
    path('', views.index, name= 'index'),
    path('', include(router.urls)),
    path('spam/mark_as_spam/', views.SpamReportViewSet.as_view({'post': 'mark_as_spam'}), name='mark_as_spam'),
    path('user/search_by_name/', views.UserViewSet.as_view({'get': 'search_by_name'}), name = 'search_by_name'),
    path('user/search_by_phone/', views.UserViewSet.as_view({'get': 'search_by_phone'}), name = 'search_by_phone'),
]
