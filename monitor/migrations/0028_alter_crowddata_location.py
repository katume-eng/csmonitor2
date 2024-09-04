# Generated by Django 5.1 on 2024-09-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0027_alter_crowddata_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowddata',
            name='location',
            field=models.CharField(choices=[('S45', '根城はサイコロを振らない'), ('情報教室1', '情報工学部 ゲーム展'), ('1F生徒昇降口付近,3FS34前PCラウンジ', '緑の羽根募金'), ('S46', 'ふっ、おもしれーゲーム'), ('S37,S38', 'ロボパーティーForBetting'), ('コミュニケーションコート', '不思議の国のベビーカステラ'), ('柔剣道場', 'トレトレかるた'), ('生物実験室', 'いっつぁまいくろわーるど_生物実験室'), ('C31', 'いっつぁまいくろわーるど_C31'), ('視聴覚室', '驚きと発見の実験ショータイム'), ('ホール', '理系が踊れちゃってごめん'), ('S21,図書室', '古本市、ビブリオバトル'), ('S55', '楽しいメイドカジノ~博学投資~')], max_length=25, verbose_name='場所'),
        ),
    ]
