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

1. Click install.
2. Configure the integration (see below for how)
3. Restart Home Assistant
4. Login to plex and add a [webook][plex_webhook_location] with the url of `{{HAS_URL}}/api/webhooks/{{webhook_id}}` where HAS_URL is the url that you can reach Home Assistant and webhook_id is the id you setup in the configuration.yaml
3. Write awesome automations around the new events!

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
  * PLAYING - When someone starts playing any media. Both `media.play` and `media.resume` events.
  * STOPPED - When someone stops playing any media. Both `media.pause` and `media.stop` events.
  * NEW - When new media is added to the server.  The `library.new` event.
* playerUuid - This is a unique id for the player that is playing, great for if you want to filter to events for one player.  The `Player->uuid` value.

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
