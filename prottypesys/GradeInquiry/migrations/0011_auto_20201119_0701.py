# Generated by Django 3.1.3 on 2020-11-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeInquiry', '0010_loginuser_admin_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='evaluation',
            field=models.CharField(blank=True, choices=[('1', '秀'), ('2', '優'), ('3', '可'), ('4', '不可')], max_length=2, verbose_name='評価'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade_id',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, verbose_name='成績ID'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student_number',
            field=models.CharField(blank=True, max_length=5, verbose_name='学籍番号'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='subject_id',
            field=models.CharField(blank=True, max_length=7, verbose_name='科目番号'),
        ),
    ]