from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=200)),
                ('course_no', models.CharField(max_length=200)),
                ('section_no', models.CharField(max_length=200)),
                ('meeting_times', models.CharField(max_length=200)),
                ('is_lab', models.BooleanField())
            ]
        )
    ]
