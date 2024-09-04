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
S45 = "S45"
JK1 = "情報教室1"
E3P = "1F生徒昇降口付近,3FS34前PCラウンジ"
S46 = "S46"
S3W = "S37,S38"
CMC = "コミュニケーションコート_パフェ"
JAK = "柔剣道場"
BOL = "生物実験室"
C31 = "C31"
SHR = "視聴覚室"
HOL_D = "ホール"
S21_L = "S21,図書室"
S55 = "S55"
CMC_3 = "コミュニケーションコート_ベビーカステラ"
S36 = "S36"
#####

ln_map ={
    "S45" : "S45",
    "JK1" : "情報教室1",
    "E3P" : "1F生徒昇降口付近,3FS34前PCラウンジ",
    "S46" : "S46",
    "S3W" : "S37,S38",
    "CMC" : "コミュニケーションコート_パフェ",
    "JAK" : "柔剣道場",
    "BOL" : "生物実験室",
    "C31" : "C31",
    "SHR" : "視聴覚室",
    "HOL_D" : "ホール",
    "S21_L" : "S21,図書室",
    "S55" : "S55",
    "CMC_3" : "コミュニケーションコート_ベビーカステラ",
    "S36" : "S36",
}

lp_map = {
    S45 : "根城はサイコロを振らない",
    JK1 : "情報工学部 ゲーム展",
    E3P : "緑の羽根募金",
    S46 : "ふっ、おもしれーゲーム",
    S3W : "ロボパーティーForBetting",
    CMC : "パフェって504通りあんねん",
    JAK : "トレトレかるた",
    BOL : "いっつぁまいくろわーるど_生物実験室",
    C31 : "いっつぁまいくろわーるど_C31",
    SHR : "驚きと発見の実験ショータイム",
    HOL_D : "理系が踊れちゃってごめん",
    S21_L : "古本市、ビブリオバトル",
    S55 : "楽しいメイドカジノ~博学投資~",
    CMC_3 : "不思議の国のベビーカステラ",
    S36 : "n回目のおつかい around the world",
}

# location:(0,列情報(並ぶ企画) 1,混雑情報(出入り自由)),一言
init_comment = "全力で開催します！ぜひ来てください！"

status_map = {
    S45 : [1,"健全？でクリーン？なカジノをやってます!"],
    JK1 : [1,"景品のピコピコハンマーのチャンスあります"],
    E3P : [1,"募金にご協力をお願いします!"],
    S46 : [0,"ボードゲームは楽しいZOY!"],
    S3W : [1,"ロボ探です。お昼時間以外はやってます!"],
    CMC : [0,"美味なパフェをあなたに"],
    JAK : [1,"午前は見学、午後は整理券必須の体験企画!"],
    BOL : [0,"全てにおいて会心の出来です！待ってます！"],
    C31 : [1,"全てにおいて会心の出来です！待ってます！"],
    SHR : [1,init_comment],
    HOL_D : [1,init_comment],
    S21_L : [1,"疲れたときにぜひお立ち寄りください"],
    S55 : [0,"共感性羞恥の塊！ぜひ楽しんでください"],
    CMC_3 : [0,"世界一美味しいベビーカステラ、ご賞味あれ"],
    S36 : [0,"13時〜15時の限定開催！お楽しみに！！"],
}


class CrowdData(models.Model):

    #####選択肢の定義
    LOCATION_CHOICE = dict(lp_map)
    #####

    location = models.CharField("場所",max_length=25,choices=LOCATION_CHOICE)
    crowd_level = models.IntegerField("混雑状況もしくは並び時間",validators=[MinValueValidator(0), MaxValueValidator(10)])
    pub_date = models.DateTimeField("pub_date",default=timezone.now)

    # localtimeにしてAsia/Tokyoに合わせる modelは時間をUTCで保存するらしい
    def __str__(self):
        return f'{self.location} - {self.crowd_level} at {timezone.localtime(self.pub_date)}'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(hours=1)

