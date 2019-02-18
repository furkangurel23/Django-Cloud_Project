from django.contrib import admin
from django.contrib.auth.models import User
from .models import (tbl_user,
					 tbl_file,
					 tbl_image,
					 tbl_music,
					 tbl_video,
					 tbl_folder,
					 tbl_folder_file,
					 tbl_address,
					 tbl_groups,
					 tbl_groups_user,
					 tbl_social_media,
					 tbl_contact,
					 tbl_share_with_user,
					 tbl_external_user,
					 tbl_share_external,)

class GroupUserInline(admin.TabularInline):
	model = tbl_groups_user
class SocialMediaInline(admin.TabularInline):
	model = tbl_social_media
class ContactInline(admin.TabularInline):
	model = tbl_contact
class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'location', 'birth_date', 'language')
	inlines = [GroupUserInline,SocialMediaInline,ContactInline]

admin.site.register(tbl_user,UserAdmin)
@admin.register(tbl_file)
class tbl_file_admin(admin.ModelAdmin):
	list_display = ('owner_id', 'title', 'date')
admin.site.register(tbl_image)
#admin.site.register(tbl_folder_in_folder)
admin.site.register(tbl_music)
admin.site.register(tbl_video)
admin.site.register(tbl_folder)
admin.site.register(tbl_folder_file)
@admin.register(tbl_address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ('owner_id', 'adType', 'extAddress', 'post_code', 'city', 'country')
admin.site.register(tbl_groups)
admin.site.register(tbl_groups_user)
admin.site.register(tbl_social_media)
@admin.register(tbl_contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('owner_id', 'full_name', 'e_mail')

admin.site.register(tbl_share_with_user)
admin.site.register(tbl_share_external)
admin.site.register(tbl_external_user)

# Register your models here.
