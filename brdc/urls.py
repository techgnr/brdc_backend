from django.contrib import admin
from rest_framework_nested import routers

admin.site.site_title = "TSCS"
admin.site.site_header = "TSCS Admin"
admin.site.index_title = "DASHBOARD-TSCS"

from . import views

router = routers.DefaultRouter()

router.register("carousels", views.CarouselViewSet)

router.register("albums", views.AlbumViewSet)
router.register("contactus", views.ContactUsViewSet)
router.register("popup", views.PopUpViewSet)
router.register("milestones", views.MilestonesViewSet)
router.register("blogs", views.BlogViewSet)
router.register("teams", views.TeamViewSet)
router.register("videolink", views.VideoGallerySet)
router.register("aboutsection", views.AboutSectionViewSet)
router.register("carrier", views.CarrierViewSet)
router.register("network", views.NetworkViewSet)
router.register("newsandnotice", views.NewsAndNoticeViewSet)
router.register("sucessstories", views.SucessStoriesViewSet)
router.register("publicationanddocuments", views.PublicationAndDocumentsViewSet)
router.register("events", views.EventsViewSet)

urlpatterns = router.urls
