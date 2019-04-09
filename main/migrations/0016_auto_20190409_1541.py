# Generated by Django 2.1.7 on 2019-04-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190409_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Restaurant_Order',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='Orders_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterOrderWithRespectTo(
            name='order',
            order_with_respect_to='Restaurant_Order',
        ),
    ]
