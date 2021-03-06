# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-11 17:35

from django.db import migrations
from wagtail.core import blocks as core_blocks
from wagtail.core import fields as core_fields


class Migration(migrations.Migration):

    dependencies = [
        ('mega_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='submenus',
            field=core_fields.StreamField((('submenu', core_blocks.StructBlock((('title', core_blocks.CharBlock()), ('overview_page', core_blocks.PageChooserBlock(required=False)), ('featured_links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)))), default=[])), ('other_links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)), ('icon', core_blocks.CharBlock()))), default=[])), ('columns', core_blocks.ListBlock(core_blocks.StructBlock((('heading', core_blocks.CharBlock(required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)))), default=[])))), default=[]))))),)),
        ),
    ]
