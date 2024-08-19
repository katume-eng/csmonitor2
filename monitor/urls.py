from django.urls import path

from . import views

urlpatterns = [
    # ex: /monitor/report/
    path("report/", views.report, name="report"),
    # ex: /monitor/tables/
    path("tables/",views.list,name="tables"),
    # ex: /monitor/aggre/
    path("aggre/",views.aggre,name="aggre"),
    # ex: /monitor/display/
    path("display/",views.display,name="display"),
    ## ex: /monitor/5/
    #path("<int:crowddata_id>/", views.detail, name="detail"),
    ## ex: /monitor/5/results/
    #path("<int:crowddata_id>/results/", views.results, name="results"),
    ## ex: /monitor/5/vote/
    #path("<int:crowddata_id>/vote/", views.vote, name="vote"),
]
