import asyncio


class Handler(object):
    def __init__(self, loop=None):
        self.loop = asyncio.get_event_loop if loop is None else loop

    async def before_request(self, region, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried,
                                   e.g. ?key1=val&key2=val2
        """
        pass

    async def after_request(self, region, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        pass

    async def before_static_request(self, url, query_params):
        """
        Called before a request to DataDragon is processed
        :param url: The url that was requested
        """
        pass

    async def after_static_request(self, url, response):
        """
        Called after a response is received and before it is returned to the user.
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        pass