class QueryParameter(object):
    pass


class PageQueryParameter(QueryParameter):

    def __init__(self, offset: int = 0, limit: int = 100):
        self.offset = offset
        self.limit = limit


async def page_parameter(offset: int = 0, limit: int = 100) -> PageQueryParameter:
    return PageQueryParameter(offset, limit)
