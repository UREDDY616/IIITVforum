# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseNo', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('courseName', models.CharField(default='', max_length=100)),
                ('credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('facultyName', models.CharField(default='', max_length=100)),
                ('facultyEmail', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadYear', models.CharField(default='', max_length=10)),
                ('semesterNo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('studentId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('studentName', models.CharField(default='', max_length=100)),
                ('progId', models.CharField(default='', max_length=100)),
                ('batch', models.CharField(default='', max_length=10)),
                ('studentEmail', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together=set([('acadYear', 'semesterNo')]),
        ),
        migrations.AddField(
            model_name='registers',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='student.Semester'),
        ),
        migrations.AddField(
            model_name='registers',
            name='courseNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Courses'),
        ),
        migrations.AddField(
            model_name='registers',
            name='facultyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Faculty'),
        ),
        migrations.AddField(
            model_name='registers',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='student.Semester'),
        ),
        migrations.AddField(
            model_name='registers',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Students'),
        ),
        migrations.AddField(
            model_name='offers',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='student.Semester'),
        ),
        migrations.AddField(
            model_name='offers',
            name='courseNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Courses'),
        ),
        migrations.AddField(
            model_name='offers',
            name='facultyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Faculty'),
        ),
        migrations.AddField(
            model_name='offers',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='student.Semester'),
        ),
        migrations.AlterUniqueTogether(
            name='registers',
            unique_together=set([('studentId', 'facultyId', 'courseNo', 'acadYear', 'semesterNo')]),
        ),
        migrations.AlterUniqueTogether(
            name='offers',
            unique_together=set([('facultyId', 'courseNo', 'acadYear', 'semesterNo')]),
        ),
    ]
