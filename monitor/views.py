from django.http import HttpResponse
from .forms import DataForm
from .models import CrowdData
from .models import lp_map,status_map,ln_map
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg,Q,Count
import datetime
from numpy import percentile
# from django.views.generic.edit import FormView

# event
def report(request, event_name_short):
    ok = "送信に成功しました!データの提供ありがとうございます"
    nok = "送信に失敗しました!不適切なデータがあります"
    url_report = "monitor/report.html"
    

    initial_value = {"location":ln_map[event_name_short],"crowd_level":0}

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            form = DataForm(initial_value)  # 正しく初期化
            message = ok
        else:
            form = DataForm(initial_value)  # 正しく初期化
            message = nok
    else:
        form = DataForm(initial_value)  # 正しく初期化
        message = ""

    return render(request, url_report, {"form": form, "message": message})

def report_none(request):
    ok = "送信に成功しました!データの提供ありがとうございます"
    nok = "送信に失敗しました!不適切なデータがあります"
    url_report = "monitor/report.html"

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            form = DataForm()  # 正しく初期化
            message = ok
        else:
            form = DataForm()  # 正しく初期化
            message = nok
    else:
        form = DataForm()  # 正しく初期化
        message = ""

    return render(request, url_report, {"form": form, "message": message})


def display(request):
    now = timezone.now()
    last_30_minutes = CrowdData.objects.filter(
        pub_date__gte = now - datetime.timedelta(minutes=20)# 今は20分です
    )
    # eld = each_location_data ( location, program_name, crowd_level)
    # loc = location
    eld = []
    for loc in lp_map:
        location_data = last_30_minutes.filter(location=loc)
        
        if location_data.exists():
            # Crowd level dataのリストを取得
            crowd_levels = list(location_data.values_list('crowd_level', flat=True))
            # 四分位範囲を計算
            Q1 = percentile(crowd_levels, 25)
            Q3 = percentile(crowd_levels, 75)
            IQR = Q3 - Q1
            # 外れ値の閾値
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            # 外れ値を除外
            filtered_data = location_data.filter(
                Q(crowd_level__gte=lower_bound) & Q(crowd_level__lte=upper_bound)
            )
            
            crowd_level_aggregated = filtered_data.aggregate(crowd_level_avg=Avg('crowd_level'))
            crowd_level_perfect = int(crowd_level_aggregated["crowd_level_avg"] * 10) / 10 if crowd_level_aggregated["crowd_level_avg"] is not None else None
            crowd_level_counted = filtered_data.count()

        else:
            crowd_level_perfect = None
            crowd_level_counted = 0
        eld.append([lp_map[loc], loc, crowd_level_perfect, crowd_level_counted, status_map[loc][0], status_map[loc][1]])

    context = {
        "model": eld,
    }
    return render(request, "monitor/display.html", context)
# class viewを用いたview
# class ReportView(FormView):
#     template_name = "monitor/report2.html"
#     form_class = DataForm
#     success_message = "送信に成功しました。データの提供ありがとうございます"
#     failure_message = "足りないデータがあるか、不適切なデータがあります"
#     initial_message = "データを入力してボタンを押してください。levelは0~10で入力してください"
# 
#     def form_valid(self, form):
#         form.save()
#         return self.render_to_response(self.get_context_data(form=self.form_class(), message=self.success_message))
# 
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=self.form_class(), message=self.failure_message))
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if 'message' not in context:
#             context['message'] = self.initial_message
#         return context

# def list(request):
#     qs = CrowdData.objects.all()
#     context = {}
#     context["model"] = qs
#     return render(request,"monitor/tables.html",context)
# 
# # 計算view.1時間以内のデータかどうかを考える
# def aggre(request):
#     now = timezone.now()
#     last_1_hour = CrowdData.objects.filter(
#         pub_date__gte = now - datetime.timedelta(hours=1)
#     )
#     context = {}
#     context["model"] = last_1_hour
#     return render(request,"monitor/aggre.html",context)


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

