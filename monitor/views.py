from django.http import HttpResponse
from .forms import DataForm
from .models import CrowdData
from .models import lp_map,lr_map
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
import datetime




def report(request):
    init_str = "データを入力してボタンを押してください。levelは0~10で入力してください"
    ok = "送信に成功しました。データの提供ありがとうございます"
    nok = "足りないデータがあるか、不適切なデータがあります"
    url_report = "monitor/report.html"
    form = DataForm()

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid:
            form.save()
            form = DataForm()
            return render(request, url_report, {"form":form,"message":ok})
        
        else:
            form = DataForm()
            return render(request, url_report, {"form":form,"message":nok})
        
    #else:エラーでも吐いとけ

    return render(request, url_report, {"form":form,"message":init_str})


def list(request):
    qs = CrowdData.objects.all()
    context = {}
    context["model"] = qs
    return render(request,"monitor/tables.html",context)

# 計算view.1時間以内のデータかどうかを考える
def aggre(request):
    now = timezone.now()
    last_1_hour = CrowdData.objects.filter(
        pub_date__gte = now - datetime.timedelta(hours=1)
    )
    context = {}
    context["model"] = last_1_hour
    return render(request,"monitor/aggre.html",context)

def display(request):
    now = timezone.now()
    last_1_hour = CrowdData.objects.filter(
        pub_date__gte = now - datetime.timedelta(hours=1)
    )
    # eld = each_location_data ( location, program_name, crowd_level)
    # loc = location
    eld = []
    for loc in lp_map:
        crowd_level_aggregated = last_1_hour.filter(location=loc).aggregate(crowd_level_avg=Avg('crowd_level'))
        crowd_level_counted = last_1_hour.filter(location=loc).count()
        if crowd_level_aggregated["crowd_level_avg"] is not None:
            crowd_level_perfect = int(crowd_level_aggregated["crowd_level_avg"]*10)/10
        else:
            crowd_level_perfect = None
        eld.append([lp_map[loc],loc , crowd_level_perfect,crowd_level_counted,lr_map[loc]])

    context = {
        "model":eld,
    }
    return render(request,"monitor/display.html",context)

#    仮
#    if request.method == 'POST':
#        form = DataForm(request.POST)
#        if form.is_valid():
#            # フォームからモデルインスタンスを作成（まだ保存しない）
#            instance = form.save(commit=False)
#            # インスタンスのフィールドに追加の値を設定
#            instance.pub_date = timezone.now()
#            # インスタンスをデータベースに保存
#            instance.save() 
#            form = DataForm()  # フォームを再生成して空にする
#
#    else:
#        model = CrowdData()
#    form = DataForm()
#    model_que = CrowdData.objects.all()


# in チュートリアル
# -pub_dateで並び替えて5個とる。それをリストで返す
#
#def index(request):
#    latest_crowddata_list = CrowdData.objects.order_by("-pub_date")[:5]
#    context = {"latest_crowddata_list": latest_crowddata_list}
#    return render(request, "monitor/index.html", context)
#
#def detail(request, crowddata_id):
#    return HttpResponse("You're looking at monitor %s." % crowddata_id)
#
#
#def results(request, crowddata_id):
#    response = "You're looking at the results of monitor %s."
#    return HttpResponse(response % crowddata_id)
#
#
#def vote(request, crowddata_id):
#    return HttpResponse("You're voting on monitor %s." % crowddata_id)
#
#
############
#むずかったらチュートリアルは無視かな。ネットでいろいろ調べようね
############

