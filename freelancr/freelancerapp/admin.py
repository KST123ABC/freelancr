from django.contrib import admin
from .models import *
# Register your models here.


class ProfileInfoAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "is_admin", "date_joined"]
	class Meta:
		model = ProfileInfo
class SkillAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Skill

admin.site.register(ProfileInfo, ProfileInfoAdmin)
admin.site.register(Skill, SkillAdmin)