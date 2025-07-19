from rest_framework_nested import routers
from django.contrib import admin

admin.site.site_title = "TSCS"
admin.site.site_header = "TSCS Admin"
admin.site.index_title = "DASHBOARD-TSCS"

from . import views


router = routers.DefaultRouter()

router.register("carousels", views.CarouselViewSet)
router.register("facilities", views.FacilityViewSet)
router.register("testimonials", views.TestimonialViewSet)
router.register("albums", views.AlbumViewSet)
router.register("contactus", views.ContactUsViewSet)
router.register("popup", views.PopUpViewSet)
router.register("campuschiefmessage", views.CampusChiefMessageViewSet)
router.register("courses", views.CoursesViewSet)
router.register("milestones", views.MilestonesViewSet)
router.register("suggestions", views.SuggestionViewSet)
router.register("blogs", views.BlogViewSet)
router.register("teams", views.TeamViewSet)
router.register("onlineadmission", views.OnlineAdmissionViewSet)
router.register("campusbatches", views.CampusBatchViewSet)
router.register("aboutcampus", views.AboutCampusViewSet)
router.register("downloads", views.DownloadViewSet)
router.register("videolink", views.VideoGallerySet)

urlpatterns = router.urls
