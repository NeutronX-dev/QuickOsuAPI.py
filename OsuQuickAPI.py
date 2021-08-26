import requests
import math

class OsuAPI:
    def __init__(self, max_returns_per_request=51):
        self.return_per_request = max_returns_per_request
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,es;q=0.8",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

    def GetTopPlays(self, UserID, plays):
        TotalRequest = self.GetPlaysPerRequest(plays)
        res = []
        for i in range(len(TotalRequest)):
            limit = TotalRequest[i]
            offset = self.return_per_request * i
            URL = f'https://osu.ppy.sh/users/{UserID}/scores/best?mode=osu&offset={offset}&limit={limit}'
            req = requests.get(
                url=URL,
                headers=self.headers
            )
            res.extend(req.json())
        return res

    def GetRecentPlays(self, UserID, plays):
        TotalRequest = self.GetPlaysPerRequest(plays)
        res = []
        for i in range(len(TotalRequest)):
            limit = TotalRequest[i]
            offset = self.return_per_request * i
            URL = f'https://osu.ppy.sh/users/{UserID}/scores/recent?mode=osu&offset={offset}&limit={limit}'
            req = requests.get(
                url=URL,
                headers=self.headers
            )
            res.extend(req.json())
        return res

    def GetMapGlobalScores(self, MapID):
        res = []
        URL = f'https://osu.ppy.sh/beatmaps/{MapID}/scores?type=global'
        req = requests.get(
            url=URL,
            headers=self.headers
        )
        return req.json()

    def GetPlaysPerRequest(self, plays=100):
        times_fit = math.floor(plays / self.return_per_request)
        remaining = plays - self.return_per_request * times_fit
        res = []
        for i in range(times_fit):
            res.append(self.return_per_request)
        if (remaining > 0):
            res.append(remaining)
        return res
