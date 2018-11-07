# pylint: disable=too-few-public-methods
from .data import Data
from .visualizations import Visualizations
from .surveys import Surveys
from .reports import Reports
from .upload_jobs import UploadJobs
from .organizations import Organizations
from .views import Views
from .results import Results


class ThematicClient(object):

    def __init__(self, access_token, api_url='https://client.getthematic.com/api'):
        self.api_url = api_url
        self.data = Data(access_token, api_url)
        self.organizations = Organizations(access_token, api_url)
        self.visualizations = Visualizations(access_token, api_url)
        self.surveys = Surveys(access_token, api_url)
        self.reports = Reports(access_token, api_url)
        self.views = Views(access_token, api_url)
        self.results = Results(access_token, api_url)
        self.upload_jobs = UploadJobs(access_token, api_url)
