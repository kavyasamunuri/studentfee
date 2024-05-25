from django.urls import include, path
from app import views
import project1


urlpatterns=[
   path('addTask/',views.addTask,name='addTask'),
   path('mark_as_Paid/<int:pk>/',views.mark_as_paid,name='mark_as_paid'),
   path('mark_as_unpaid/<int:pk>/',views.mark_as_unpaid,name='mark_as_unpaid'),
   path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
   path('delete_task/<int:pk>/',views.delete_task,name='delete_task')
]
