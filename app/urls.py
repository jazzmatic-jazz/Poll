from django.urls import path
from .views import DetailView, ResultsView, vote, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
