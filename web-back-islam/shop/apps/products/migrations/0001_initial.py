# Generated by Django 3.0.6 on 2020-05-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='product name')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_img')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categories', models.ManyToManyField(related_name='products', to='categories.Category')),
            ],
        ),
    ]
