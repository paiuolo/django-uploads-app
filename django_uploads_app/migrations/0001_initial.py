# Generated by Django 2.2.24 on 2021-10-11 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_uploads_app.managers
import django_uploads_app.models
import django_uploads_app.storage
import django_uploads_app.utils
import filer.fields.file
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0012_file_mime_type'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=36, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('secret', models.CharField(db_index=True, default=django_uploads_app.utils.create_secret, max_length=2048, unique=True, verbose_name='Secret')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('downloaded_at', models.DateTimeField(blank=True, null=True, verbose_name='Last download')),
                ('times_downloadable', models.PositiveIntegerField(blank=True, null=True, verbose_name='Times downloadable')),
                ('times_downloaded', models.PositiveIntegerField(default=0, verbose_name='Times downloaded')),
                ('active_forever', models.BooleanField(default=True, verbose_name='Active forever')),
                ('active_until', models.DateTimeField(blank=True, null=True, verbose_name='Active until')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django_uploads_app.managers.LinkManager()),
            ],
        ),
        migrations.CreateModel(
            name='UploadType',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('is_public', models.BooleanField(default=False, verbose_name='is public')),
                ('meta', models.TextField(blank=True, null=True, verbose_name='Meta')),
                ('validation_module', models.CharField(blank=True, max_length=255, null=True, verbose_name='Validation module')),
                ('file_mime', models.CharField(blank=True, max_length=255, null=True, verbose_name='File mime')),
                ('upload_success_message', models.TextField(blank=True, null=True, verbose_name='Upload success message')),
                ('upload_success_redirect_url', models.TextField(blank=True, null=True, verbose_name='Upload success redirect URL')),
                ('upload_success_rpc_url', models.TextField(blank=True, null=True, verbose_name='Upload success RPC URL')),
                ('times_downloadable', models.PositiveIntegerField(blank=True, null=True, verbose_name='Times downloadable')),
                ('active_forever', models.BooleanField(default=True, verbose_name='Active forever')),
                ('active_until', models.DateTimeField(blank=True, null=True, verbose_name='Active until')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Groups')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django_uploads_app.managers.SlugPKManager()),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=36, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('meta', models.TextField(blank=True, null=True, verbose_name='Meta')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('file_name', models.CharField(max_length=512, verbose_name='File name')),
                ('file_base64', models.TextField(blank=True, null=True, verbose_name='File base64')),
                ('file_url', models.CharField(blank=True, max_length=2048, null=True, verbose_name='File url')),
                ('file_path', models.CharField(blank=True, db_index=True, max_length=2048, null=True, verbose_name='File path')),
                ('file_md5', models.CharField(blank=True, max_length=32, null=True, verbose_name='File md5')),
                ('file_sha1', models.CharField(blank=True, max_length=40, null=True, verbose_name='File sha1')),
                ('file_mime', models.CharField(blank=True, max_length=255, null=True, verbose_name='File mime')),
                ('file_size', models.PositiveIntegerField(default=0, verbose_name='File size')),
                ('validated_at', models.DateTimeField(blank=True, null=True, verbose_name='Validated at')),
                ('successfully_validated', models.NullBooleanField(verbose_name='Successfully validated')),
                ('parsed_at', models.DateTimeField(blank=True, null=True, verbose_name='Parsed at')),
                ('successfully_parsed', models.NullBooleanField(verbose_name='Successfully parsed')),
                ('revision', models.CharField(blank=True, max_length=255, null=True, verbose_name='Revision')),
                ('upload_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_uploads_app.UploadType', verbose_name='upload type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django_uploads_app.managers.UploadManager()),
            ],
        ),
        migrations.CreateModel(
            name='LinkShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=36, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('permissions', models.CharField(blank=True, max_length=10, null=True, verbose_name='permissions')),
                ('resource_type', models.CharField(blank=True, choices=[('user', 'User'), ('group', 'Group')], max_length=255, null=True, verbose_name='Resource type')),
                ('resource_uuid', models.CharField(blank=True, max_length=255, null=True, verbose_name='Resource UUID')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to='django_uploads_app.Link', verbose_name='Link')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django_uploads_app.managers.UuidPKManager()),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='django_uploads_app.Upload', verbose_name='Upload'),
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=36, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('upload_url', models.CharField(max_length=255, verbose_name='Upload url')),
                ('file_url', models.CharField(blank=True, max_length=2048, null=True, verbose_name='File url')),
                ('uploaded_at', models.DateTimeField(blank=True, null=True, verbose_name='date uploaded')),
                ('file_data', models.FileField(blank=True, null=True, storage=django_uploads_app.storage.PrivateFileSystemStorage(), max_length=255, upload_to=django_uploads_app.models.get_uploaded_file_path)),
                ('filer_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File')),
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='file_upload', to='django_uploads_app.Upload', verbose_name='Upload')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django_uploads_app.managers.FileUploadManager()),
            ],
        ),
    ]
