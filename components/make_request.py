# -*- coding: utf-8 -*-
import requests
from meya import Component


class MakeRequest(Component):

    def start(self):
        response = requests.get(self.db.flow.get('url'))
        print response.status_code
        return self.respond(action="next")
