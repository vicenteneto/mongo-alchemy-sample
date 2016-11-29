from werkzeug import exceptions


class BadRequest(exceptions.BadRequest):
    def __init__(self, form=None):
        super(BadRequest, self).__init__()
        BadRequest.form = form
