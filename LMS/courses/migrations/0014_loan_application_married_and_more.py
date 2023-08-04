# Generated by Django 4.2.2 on 2023-07-31 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_loan_application_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_application',
            name='Married',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Credit_History',
            field=models.FloatField(choices=[(0, 0), (1, 1)]),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Dependents',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Education',
            field=models.CharField(choices=[('0', 'Graduate'), ('1', 'Not Graduate')], max_length=20),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Gender',
            field=models.CharField(choices=[('1', 'MALE'), ('0', 'FEMALE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Property_Area',
            field=models.CharField(choices=[('0', 'Rural \t'), ('1', 'Semiurban'), ('2', 'Urban')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Self_Employed',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'NO')], max_length=26),
        ),
    ]
