from django.contrib import admin
from .Userdatamodel import Userdatamodel


@admin.register(Userdatamodel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # Display these fields in the list view
    search_fields = ('username', 'id')  # Enable search by username and email

# Register the model with the customized admin class
