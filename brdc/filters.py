from django_filters import rest_framework as filters
from brdc.models import AboutSection, Milestone


class AboutSectionFilter(filters.FilterSet):
    is_who_we_are = filters.BooleanFilter(field_name="is_who_we_are")
    is_what_we_do = filters.BooleanFilter(field_name="is_what_we_do")
    # created_at = filters.DateTimeFilter(field_name="created_at")

    class Meta:
        model = AboutSection
        fields = []


class MilestoneFilter(filters.FilterSet):
    is_reached = filters.BooleanFilter(field_name="is_reached")
    is_statistics = filters.BooleanFilter(field_name="is_statistics")
    # created_at = filters.DateTimeFilter(field_name="created_at")

    class Meta:
        model = Milestone
        fields = []
