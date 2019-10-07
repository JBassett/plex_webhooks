# Plex Webhooks

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [Plex Webhooks][plex_webhooks]._

## What this integration adds
This is a custom component that will take in webhooks from Plex and turn them into events that you can write automations around.  One usecase is when plex starts playing on living room TV dim the kitchen lights and turn out all the living room lights.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `plex_webhooks`.
4. Download _all_ the files from the `custom_components/plex_webhooks/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Update configuration.yaml to include needed config below.
7. Restart Home Assistant.
8. Login to plex and add a [webook][plex_webhook_location] with the url of `{{HAS_URL}}/api/webhooks/{{webhook_id}}` where HAS_URL is the url that you can reach Home Assistant and webhook_id is the id you setup in the configuration.yaml
8. Write awesome automations around the new events!

## Example configuration.yaml

```yaml
plex_webhooks:
  webhook_id: plex_webhook
```

## Configuration options

Key | Type | Required | Description
-- | -- | -- | --
`webhook_id` | `string` | `True` | The webhook id used when configuring plex.

## What the event data actually means
In addition to the whole plex webhook json being passed (https://support.plex.tv/articles/115002267687-webhooks/) we add 2 additional fields.
* status - This is an easy field to use to determine what is happening it can be 3 values.
  * PLAYING - When someone starts playing any media.
  * STOPPED - When someone stops playing any media.
  * NEW - When new media is added to the server.
* playerUuid - This is a unique id for the player that is playing, great for if you want to filter to events for one player.

Example Music Data:
```json
{
    "event_type": "PLEX_EVENT",
    "data": {
        "event": "media.stop",
        "user": false,
        "owner": true,
        "Account": {
            "id": 123456789,
            "thumb": "https://plex.tv/users/XXXXXXXX/avatar?c=XXXXXXX",
            "title": "john.doe@example.com"
        },
        "Server": {
            "title": "ssv Normandy",
            "uuid": "123456789abcd"
        },
        "Player": {
            "local": false,
            "publicAddress": "192.168.x.x",
            "title": "Living Room TV",
            "uuid": "123456789abcd"
        },
        "Metadata": {
            "librarySectionType": "artist",
            "ratingKey": "14454",
            "key": "/library/metadata/14454",
            "parentRatingKey": "14453",
            "grandparentRatingKey": "14452",
            "guid": "com.plexapp.agents.plexmusic://gracenote/track/170163331-DF725E4DA03E6040915B2564D5A06E70/170163337-1EB863722EF8D07A087D4258B2FFA2D6?lang=en",
            "parentGuid": "com.plexapp.agents.plexmusic://gracenote/album/05DF725E0A247C83/170163331-DF725E4DA03E6040915B2564D5A06E70?lang=en",
            "grandparentGuid": "com.plexapp.agents.plexmusic://gracenote/artist/05DF725E0A247C83?lang=en",
            "librarySectionTitle": "Music",
            "librarySectionID": 4,
            "librarySectionKey": "/library/sections/4",
            "type": "track",
            "title": "You Belong With Me",
            "grandparentKey": "/library/metadata/14452",
            "parentKey": "/library/metadata/14453",
            "grandparentTitle": "Taylor Swift",
            "parentTitle": "Fearless",
            "originalTitle": "Taylor Swift",
            "summary": "",
            "index": 6,
            "parentIndex": 1,
            "ratingCount": 4219823,
            "thumb": "/library/metadata/14453/thumb/1491873574",
            "art": "/library/metadata/14452/art/1569915711",
            "parentThumb": "/library/metadata/14453/thumb/1491873574",
            "grandparentThumb": "/library/metadata/14452/thumb/1569915711",
            "grandparentArt": "/library/metadata/14452/art/1569915711",
            "addedAt": 1491873349,
            "updatedAt": 1567174880
        },
        "playerUuid": "14684678d4b104c305387744dcf82238",
        "status": "STOPPED"
    }
}
```

***

[plex_webhooks]: https://github.com/JBassett/plex_webhooks
[plex_webhook_location]: https://app.plex.tv/desktop#!/settings/webhooks
[commits-shield]: https://img.shields.io/github/commit-activity/y/JBassett/plex_webhooks.svg?style=for-the-badge
[commits]: https://github.com/JBassett/plex_webhooks/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[maintenance-shield]: https://img.shields.io/badge/maintainer-Justin%20Bassett%20%40JBassett-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/JBassett/plex_webhooks.svg?style=for-the-badge
[releases]: https://github.com/JBassett/plex_webhooks/releases
