import logging

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, PositiveIntegerField, BooleanField
from django.conf import settings
from django.urls import reverse

from django_sso_app.core.apps.users.models import DjangoSsoAppUserModelMixin

from django_uploads_app.ftp.utils import create_random_password

logger = logging.getLogger('tests')


class User(AbstractUser, DjangoSsoAppUserModelMixin):
    ftp_enabled = BooleanField(default=True)
    ftp_password = CharField(max_length=100, default=create_random_password)
    ftp_quota = PositiveIntegerField(default=settings.DJANGO_UPLOADS_FTP_QUOTA_MB)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        setattr(self, '__old_ftp_password', getattr(self, 'ftp_password', None))
        setattr(self, '__old_ftp_quota', getattr(self, 'ftp_quota', None))

    @property
    def ftp_password_has_changed(self):
        old_ftp_password = getattr(self, '__old_ftp_password')
        return old_ftp_password != self.ftp_password

    @property
    def ftp_quota_has_changed(self):
        old_ftp_quota = getattr(self, '__old_ftp_quota')
        return old_ftp_quota != self.ftp_quota

    #def get_relative_url(self):
    #    return reverse("users:detail", kwargs={"username": self.username})

    def create_filer_folders(self):
        from filer.models.foldermodels import Folder
        from django_uploads_app.models import UploadType

        users_folder, _created = Folder.objects.get_or_create(name='users')
        user_folder, _created = Folder.objects.get_or_create(name=self.sso_id, parent=users_folder, owner=self)

        for ut in UploadType.objects.all():
            _ut_folder, _created = Folder.objects.get_or_create(name=ut.slug, parent=user_folder, owner=self)
