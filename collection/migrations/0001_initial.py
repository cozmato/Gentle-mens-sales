# Generated by Django 4.2.4 on 2024-01-20 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(default='provision', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmailMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_1', models.FileField(blank=True, null=True, upload_to='product_pic')),
                ('file_2', models.FileField(blank=True, null=True, upload_to='product_pic')),
                ('file_3', models.FileField(blank=True, null=True, upload_to='product_pic')),
                ('file_4', models.FileField(blank=True, null=True, upload_to='product_pic')),
                ('file_5', models.FileField(blank=True, null=True, upload_to='product_pic')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, max_length=14, null=True)),
                ('discount', models.FloatField(blank=True, max_length=14, null=True)),
                ('currency', models.CharField(blank=True, choices=[('$', '$'), ('₦', '₦'), ('£', '£'), ('€', '€')], default=None, max_length=11, null=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Published', max_length=11)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='provision', on_delete=django.db.models.deletion.PROTECT, related_name='category', to='collection.category')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['image', 'name'], name='collection__image_29c849_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'price', 'discount', 'currency', 'category', 'status', 'description'], name='collection__name_e4312a_idx'),
        ),
    ]
