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
        val = arrow.utcnow().to('US/Eastern').format("MMM. D @ H:mma ET")
        db.set(key, val)
        return self.respond(action="next")
