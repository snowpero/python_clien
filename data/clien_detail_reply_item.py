#-*- coding: utf-8 -*-
import json

class ClienDetailReplyItem:
    """
    This is Clien Board Item Data Class.
    """
    user = ''
    date = ''
    text = ''
    isAddReply = False
    hasImgId = False
    imgUrl = ''

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)