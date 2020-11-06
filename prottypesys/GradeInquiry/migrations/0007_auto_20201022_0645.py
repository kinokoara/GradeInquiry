# Generated by Django 3.1.2 on 2020-10-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeInquiry', '0006_course_depart_enrolled_grade_student_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='depart_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='depart',
            name='depart_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enrolled',
            name='enrolled_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='units',
            field=models.CharField(max_length=2),
        ),
    ]
