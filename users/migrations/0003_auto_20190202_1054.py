# Generated by Django 2.1.2 on 2019-02-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190202_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_pics/picc.jpg', upload_to='profile_pics'),
        ),
    ]