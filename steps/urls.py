from django.urls import path

from . import views

app_name = "steps"

urlpatterns = [
    path('', views.home),
    path('job_title/save/', views.save_work_title, name="save_work_title"),
    path('work_experience/save/', views.save_work_experience, name="save_work_experience"),
    path('opportunity/save/', views.save_opportunity_available, name="save_opportunity")
]
