# Generated by Django 2.2.14 on 2020-08-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0254_course_collaborator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborator',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='corporateendorsement',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='courseruntype',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='coursetype',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='curriculum',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='curriculumcoursemembership',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='curriculumcourserunexclusion',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='curriculumprogrammembership',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='endorsement',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='mode',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='pathway',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='ranking',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='seattype',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterField(
            model_name='leveltypetranslation',
            name='name_t',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
