import aiohttp
class Conditions:
    """
    An asynchronous class to handle requests for condition data from the Polygon.io API.

    Attributes:
        api_key (str): The Polygon.io API key.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.BASE_URL = f"https://api.polygon.io/v3/reference/conditions?apiKey={self.api_key}"



    async def get_conditions(self, asset_class=None, data_type=None, id=None, sip=None, order=None, limit=1000, sort=None):
        """
        Retrieves conditions from the Polygon.io API based on the provided parameters.

        Parameters:
            asset_class (str): Filter for conditions within a given asset class.
            data_type (str): Filter by data type.
            id (int): Filter for conditions with a given ID.
            sip (str): Filter by SIP.
            order (str): Order results based on the sort field.
            limit (int): Limit the number of results returned, default is 10 and max is 1000.
            sort (str): Sort field used for ordering.

        Returns:
            list: A list of conditions that match the query.
        """

        params = {
            "asset_class": asset_class,
            "data_type": data_type,
            "id": id,
            "sip": sip,
            "order": order,
            "limit": limit,
            "sort": sort
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params=params) as response:
                response.raise_for_status()
                data = await response.json()
                return data["results"]

    async def get_conditions_map(self):
        """
        Retrieve a dictionary mapping condition IDs to their corresponding condition definitions.

        :return: A dictionary with condition IDs as keys and condition definitions as values.
        """
        conditions = await self.get_conditions()
        return {cond["id"]: cond for cond in conditions}