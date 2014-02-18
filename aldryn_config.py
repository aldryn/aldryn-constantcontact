from aldryn_client import forms


class Form(forms.BaseForm):
    api_key = forms.CharField('Constant Contact API Key')
    token = forms.CharField('Constant Contact Token')
    default_list_id = forms.CharField('Constant Contact Default List ID')

    def to_settings(self, data, settings):
        settings['CONSTANTCONTACT_APIKEY'] = data['api_key']
        settings['CONSTANTCONTACT_TOKEN'] = data['token']
        settings['CONSTANTCONTACT_DEFAULT_LIST_ID'] = data['default_list_id']
        return settings
