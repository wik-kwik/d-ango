from django.contrib import admin
from .models import Form
from .models import Post

# Register your models here.

class FormAdmin(admin.ModelAdmin):

    list_display = ("name", "street", "postal_code", "city", "phone_number", "email", "animal", "amount", "period", "since", "rodo_agreement", "data_agreement")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "text", "imgOne", "imgTwo", "created_on")


admin.site.register(Form, FormAdmin)
admin.site.register(Post, PostAdmin)
