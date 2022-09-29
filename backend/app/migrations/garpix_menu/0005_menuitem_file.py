# Generated by Django 3.2 on 2022-09-29 12:20

from django.db import migrations, models
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_menu', '0004_auto_20220713_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Файл'),
        ),
    ]