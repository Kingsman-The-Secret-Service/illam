class IsOwnerFilterBackend():
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user.id)        