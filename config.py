import re

import requests
import logging

SESSION = requests.Session()

APP_URL = "http://localhost:8080"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin"

LOG = logging.getLogger()


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "******")
        record.msg = re.sub(r'Authrization.*?,','Authrization\': \'******\', ', str(record.msg))
        return True


LOG.addFilter(HideSensitiveData())
