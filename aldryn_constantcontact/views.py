import json
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from pyrate.services import constantcontact


def submit_form(request):
    h = constantcontact.ConstantContactPyrate(
        api_key=settings.CONSTANTCONTACT_APIKEY,
        token=settings.CONSTANTCONTACT_TOKEN,
    )

    list_id = request.POST.get('list_id') or settings.CONSTANTCONTACT_DEFAULT_LIST_ID
    success, raw = h.create_contact(request.POST.get('email'), list_id, 'ACTION_BY_VISITOR')
    content = json.loads(raw)

    # We're ignoring already registered
    if success or content[0][u'error_key'] == 'http.status.email_address.conflict':
        if request.POST.get('redirect_url'):
            return HttpResponseRedirect(request.POST.get('redirect_url'))
        return HttpResponse(status=200)

    raise Exception(content)
