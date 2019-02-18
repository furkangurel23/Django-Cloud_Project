from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class tbl_user(models.Model):
    #on = models.ForeignKey('tbl_folder', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    language = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('user-detail', args=[str(self.user.pk)])

    """def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300  or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save()"""


class tbl_groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    isAdmin = models.BooleanField(default=False)
    group_name = models.CharField(max_length=50, blank=False)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('group-detail', args=[str(self.group_id)])

    def __str__(self):
        return self.group_name
class tbl_groups_user(models.Model):
    group_id = models.ForeignKey(tbl_groups, on_delete=models.CASCADE, blank=False)
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, blank=False)
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('group-detail', args=[str(self.group_id)])

class tbl_file(models.Model):
    file_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    size = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    isFav = models.BooleanField(default=False)

    """def get_absolute_url(self):
        return reverse('file-detail', args=[str(self.file_id)])"""
    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk':self.file_id})

    def __str__(self):
        return self.title

class tbl_image(tbl_file):
    resolution = models.IntegerField()
    def __str__(self):
        return self.title
        
class tbl_music(tbl_file):
    time = models.IntegerField()
    artist = models.CharField(max_length=50)
    mType = models.CharField(max_length=50)
    album = models.CharField(max_length=50)

    
    def __str__(self):
        return self.title

class tbl_video(tbl_file):
    vType = models.CharField(max_length=50)
    resolution = models.IntegerField()
    time = models.IntegerField()

    
    def __str__(self):
        return self.title

class tbl_folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, verbose_name='Owner')
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='tbl_folder')
    size = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    describtion = models.CharField(max_length=200)
    isFav = models.BooleanField(default=False)

    def get_all_children(self,include_self=True):
        r=[]
        if include_self:
            r.append(self)
        for c in tbl_folder.objects.filter(parent_folder=self):
            _r = c.get_all_children(include_self=True)
            if 0<len(_r):
                r.extend(_r)
        return r
    def __str__(self):
        return self.title
    #def get_absolute_url(self):
     #   return reverse('folder-detail', args=[str(self.folder_id)])
    
    def get_absolute_url(self):
        return reverse('folder-detail', kwargs={'pk':self.pk})




class tbl_folder_file(models.Model):
    folder_id = models.ForeignKey(tbl_folder, on_delete=models.CASCADE, blank=True)
    file_id = models.ForeignKey(tbl_file, on_delete=models.CASCADE, blank=True)
    def get_absolute_url(self):
        return reverse('folder-detail', kwargs={'pk':self.pk})

class tbl_address(models.Model):
	owner_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
	adType = models.CharField(max_length=50)
	extAddress = models.CharField(max_length=500)
	post_code = models.IntegerField()
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.adType

class tbl_social_media(models.Model):
    owner_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, blank=False, verbose_name='Owner')
    media_type = models.CharField(max_length=50)
    def __str__(self):
        return self.media_type

class tbl_contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, blank=False, verbose_name='Contact User:')
    full_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12, blank=True, help_text='Please fill with a maximum 12-digit phone number')
    location = models.CharField(max_length=30, blank=True)
    from_next_cloud_or_another = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('contract-detail', args=[str(self.contact_id)])

class tbl_share_with_user(models.Model):
    share_id = models.AutoField(primary_key=True)
    file_id = models.ForeignKey(tbl_file, on_delete=models.CASCADE, blank=False, verbose_name='File Name')
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, blank=False, verbose_name='User Name', related_name='+')#, related_name='+'
    user_id2 = models.ForeignKey(tbl_user, on_delete=models.CASCADE, blank=False, verbose_name='Shared User')
    expire_on = models.DateField(default=timezone.now)
    readable_writable = models.BooleanField(default=False)
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('share-detail', args=[str(self.share_id)])

class tbl_external_user(models.Model):
    uuid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50)
    def __str__(self):
        return self.user_name

class tbl_share_external(models.Model):
    share_id = models.AutoField(primary_key=True)
    file_id = models.ForeignKey(tbl_file, on_delete=models.CASCADE, blank=False, verbose_name='File Name')
    user_id = models.ForeignKey(tbl_external_user, on_delete=models.CASCADE, blank=False, verbose_name='User Name')
    expire_on = models.DateField(default=timezone.now)
