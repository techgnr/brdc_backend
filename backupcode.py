
# class Download(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     is_curriculum = models.BooleanField(default=False)
#     is_report = models.BooleanField(default=False)
#     is_form = models.BooleanField(default=False)
#     is_notice = models.BooleanField(default=False)
#     is_result = models.BooleanField(default=False)
#     created_at = models.TimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = "Downloads"


# class DownloadCategory(models.Model):
#     # want one to many field
#     title = models.CharField(max_length=255)
#     dowload = models.ForeignKey(
#         Download, on_delete=models.CASCADE, related_name="categories"
#     )
#     attachment = models.FileField(upload_to="downloads/")
#     created_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = "Download Categories"
#         ordering = ["-created_at"]  # DESCENDING order by created_at
