from rest_framework import serializers

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


class MilestonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ["id", "name", "count", "is_reached", "is_statistics"]


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ["id", "image"]


class AlbumSerializer(serializers.ModelSerializer):
    images = AlbumImageSerializer(many=True)

    class Meta:
        model = Album
        fields = ["id", "title", "description", "thumbnail", "images"]


# for youtube video links
class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = [
            "id",
            "title",
            "video_link",
        ]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["id", "full_name", "email", "phone_no", "description"]


class PopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = ["id", "name", "image"]


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
            "description",
            "image",
            "is_bod_team",
            "is_administrative",
        ]


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ["id", "name", "image"]


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ["id", "name", "description", "upload_document"]


class AboutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCategory
        fields = ["id", "description"]


class AboutSectionSerializer(serializers.ModelSerializer):
    categories = AboutCategorySerializer(many=False)


    class Meta:
        model = AboutSection
        fields = [
            "id",
            "name",
            "image",
            "is_who_we_are",
            "is_what_we_do",
            "categories",
        ]


class ResourceAndMediaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceAndMediaCategory
        fields = ["id", "name", "description", "upload_document", "created_at"]


class ResourceAndMediaSectionSerializer(serializers.ModelSerializer):
    categories = ResourceAndMediaCategorySerializer(many=True)

    class Meta:
        model = ResourceAndMediaSection
        fields = [
            "id",
            "name",
        ]
