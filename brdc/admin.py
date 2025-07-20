from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.admin import SummernoteInlineModelAdmin  # ✅

from brdc.models import (
    AboutCategory,
    AboutSection,
    Album,
    AlbumImage,
    Blog,
    Carousel,
    CarouselItem,
    Carrier,
    ContactUs,
    Milestone,
    Network,
    PopUp,
    ResourceAndMediaCategory,
    ResourceAndMediaSection,
    Team,
    VideoGallery,
)


class CarouselItemAdminInline(admin.StackedInline):
    model = CarouselItem
    extra = 1


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ["id"]
    inlines = [CarouselItemAdminInline]


class AlbumImageAdmin(admin.TabularInline):
    model = AlbumImage
    # min_num = 1
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    inlines = [AlbumImageAdmin]


@admin.register(Milestone)
class MilestonesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "count"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "phone_no", "description"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(PopUp)
class PopUpAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "position",
        "description",
        "image",
        "is_bod_team",
        "is_administrative",
    ]


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]


@admin.register(Carrier)
class CarrierAdmin(SummernoteModelAdmin):
    list_display = ["id", "name", "description", "upload_document"]


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ["id", "title", "author", "thumbnail", "created_at", "updated_at"]


class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter Your Title"}),
        }


class AboutCategoryInline(SummernoteInlineModelAdmin, admin.StackedInline):
    model = AboutCategory
    summernote_fields = ("description",)
    extra = 1
    fields = ("id", "description")


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    form = AboutSectionForm  # use custom form here
    list_display = (
        "id",
        "name",
        "image",
        "is_who_we_are",
        "is_what_we_do",
    )
    inlines = [AboutCategoryInline]


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "video_link"]


class ResourceAndMediaSectionForm(forms.ModelForm):
    class Meta:
        model = ResourceAndMediaSection
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter Your Title"}),
        }


class ResourceAndMediaCategoryInline(SummernoteInlineModelAdmin, admin.StackedInline):
    model = ResourceAndMediaCategory
    summernote_fields = ("description",)

    extra = 1
    fields = (
        "id",
        "name",
        "description",
        "upload_document",
    )


@admin.register(ResourceAndMediaSection)
class ResourceAndMediaSectionAdmin(admin.ModelAdmin):
    form = ResourceAndMediaSectionForm  # use custom form here
    list_display = (
        "id",
        "name",
    )
    inlines = [ResourceAndMediaCategoryInline]
