from django.urls import path

from app.views import AppCreateView, AppListView, AppDetailView, AppUpdateView
from app import views


urlpatterns = [
    path('test/<api_key>/', views.appDetailJSON, name='detail-json'),
    path('generate-api-key/<int:id_app>', views.generate_key, name='generate-key'),
    path('all/', AppListView.as_view(), name='all-apps'),
    path('create/', AppCreateView.as_view(), name='create_app'),
    path('detail/<int:pk>/', AppDetailView.as_view(), name='detail-app'),
    path('update/<int:pk>/', AppUpdateView.as_view(), name='update-app')
]
