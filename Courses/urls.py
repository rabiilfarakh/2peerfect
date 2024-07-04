from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('list/', CourseViewSet.as_view({'get': 'list'}), name='course_list'),
    path('create/', CourseViewSet.as_view({'post': 'create'}), name='course_create'),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='course_detail'),
    path('update/<int:pk>/', CourseViewSet.as_view({'put': 'update'}), name='course_update'),
    path('partial_update/<int:pk>/', CourseViewSet.as_view({'patch': 'partial_update'}), name='course_partial_update'),
    path('delete/<int:pk>/', CourseViewSet.as_view({'delete': 'destroy'}), name='course_delete'),
]

urlpatterns += router.urls

# This setup ensures your API endpoints will be as follows:

# POST /api/courses/create/ to create a new course.
# GET /api/courses/list/ to list all courses.
# GET /api/courses/<int:pk>/ to retrieve a specific course.
# PUT /api/courses/update/<int:pk>/ to update a specific course.
# PATCH /api/courses/partial_update/<int:pk>/ to partially update a specific course.
# DELETE /api/courses/delete/<int:pk>/ to delete a specific course.