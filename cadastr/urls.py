from django.urls import path
from .views import (
    CadastrRecordAPICreate,
    CadastrAllRecordsAPIList,
    PingView,
    HistoryRecordsAPIList)


urlpatterns = [
    path('query/', CadastrRecordAPICreate.as_view(), name='query'),
    path('result/', CadastrAllRecordsAPIList.as_view(), name='result'),
    path('ping/', PingView.as_view(), name='ping'),
    path('history/', HistoryRecordsAPIList.as_view(), name='history'),

]
