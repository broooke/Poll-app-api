# Generated by Django 3.1.6 on 2021-02-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollAPI', '0002_poll_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='pollAPI.choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='pollAPI.poll'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='pollAPI.question'),
        ),
    ]