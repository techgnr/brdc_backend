from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters
from rest_framework.viewsets import ModelViewSet

from brdc.filters import AboutSectionFilter
from brdc.models import (
    AboutSection,
    Album,
    Blog,
    Carousel,
    Carrier,
    ContactUs,
    Events,
    Milestone,
    Network,
    NewsAndNotice,
    PopUp,
    PublicationAndDocuments,
    SucessStories,
    Team,
    VideoGallery,
)
from brdc.serializers import (
    AboutSectionSerializer,
    AlbumSerializer,
    BlogSerializer,
    CarouselSerilaizer,
    CarrierSerializer,
    ContactUsSerializer,
    EventsSerializer,
    MilestonesSerializer,
    NetworkSerializer,
    NewsAndNoticeSerializer,
    PopUpSerializer,
    PublicationAndDocumentsSerializer,
    SucessStoriesSerializer,
    TeamSerializer,
    VideoGallerySerializer,
)

# Create your views here.


class CarouselViewSet(ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerilaizer


class MilestonesViewSet(ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestonesSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class VideoGallerySet(ModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    # permission_classes = [CustomPermission]


class PopUpViewSet(ModelViewSet):
    queryset = PopUp.objects.all()
    serializer_class = PopUpSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class CarrierViewSet(ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


class AboutSectionViewSet(ModelViewSet):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_class = AboutSectionFilter

    search_fields = [
        "is_who_we_are",
        "is_what_we_do",
        # "created_at",
    ]
    # ordering_fields = ["created_at"]
    # ordering = ["-created_at"]  # default ordering: newest first


class NewsAndNoticeViewSet(ModelViewSet):
    queryset = NewsAndNotice.objects.all()
    serializer_class = NewsAndNoticeSerializer


class EventsViewSet(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class SucessStoriesViewSet(ModelViewSet):
    queryset = SucessStories.objects.all()
    serializer_class = SucessStoriesSerializer


class PublicationAndDocumentsViewSet(ModelViewSet):
    queryset = PublicationAndDocuments.objects.all()
    serializer_class = PublicationAndDocumentsSerializer
