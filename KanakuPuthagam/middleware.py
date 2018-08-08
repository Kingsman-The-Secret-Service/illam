from calendar import monthrange
from datetime import datetime

def DurationMiddleware(get_response):

    def middleware(request):

        today = datetime.today()
        startDate = datetime(today.year, today.month, 1).strftime('%d-%m-%Y')
        endDate =datetime(today.year, today.month, monthrange(today.year, today.month)[1]).strftime('%d-%m-%Y')

        if 'startDate' not in request.session.keys():
            request.session['startDate'] = startDate
        if 'endDate' not in request.session.keys():   
            request.session['endDate'] = endDate

        response = get_response(request)

        return response

    return middleware