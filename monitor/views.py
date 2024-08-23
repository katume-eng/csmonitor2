from django.http import HttpResponse
from .forms import DataForm
from .models import CrowdData
from .models import lp_map,lr_map
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
import datetime
# from django.views.generic.edit import FormView


def report(request):
    init_str = "データを入力してボタンを押してください。levelは0~10で入力してください"
    ok = "送信に成功しました。データの提供ありがとうございます"
    nok = "足りないデータがあるか、不適切なデータがあります"
    url_report = "monitor/report.html"
    form = DataForm()

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            form = DataForm()
            return render(request, url_report, {"form":form,"message":ok})
        else:
            form = DataForm()
            return render(request, url_report, {"form":form,"message":nok})

    return render(request, url_report, {"form":form,"message":init_str})

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

import time
import httpx
import asyncio
import requests

times_of_requests = [10, 20, 50, 100, 200, 500]
test_site_url = 'http://localhost:8003/test_site/'

async def test_async(request):
    async with httpx.AsyncClient() as client:
        for n in times_of_requests:
            start_time = time.time()
            tasks = [client.get(test_site_url) for _ in range(n)]
            responses = await asyncio.gather(*tasks)
            end_time = time.time()
            print(f"Total time for {n} async requests: {end_time - start_time:.2f} seconds")

def test_sync(request):
    for n in times_of_requests:
        responses = []
        start_time = time.time()
        for _ in range(n):
            responses.append(requests.get(test_site_url))
        end_time = time.time()
        print(f"Total time for {n} sync requests: {end_time - start_time:.2f} seconds")
        time.sleep(2)
    print('the end of test')

def test_site(request):
    return HttpResponse('OK')


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

