from django.conf import settings
from django.db import models

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


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    description = models.TextField()
    is_reached = models.BooleanField(default=False)
    is_statistics = models.BooleanField(default=False)

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
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="blog/thumbnails")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blogs"


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


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="team/")
    is_bod_team = models.BooleanField(default=False)
    is_administrative = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Team"


class Network(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="sponsors/")

    class Meta:
        verbose_name_plural = "Our Networks"


class Carrier(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    upload_document = models.FileField(upload_to="resource_and_media/")

    class Meta:
        verbose_name_plural = "Carriers"


class AboutSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    is_who_we_are = models.BooleanField(default=False)
    is_what_we_do = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Sections"


class AboutCategory(models.Model):
    """
    Dyamic dropdown thats way we make this

    """

    description = models.TextField()
    # Change from ForeignKey to OneToOneField

    about = models.OneToOneField(
        AboutSection, on_delete=models.CASCADE, related_name="about_categories"
    )

    class Meta:
        verbose_name_plural = "About Us Categories"


class ResourceAndMediaSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "ResourceAndMedia Sections"


class ResourceAndMediaCategory(models.Model):
    """
    Dyamic dropdown thats way we make this

    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upload_document = models.FileField(upload_to="resource_and_media/")
    about = models.ForeignKey(
        ResourceAndMediaSection,
        on_delete=models.CASCADE,
        related_name="resource_categories",
    )

    class Meta:
        verbose_name_plural = "ResourceAndMedia Categories"
