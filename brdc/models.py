from django.conf import settings
from django.db import models


class CarouselButton(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


# Create your models here.


class Carousel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        verbose_name_plural = "HomePage Banners"


class CarouselItem(models.Model):
    carousel = models.ForeignKey(
        Carousel, on_delete=models.CASCADE, related_name="items"
    )
    heading = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="carousel/")
    primary_button_label = models.CharField(max_length=255, blank=True, null=True)
    primary_button_link = models.CharField(max_length=255, blank=True, null=True)
    secondary_button_label = models.CharField(max_length=255, blank=True, null=True)
    secondary_button_link = models.CharField(max_length=255, blank=True, null=True)


class Facility(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="facilities/")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Facilities"


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()

    class Meta:
        verbose_name_plural = "Milestones"


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="album/")

    class Meta:
        verbose_name_plural = "Image Gallery"


class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="album/")

    class Meta:
        verbose_name_plural = "Album Images"


class VideoGallery(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Video Gallery"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    # content = RichTextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="blog/thumbnails")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blogs"


class UserReview(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="review/")
    review = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "User Reviews"


class ContactUs(models.Model):
    full_name = models.CharField(
        max_length=255,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    phone_no = models.CharField(
        max_length=15,
    )
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"


class PopUp(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pop_up/")

    class Meta:
        verbose_name_plural = "Important Notice"


class CampusChiefMessage(models.Model):
    heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="campus_chief_message/")

    class Meta:
        verbose_name_plural = "Campus Chief Message"


class Courses(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses/")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Courses"


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonials/")
    description = models.TextField()
    position = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Testimonials-Reviews"


class Suggestion(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Suggestions"


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    service = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="team/")
    is_management = models.BooleanField(default=False)
    is_administrative = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Team"


class OnlineAdmission(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Online Admission"


# here we use the implementation of the realtionship in the django project of the school


class CampusBatch(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Campus Batches"


class Student(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.FloatField()
    image = models.ImageField(upload_to="students/")
    slc_batch = models.ForeignKey(
        CampusBatch, related_name="students", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Students"


class AboutCampus(models.Model):
    title = models.CharField(max_length=255)
    # description = RichTextField() LTER IN PRODUCTION RIGHT
    description = models.TextField()
    image = models.ImageField(upload_to="about_school/")

    class Meta:
        verbose_name_plural = "About Campus"


class Download(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_curriculum = models.BooleanField(default=False)
    is_report = models.BooleanField(default=False)
    is_form = models.BooleanField(default=False)
    is_notice = models.BooleanField(default=False)
    is_result = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Downloads"


class DownloadCategory(models.Model):
    # want one to many field
    title = models.CharField(max_length=255)
    dowload = models.ForeignKey(
        Download, on_delete=models.CASCADE, related_name="categories"
    )
    attachment = models.FileField(upload_to="downloads/")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Download Categories"
        ordering = ["-created_at"]  # DESCENDING order by created_at
