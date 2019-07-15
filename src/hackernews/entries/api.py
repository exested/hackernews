from django.http import JsonResponse
from django.views.generic import View
from .models import Entry


class EntryList(View):
    DEFAULT_LIMIT = 5
    DEFAULT_OFFSET = 0
    DEFAULT_ORDER = 'id'

    def get_limit(self):
        try:
            return int(self.request.GET.get('limit', self.DEFAULT_LIMIT))
        except ValueError:
            pass
        return self.DEFAULT_LIMIT

    def get_offset(self):
        try:
            return int(self.request.GET.get('offset', self.DEFAULT_OFFSET))
        except ValueError:
            pass
        return self.DEFAULT_OFFSET

    def get_order(self):
        order = self.request.GET.get('order')
        if order:
            asc_desc = ''
            if order[0] == '-':
                asc_desc = '-'
                order = order[1:]

            fields = [item.name for item in Entry._meta.get_fields()]
            if order in fields:
                self.order = asc_desc+order
            return self.order

        return self.DEFAULT_ORDER

    def queryset(self):
        limit = self.get_limit()
        offset = self.get_offset()
        order = self.get_order()
        entry_list = Entry.objects.all().order_by(order)[offset:limit]
        return entry_list

    def get_total_count(self):
        return Entry.objects.count()

    def entry_serialise(self, entry):
        return {
            'id': entry.id,
            'title': entry.title,
            'url': entry.url,
            'created': entry.created.isoformat(),
        }

    def get(self, request):
        entry_list = [self.entry_serialise(entry) for entry in self.queryset()]
        response = JsonResponse({
            'entry_list': entry_list,
            'total_count': self.get_total_count(),
        })
        return response


