"""Support for plex webhooks."""
import json
import logging

import requests
import voluptuous as vol

import aiohttp

from homeassistant.const import CONF_WEBHOOK_ID
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

EVENT_RECEIVED = "PLEX_EVENT"

DOMAIN = "plex_webhooks"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_WEBHOOK_ID): cv.string
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def handle_webhook(hass, webhook_id, request):
    """Handle webhook callback."""
    logging.debug('Got plex webhook.')

    data = {}
    
    try:
        body = await request.text()
        # This is bad, but I don't see a better way to extract just the json...
        raw_json = body[body.index('{'):body.rindex('}')+1]
        data = json.loads(raw_json) if body else {}
    except ValueError:
        logging.warn('Issue decoding webhook: ' + raw_json)
        return None
    except:
        logging.debug('Ignoring webhook, must be a photo?')
        return None

    data['playerUuid'] = data['Player']['uuid']

    event = data['event']
    playing = ['media.play', 'media.resume']
    stopped = ['media.pause', 'media.stop']
    grabbed = ['library.new']
    
    if event in playing:
        logging.debug('Plex started playing')
        data['status'] = 'PLAYING'
    elif event in stopped:
        logging.debug('Plex stopped playing')
        data['status'] = 'STOPPED'
    elif event in grabbed:
        logging.debug('Plex got new media')
        data['status'] = 'GRABBED'

    hass.bus.async_fire(EVENT_RECEIVED, data)

async def async_setup(hass, config):
    logging.debug('Initing Plex Webhooks!')
    webhook_id = config[DOMAIN][CONF_WEBHOOK_ID]
    hass.components.webhook.async_register(
        DOMAIN, "Plex", webhook_id, handle_webhook
    )
    return True
