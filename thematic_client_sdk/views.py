# pylint: disable=too-few-public-methods
import requests
from .requester import Requestor


class Views(Requestor):

    def create(self, organization, survey_id, view_name, view_config='{}', manualUploadAllowed=True):
        url = self.create_url('/survey/{}/view?organization={}'.format(survey_id, organization))
        fields = {'configuration': view_config, 'name':view_name, 'manualUploadAllowed': True}
        response = requests.post(
            url, headers={'Authorization': 'bearer ' + self.access_token}, json=fields)
        if response.status_code != 200:
            raise Exception('Could not create view: ' +
                            str(response.text.replace('\\n', '\n')))
        return response
