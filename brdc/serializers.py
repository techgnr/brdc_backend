from rest_framework import serializers

from brdc.models import (
    AboutCampus,
    Album,
    AlbumImage,
    Blog,
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
    CampusChiefMessage,
    CampusBatch,
    Student,
    Suggestion,
    Team,
    Testimonial,
    VideoGallery,
)


class CarouselItemSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = [
            "id",
            "heading",
            "title",
            "description",
            "image",
            "primary_button_label",
            "primary_button_link",
            "secondary_button_label",
            "secondary_button_link",
        ]


class CarouselSerilaizer(serializers.ModelSerializer):
    items = CarouselItemSerilaizer(many=True)

    class Meta:
        model = Carousel
        fields = ["id", "items"]


class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name", "image", "description"]


class MilestonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ["id", "name", "count"]


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ["id", "image"]


class AlbumSerializer(serializers.ModelSerializer):
    images = AlbumImageSerializer(many=True)

    class Meta:
        model = Album
        fields = ["id", "title", "description", "thumbnail", "images"]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["id", "full_name", "email", "phone_no", "description"]


class PopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = ["id", "name", "image"]


class CampusChiefMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusChiefMessage
        fields = ["id", "heading", "title", "description", "author", "image"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id", "name", "image", "description"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "image", "description", "position"]


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ["id", "name", "email", "phone_no", "description"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "thumbnail",
            "author",
            "created_at",
            "updated_at",
        ]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
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


class OnlineAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineAdmission
        fields = ["id", "link", "title"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "percentage", "image"]


class CampusBatchSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = CampusBatch
        fields = ["id", "name", "students"]


class AboutCampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCampus
        fields = ["id", "title", "description", "image"]


class DownloadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadCategory
        fields = ["id", "title", "attachment", "created_at"]


class DownloadSerializer(serializers.ModelSerializer):
    categories = DownloadCategorySerializer(many=True)

    class Meta:
        model = Download
        fields = [
            "id",
            "name",
            "is_curriculum",
            "is_report",
            "is_form",
            "is_notice",
            "created_at",
            "is_result",
            "categories",
        ]


# for youtube video links
class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = [
            "id",
            "title",
            "video_link",
        ]
