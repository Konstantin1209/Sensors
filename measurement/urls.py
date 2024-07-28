from django.urls import path

from measurement.views import SensorView, SensorRetrieveView, MeasurementView, MeasurementRetievView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/',SensorView.as_view()),
    path('sensors/<pk>/',SensorRetrieveView.as_view()),
    path('measurements/',MeasurementView.as_view()),
    path('measurements/<pl>/',MeasurementRetievView.as_view()),



]
