from django.urls import path

from . import views
from . import views_test

urlpatterns = [
    # ex: /monitor/
    path("", views.report, name="report"),
    # ex: /monitr/display/
    path("display/",views.display,name="display"),
    # ex: /monitor/test_async/
    path("test_async/",views_test.test_async,name="test_async"),
    # ex: /monitor/report_test/
    path("test_report/",views_test.test_report,name="test_report"),
    # ex: /monitor/report_test_async/
    path("test_report_async/",views_test.test_report_async,name="test_report_async"),
    # ex: /monitor/test_sync/
    path("test_sync/",views_test.test_sync,name="test_sync"),
    # ex: /monitor/test_site/
    path("test_site",views_test.test_site,name="test_site"),
    # ex: /report2.html/
    # path("", ReportView.as_view(), name="report2")
    # ex: /tables/
    # path("tables/",views.list,name="tables"),
    # ex: /aggre/
    # path("aggre/",views.aggre,name="aggre"),
  


    ## ex: //5/
    #path("<int:crowddata_id>/", views.detail, name="detail"),
    ## ex: //5/results/
    #path("<int:crowddata_id>/results/", views.results, name="results"),
    ## ex: //5/vote/
    #path("<int:crowddata_id>/vote/", views.vote, name="vote"),
]
