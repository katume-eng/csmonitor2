from django.db import models
import datetime
from django.utils import timezone

#CrowdDataモデル。データベースの構造を決定
# 1.location 場所のデータをchoiceで管理
# 2.crowd_lavel 混雑度をint整数値で管理
# 3.pub_date 定義された時間を管理
# def __str__ : crowddateを返す関数
# def was_publish.. : 直近のクエリかどうか

#####locationの詳細定義 場所＝プログラム名で定義
S44 = "S44"
CM3 = "COMMUNICATIONCAT3"
GML = "GEOROGYLABOLATORY"
S43 = "S43"
SRS = "理科調査研究室"
S70 = "S70"
S71 = "S71"
S72 = "S72"
S73 = "S73"
S74 = "S74"
#####

lp_map = {
    S44 : "TOMIKEN",
    CM3 : "プログラム名",
    GML : "地球の正体",
    S43 : "S43",
    SRS : "理科調査研究室",
    S70 : "S70",
    S71 : "S71",
    S72 : "S72",
    S73 : "S73",
    S74 : "S74",

}


class CrowdData(models.Model):

    #####選択肢の定義
    LOCATION_CHOICE = dict(lp_map)
    #####

    location = models.CharField(max_length=20,choices=LOCATION_CHOICE)
    crowd_level = models.IntegerField("Crowd Level")
    pub_date = models.DateTimeField("pub_date",default=timezone.now)

    # localtimeにしてAsia/Tokyoに合わせる modelは時間をUTCで保存するらしい
    def __str__(self):
        return f'{self.location} - {self.crowd_level} at {timezone.localtime(self.pub_date)}'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(hours=1)

