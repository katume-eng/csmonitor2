from django.urls import path

from . import views

urlpatterns = [
    # ex: //report/
    path("", views.report, name="report"),
    # ex: //tables/
    path("tables/",views.list,name="tables"),
    # ex: //aggre/
    path("aggre/",views.aggre,name="aggre"),
    # ex: //display/
    path("display/",views.display,name="display"),
    ## ex: //5/
    #path("<int:crowddata_id>/", views.detail, name="detail"),
    ## ex: //5/results/
    #path("<int:crowddata_id>/results/", views.results, name="results"),
    ## ex: //5/vote/
    #path("<int:crowddata_id>/vote/", views.vote, name="vote"),
]
