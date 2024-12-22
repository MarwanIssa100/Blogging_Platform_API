# Generated by Django 5.1.4 on 2024-12-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_tag_blog_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='blog',
            field=models.ManyToManyField(related_name='tags', to='blog.blog'),
        ),
    ]