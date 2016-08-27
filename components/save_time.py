# -*- coding: utf-8 -*-
import arrow
from meya import Component


class SaveTime(Component):

    def start(self):
        scope = self.properties.get('scope') or "flow"
        key = self.properties['key']
        db = {
            'flow': self.db.flow,
            'user': self.db.user,
            'bot': self.db.bot
        }[scope]
        val = arrow.utcnow().to('US/Pacific').format("MMM. D @ H:mm ET")
        db.set(key, val)
        return self.respond(action="next")
