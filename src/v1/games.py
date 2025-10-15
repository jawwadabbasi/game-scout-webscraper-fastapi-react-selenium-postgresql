from v1.scraper import Scraper
from includes.db import Db
from includes.models import Game

class Games:

    def ScrapeSteam():

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        Scraper.Steam()

        api_data['ApiHttpResponse'] = 200
        api_data['ApiMessages'] += ['Request processed successfully']

        return api_data

    def Get():

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            with Db.SessionScope() as session:

                results = session.query(Game).all()

                api_data["ApiResult"] = [
                    {
                        "Id": g.id,
                        "Title": g.title,
                        "Vendor": g.vendor,
                        "Platform": g.platform,
                        "Rating": g.rating,
                        "Price": g.selling_price,
                        "Discount": g.discount,
                        "ReleaseDate": g.release_date,
                        "Link": g.link,
                    }
                    for g in results
                ]

        except Exception as e:
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Failed to get results: ', e]

            return api_data

        api_data['ApiHttpResponse'] = 200
        api_data['ApiMessages'] += ['Request processed successfully']

        return api_data
    
    def GetById(game_id):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            game_id = int(game_id)

        except:
            api_data['ApiHttpResponse'] = 400
            api_data['ApiMessages'] += ['ERROR - Invalid arguments']

            return api_data

        try:
            with Db.SessionScope() as session:
                
                game = session.query(Game).filter(Game.id == game_id).first()

                if not game:
                    api_data['ApiHttpResponse'] = 404
                    api_data['ApiMessages'] += ['INFO - No records found']

                    return api_data

                api_data["ApiResult"] = [
                    {
                        "Id": game.id,
                        "Title": game.title,
                        "Vendor": game.vendor,
                        "Platform": game.platform,
                        "Rating": game.rating,
                        "Price": game.selling_price,
                        "Discount": game.discount,
                        "ReleaseDate": game.release_date,
                        "Link": game.link,
                    }
                ]

        except Exception as e:
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Failed to get results: ', e]

            return api_data

        api_data['ApiHttpResponse'] = 200
        api_data['ApiMessages'] += ['Request processed successfully']

        return api_data