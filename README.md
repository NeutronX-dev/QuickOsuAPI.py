# osu-quick-api (for Python)
Simple osu! api usage without an API key.

# File Exports
## `OsuAPI`
It is simple to start using this library. Just build `OsuAPI` object and start using the methods. The parameter for the constructor is optional. It is how many plays you want to retrieve per request, maximum is 51, the API will not send more than that.

### `GetTopPlays(UserID, plays)`:
#### Parameters:
> `UserID`: User ID. For exmaple, in **`osu.ppy.sh/users/4787150`** the `UserID` would be **`4787150`**
> `plays`: How many plays you want to retrieve.
#### Returns
> `[{...}, {...}]`: An array of dictionaries (JSON). ([Structure](#returns-structure))

### `GetRecentPlays(UserID, plays)`:
#### Parameters:
> `UserID`: User ID. For exmaple, in **`osu.ppy.sh/users/4787150`** the `UserID` would be **`4787150`**
> `plays`: How many plays you want to retrieve.
#### Returns
> `[{...}, {...}]`: An array of dictionaries (JSON). ([Structure](#returns-structure))

# Returns Structure
The methods `GetTopPlays`, `GetRecentPlays` return an **__array__** of the following dictionaries (JSON):
```json
{
    "id": 0,
    "user_id": 0,
    "accuracy": 0,
    "mods": [""],
    "score": 0,
    "max_combo": 0,
    "passed": false,
    "perfect": false,
    "statistics": {
        "count_50": 0,
        "count_100": 0,
        "count_300": 0,
        "count_geki": 0,
        "count_katu": 0,
        "count_miss": 0
    },
    "rank": "",
    "created_at": "",
    "best_id": 0,
    "pp": 0,
    "mode": "",
    "mode_int": 0,
    "replay": false,
    "beatmap": {
        "beatmapset_id": 0,
        "difficulty_rating": 0,
        "id": 0,
        "mode": "",
        "status": "",
        "total_length": 0,
        "user_id": 0,
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "bpm": 0,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "cs": 0,
        "deleted_at": "",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 0,
        "url": "",
        "checksum": ""
    },
    "beatmapset": {
        "artist": "",
        "artist_unicode": "",
        "covers": {
            "cover": "",
            "cover@2x": "",
            "card": "",
            "card@2x": "",
            "list": "",
            "list@2x": "",
            "slimcover": "",
            "slimcover@2x": ""
        },
        "creator": "",
        "favourite_count": 0,
        "hype": "",
        "id": 0,
        "nsfw": false,
        "play_count": 0,
        "preview_url": "",
        "source": "",
        "status": "ranked | unranked",
        "title": "",
        "title_unicode": "",
        "user_id": 0,
        "video": false
    },
    "weight": {
        "percentage": 0,
        "pp": 0
    },
    "user": {
        "avatar_url": "",
        "country_code": "",
        "default_group": "",
        "id": 0,
        "is_active": false,
        "is_bot": false,
        "is_deleted": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "",
        "pm_friends_only": false,
        "profile_colour": "",
        "username": ""
    }
}
```

# Code Example
## Printing three top Plays
### Code
```py
from PlaysFetch import OsuAPI
API = OsuAPI()

LastTopPlays = API.GetTopPlays("4787150", 3)
for Play in LastTopPlays:
    print("======================================")
    print(f'{Play["beatmapset"]["title"]} [{Play["beatmap"]["version"]}]')
    print(f'Stars: {Play["beatmap"]["difficulty_rating"]}')
    print(f'Mods: {"".join(Play["mods"])}')
    print(f'BPM: {Play["beatmap"]["bpm"]}')
    print(f'AR: {Play["beatmap"]["ar"]}')
    print(f'Gained: {Play["pp"]}pp')
```
### Console
```
======================================
Wizard's Tower [Ultimate Magic]
Stars: 6.55
Mods: HDDT
BPM: 175
AR: 9.4
Gained: 1092.91pp
======================================
UNION!! [We are all MILLION!!]
Stars: 6.21
Mods: HDDT
BPM: 172
AR: 9.2
Gained: 1029.95pp
======================================
Tsukinami [Nostalgia]
Stars: 6.1
Mods: HDDT
BPM: 180
AR: 9.2
Gained: 1021.26pp
```

# LICENSE
![gnu-logo](logos/gplv3-88x31.png)

This program is free software: you can redistribute it and/or modify
it under the terms of the [GNU General Public License](https://github.com/NeutronX-dev/ws.js/blob/main/LICENSE) as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.