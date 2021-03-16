# Generated by Django 1.11.28 on 2020-02-27 16:38


from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0236_add_program_type_uuid_and_coaching'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoliaProxyCourse',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('course_metadata.course',),
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AlgoliaProxyProgram',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('course_metadata.program',),
        ),
    ]
