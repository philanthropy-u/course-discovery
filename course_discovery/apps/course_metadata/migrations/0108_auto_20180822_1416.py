# Generated by Django 1.11.11 on 2018-08-22 14:16


from django.db import migrations


def seed_pathway(apps, schema_editor):
    CreditPathway = apps.get_model('course_metadata', 'CreditPathway')
    Pathway = apps.get_model('course_metadata', 'Pathway')
    for cp in CreditPathway.objects.all():
        pathway, _ = Pathway.objects.update_or_create(
            uuid=cp.uuid,
            partner=cp.partner,
            name=cp.name,
            org_name=cp.org_name,
            email=cp.email,
            description=cp.description,
            destination_url=cp.destination_url,
        )
        pathway.programs = cp.programs.all()
        pathway.save()

class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0107_auto_20180821_1340'),
    ]

    operations = [
        migrations.RunPython(seed_pathway, migrations.RunPython.noop),
    ]
