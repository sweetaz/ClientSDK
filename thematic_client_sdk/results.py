import requests
from .requester import Requestor

class Results(Requestor):

    def create(self, survey_id, job_id, result_type='published'):
        url = self.create_url('/survey/{}/result'.format(survey_id))
        fields = {'jobID': job_id, 'type': result_type, 'manualUploadAllowed': True}        
        response = requests.post(
            url, headers={'Authorization': 'bearer ' + self.access_token}, json=fields)
        if response.status_code != 200:
            raise Exception('Could not create result: ' +
                            str(response.text.replace('\\n', '\n')))