from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


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

# locationと(0,列情報 1,混雑情報)
lr_map = {
    S44 : 1,
    CM3 : 1,
    GML : 0,
    S43 : 1,
    SRS : 1,
    S70 : 1,
    S71 : 1,
    S72 : 1,
    S73 : 0,
    S74 : 0,
}


class CrowdData(models.Model):

    #####選択肢の定義
    LOCATION_CHOICE = dict(lp_map)
    #####

    location = models.CharField("場所",max_length=20,choices=LOCATION_CHOICE)
    crowd_level = models.IntegerField("混雑状況もしくは並び時間",validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateTimeField("pub_date",default=timezone.now)

    # localtimeにしてAsia/Tokyoに合わせる modelは時間をUTCで保存するらしい
    def __str__(self):
        return f'{self.location} - {self.crowd_level} at {timezone.localtime(self.pub_date)}'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(hours=1)

