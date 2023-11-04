from django.urls import path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('all-docs', views.AllDocs, 'all-docs')
router.register(
    'doc-reviews/(?P<medico_id>[\d]+)', views.DocReviews, 'doc-reviewsxx')
router.register(
    'doc-reviewsReorg/(?P<medico_id>[\d]+)', views.DocReviewsReorg, 'doc-reviewsReorg')
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('ws/asyncReviews2/<int:medico_id>/',
         views.DocReviews.aList, name='xasyncDocReviews'),
    path('ws/asyncReviews3/<int:medico_id>/',
         views.DocReviewsReorg.aList, name='xasyncDocReviewsReorg'),
]


urlpatterns += router.urls
a = 9
