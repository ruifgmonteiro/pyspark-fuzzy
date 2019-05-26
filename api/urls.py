from django.urls import path

from . import views

urlpatterns = [
    # ex: /api/
    path('', views.index, name='index'),
    # ex: /api/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /api/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /api/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /api/companies/5
    path('companies/<int:company_id>/', views.test, name='test')
]