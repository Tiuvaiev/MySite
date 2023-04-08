from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('contacts/', views.contacts, name="contacts"),
    path('repair/', views.repair, name="repair"),
    path('repair_iphone/', views.repair_iphone, name="repair_iphone"),
    path('repair_ipod/', views.repair_ipod, name="repair_ipod"),
    path('repair_ipad/', views.repair_ipad, name="repair_ipad"),
    path('repair_imac/', views.repair_imac, name="repair_imac"),
    path('repair_macbook/', views.repair_macbook, name="repair_macbook"),
    path('repair_watch/', views.repair_watch, name="repair_watch"),

    path('repair_14ProMax/', views.repair_14ProMax, name="repair_14ProMax"),
    path('repair_14Pro/', views.repair_14Pro, name="repair_14Pro"),
    path('repair_14Plus/', views.repair_14Plus, name="repair_14Plus"),
    path('repair_14/', views.repair_14, name="repair_14"),

    path('repair_13ProMax/', views.repair_13ProMax, name="repair_13ProMax"),
    path('repair_13Pro/', views.repair_13Pro, name="repair_13Pro"),
    path('repair_13Mini/', views.repair_13Mini, name="repair_13Mini"),
    path('repair_13/', views.repair_13, name="repair_13"),

    path('repair_12ProMax/', views.repair_12ProMax, name="repair_12ProMax"),
    path('repair_12Pro/', views.repair_12Pro, name="repair_12Pro"),
    path('repair_12/', views.repair_12, name="repair_12"),
    path('repair_12Mini/', views.repair_12Mini, name="repair_12Mini"),

    path('repair_11ProMax/', views.repair_11ProMax, name="repair_11ProMax"),
    path('repair_11Pro/', views.repair_11Pro, name="repair_11Pro"),
    path('repair_11/', views.repair_11, name="repair_11"),

    path('repair_XsMax/', views.repair_XsMax, name="repair_XsMax"),
    path('repair_Xs/', views.repair_Xs, name="repair_Xs"),
    path('repair_X/', views.repair_X, name="repair_X"),
    path('repair_Xr/', views.repair_Xr, name="repair_Xr"),

    path('repair_SE/', views.repair_SE, name="repair_SE"),
    path('repair_SE2/', views.repair_SE2, name="repair_SE2"),

    path('repair_8Plus/', views.repair_8Plus, name="repair_8Plus"),
    path('repair_8/', views.repair_8, name="repair_8"),

    path('repair_7Plus/', views.repair_7Plus, name="repair_7Plus"),
    path('repair_7/', views.repair_7, name="repair_7"),

    path('repair_6SPlus/', views.repair_6sPlus, name="repair_6sPlus"),
    path('repair_6s/', views.repair_6s, name="repair_6s"),
    path('repair_6Plus/', views.repair_6Plus, name="repair_6Plus"),
    path('repair_6/', views.repair_6, name="repair_6"),

    path('repair_5s/', views.repair_5s, name="repair_5s"),
    path('repair_5c/', views.repair_5c, name="repair_5c"),

]
