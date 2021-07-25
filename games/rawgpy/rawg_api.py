import asyncio
import rawg


# documentation: https://api.rawg.io/docs/

async def requests():
    async with rawg.ApiClient() as api_client:
        # Create an instance of the API class
        api = rawg.GamesApi(api_client)

        # Making requests
        coros = [api.games_read(id=name) for name in ['grand-theft-auto-v', 'minecraft']]

        # Waiting for requests
        for coro in asyncio.as_completed(coros):
            game: rawg.GameSingle = await coro
            print('        Name |', game.name)
            print('    Released |', game.released)
            print('      Rating |', game.rating)
            print('Achievements |', game.achievements_count)
            print('     Website |', game.website)
            print('  Metacritic |', game.metacritic)
            print('    Playtime |', game.playtime)
            print('——————————————————————————————————————————————')






if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(requests())


'''
What are the most popular games in 2019?
GET https://api.rawg.io/api/games?dates=2019-01-01,2019-12-31&ordering=-added


GET https://api.rawg.io/api/platforms?key=YOUR_API_KEY
GET https://api.rawg.io/api/games?key=YOUR_API_KEY&dates=2019-09-01,2019-09-30&platforms=18,1,7

'''