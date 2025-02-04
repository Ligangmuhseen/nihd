# Generated by Django 4.2.9 on 2024-02-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('story', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Abouttwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='about_images/')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='back_images/')),
            ],
        ),
        migrations.CreateModel(
            name='FaqsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Healthvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hero_images/')),
                ('mainheading', models.CharField(max_length=255)),
                ('subheading', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Heroslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hero_sliderimages/')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacies', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('diseases', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='service_images/')),
                ('service', models.TextField()),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.CreateModel(
            name='SocietyFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Me', 'Me'), ('ke', 'Ke')], max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('ward', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('health_status_description', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('has_disease', models.BooleanField()),
                ('disease_name', models.CharField(blank=True, max_length=255, null=True)),
                ('medication_used', models.CharField(blank=True, max_length=255, null=True)),
                ('treatment_facility', models.CharField(blank=True, choices=[('Kliniki ya tiba mbadala', 'Kliniki ya tiba mbadala'), ('Zahanati', 'Zahanati'), ('Kituo cha Afya', 'Kituo cha Afya'), ('Hospitali', 'Hospitali'), ('Duka la dawa', 'Duka la dawa')], max_length=255, null=True)),
                ('has_allergy', models.BooleanField()),
                ('allergy_description', models.TextField(blank=True, null=True)),
                ('family_health_conditions', models.TextField(blank=True, null=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Strategicone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='strategic_images/')),
                ('heading', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Strategictwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='strategic_images/')),
                ('heading', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('words', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('has_badge', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Whyusone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('readmore', models.TextField(default='yes')),
            ],
        ),
        migrations.CreateModel(
            name='Whyustwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='whyus_images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
