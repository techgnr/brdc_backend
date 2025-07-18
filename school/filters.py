from django_filters import rest_framework as filters
from .models import Download


class DownloadsFilter(filters.FilterSet):
    is_curriculum = filters.BooleanFilter(field_name="is_curriculum")
    is_report = filters.BooleanFilter(field_name="is_report")
    is_form = filters.BooleanFilter(field_name="is_form")
    is_notice = filters.BooleanFilter(field_name="is_notice")
    is_result = filters.BooleanFilter(field_name="is_result")
    created_at = filters.DateTimeFilter(field_name="created_at")

    class Meta:
        model = Download
        fields = []


# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.select_related('user', 'permanent_address').all()
#     serializer_class = PersonSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = PersonFilter
