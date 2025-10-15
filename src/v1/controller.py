import inspect

from services.logger import Logger
from v1.games import Games

class Ctrl_v1:

    def Response(endpoint, request_data=None, api_data=None, log=True):

        if log is True:
            Logger.CreateServiceLog(endpoint, request_data, api_data)

        return api_data

    def BadRequest(endpoint, request_data=None):

        api_data = {}
        api_data['ApiHttpResponse'] = 400
        api_data['ApiMessages'] = ['ERROR - Missing required parameters']
        api_data['ApiResult'] = []

        Logger.CreateServiceLog(endpoint, request_data, api_data)

        return api_data

    def GetGames(request_data):

        api_data = Games.Get()

        return Ctrl_v1.Response(inspect.stack()[0][3], request_data, api_data)
    
    def GetGameById(game_id):

        if not game_id:
            return Ctrl_v1.BadRequest(inspect.stack()[0][3], {"Id": game_id})

        api_data = Games.GetById(
            game_id,
        )

        return Ctrl_v1.Response(inspect.stack()[0][3], {"Id": game_id}, api_data)
    
    def ScrapeSteam(request_data):

        api_data = Games.ScrapeSteam()

        return Ctrl_v1.Response(inspect.stack()[0][3], request_data, api_data)