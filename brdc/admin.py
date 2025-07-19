from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from brdc.models import (
    AboutCampus,
    Album,
    AlbumImage,
    Blog,
    CampusBatch,
    CampusChiefMessage,
    Carousel,
    CarouselItem,
    ContactUs,
    Courses,
    Download,
    DownloadCategory,
    Facility,
    Milestone,
    OnlineAdmission,
    PopUp,
    Student,
    Suggestion,
    Team,
    Testimonial,
    VideoGallery,
)


class CarouselItemAdminInline(admin.StackedInline):
    model = CarouselItem
    extra = 1


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ["id"]
    inlines = [CarouselItemAdminInline]


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


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


@admin.register(CampusChiefMessage)
class CampusChiefMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "heading", "title", "description", "author", "image"]


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image", "description"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image", "description", "position"]


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone_no", "description"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "position",
        "service",
        "image",
        "is_management",
        "is_administrative",
        "is_staff",
        "is_advisor",
    ]


@admin.register(OnlineAdmission)
class OnlineAdmissionAdmin(admin.ModelAdmin):
    list_display = ["id", "link", "title"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ["id", "title", "author", "thumbnail", "created_at", "updated_at"]


class StudentsAdmin(admin.StackedInline):
    model = Student
    min_num = 1
    extra = 1


@admin.register(CampusBatch)
class CampusBatchAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [StudentsAdmin]


@admin.register(AboutCampus)
class AboutCampusAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
    list_display = ["id", "title", "description", "image"]


class DownloadForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter Your Title"}),
        }


class DownloadCategoryInline(admin.TabularInline):
    model = DownloadCategory
    extra = 1
    fields = ("title", "attachment", "created_at")


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    form = DownloadForm  # use custom form here
    list_display = (
        "name",
        "is_curriculum",
        "is_report",
        "is_form",
        "is_notice",
        "is_result",
        "created_at",
    )
    inlines = [DownloadCategoryInline]


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "video_link"]
