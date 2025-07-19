from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters

from brdc.filters import DownloadsFilter
from brdc.models import (
    AboutCampus,
    Download,
    CampusChiefMessage,
    Album,
    Blog,
    Carousel,
    ContactUs,
    Courses,
    Facility,
    Milestone,
    OnlineAdmission,
    PopUp,
    CampusBatch,
    Suggestion,
    Team,
    Testimonial,
    VideoGallery,
)
from brdc.serializers import (
    AboutCampusSerializer,
    CampusChiefMessageSerializer,
    DownloadSerializer,
    AlbumSerializer,
    BlogSerializer,
    CarouselSerilaizer,
    ContactUsSerializer,
    CourseSerializer,
    FacilitiesSerializer,
    MilestonesSerializer,
    OnlineAdmissionSerializer,
    PopUpSerializer,
    CampusBatchSerializer,
    SuggestionSerializer,
    TeamSerializer,
    TestimonialSerializer,
    VideoGallerySerializer,
)
from brdc_backend.permissions import CustomPermission

# Create your views here.


class CarouselViewSet(ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerilaizer


class FacilityViewSet(ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitiesSerializer


class MilestonesViewSet(ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestonesSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    # permission_classes = [CustomPermission]


class PopUpViewSet(ModelViewSet):
    queryset = PopUp.objects.all()
    serializer_class = PopUpSerializer


class CampusChiefMessageViewSet(ModelViewSet):
    queryset = CampusChiefMessage.objects.all()
    serializer_class = CampusChiefMessageSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class TestimonialViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class SuggestionViewSet(ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class OnlineAdmissionViewSet(ModelViewSet):
    queryset = OnlineAdmission.objects.all()
    serializer_class = OnlineAdmissionSerializer
    # permission_classes = [CustomPermission]


class CampusBatchViewSet(ModelViewSet):
    queryset = CampusBatch.objects.prefetch_related("students").all()
    serializer_class = CampusBatchSerializer


class AboutCampusViewSet(ModelViewSet):
    queryset = AboutCampus.objects.all()
    serializer_class = AboutCampusSerializer


class DownloadViewSet(ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_class = DownloadsFilter

    search_fields = [
        "is_curriculum",
        "is_report",
        "is_form",
        "is_notice",
        "is_result",
        "created_at",
    ]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]  # default ordering: newest first


class VideoGallerySet(ModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
