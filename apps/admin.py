from django.contrib import admin
from apps.models import Product, Post
from django import forms


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_title(self):
        if self.cleaned_data["title"] == "Zombie":
            raise forms.ValidationError("No Vampires")

        return self.cleaned_data["title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "time", "description")
    search_fields = ("title__startswith",)
    list_filter = ("title", "time", "description",)
    form = PostAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "title")
    search_fields = ("name__startswith",)
    list_filter = ("name", "price", "title",)
