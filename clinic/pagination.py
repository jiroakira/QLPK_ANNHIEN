from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'pagination_page'
    page_size_query_param = 'pagination_perpage'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({           
            'meta': {
                'page': self.page.number,
                'pages': self.page.paginator.num_pages,
                'perpage': self.page_size,
                'total': self.page.paginator.count,
            },
            'data': data,
        })