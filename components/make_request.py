# -*- coding: utf-8 -*-
import requests
from meya import Component


class MakeRequest(Component):
    def start(self):
        try:
            response = requests.get(self.db.flow.get('url'), timeout=10)
        except:
            response = None

        is_up = "⬇ Down"
        if response:
            if response.status_code >= 200 and response.status_code < 300:
                is_up = "⬆ Up"

        self.db.bot.set('is_up', is_up)
            
        return self.respond(action="next")
