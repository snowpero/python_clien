#-*- coding: utf-8 -*-
import json

class ClienDetailReplyItem:
    """
    This is Clien Board Item Data Class.
    """
    date = ''
    text = ''
    isAddReply = False

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)