from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import MurrCardView, EditorImageForMurrCardView, EditorDataForMurrView

urlpatterns = [
    path('', MurrCardView.as_view(), name='MurrCardView'),
    path('save_editor_image/', csrf_exempt(EditorImageForMurrCardView.as_view()), name='save_editor_image'),
    path('save_data_for_murr_card/', csrf_exempt(EditorDataForMurrView.as_view()), name='save_data_for_murr_card'),
]
