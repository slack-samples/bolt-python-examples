import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.models.metadata import EventAndEntityMetadata
from metadata import sample_entities


# Initializes your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# Listens for the link_shared event
# https://docs.slack.dev/reference/events/link_shared/
@app.event("link_shared")
def link_shared_callback(event: dict, client: WebClient, logger: logging.Logger):
    try:
        for link in event["links"]:
            entity = sample_entities[link["url"]]
            if entity is not None:
                client.chat_unfurl(
                    channel=event["channel"],
                    ts=event["message_ts"],
                    metadata=EventAndEntityMetadata(entities=[entity]),
                )
            else:
                logger.info("No entity found with URL " + link)
    except Exception as e:
        logger.error(
            f"An error occurred while handling the entity_details_requested event: {type(e).__name__} - {str(e)}",
            exc_info=e,
        )


# Listens for the entity_details_requested event, which is sent when a user opens the flexpane
# https://docs.slack.dev/reference/events/entity_details_requested/
@app.event("entity_details_requested")
def entity_details_callback(event: dict, client: WebClient, logger: logging.Logger):
    try:
        entity_url = event["entity_url"]
        entity = sample_entities[entity_url]
        if entity is not None:
            client.entity_presentDetails(
                trigger_id=event["trigger_id"], metadata=entity
            )
        else:
            logger.info("No entity found with URL " + entity_url)
    except Exception as e:
        logger.error(
            f"An error occurred while handling the entity_details_requested event: {type(e).__name__} - {str(e)}",
            exc_info=e,
        )


# Listens for the view_submission event sent when the user submits edits in the flexpane
# https://docs.slack.dev/tools/bolt-js/concepts/view-submissions/
# https://docs.slack.dev/messaging/work-objects/#editing-view-submission
@app.view_submission("work-object-edit")
def work_object_edit_callback(view: dict, body: dict, client: WebClient, logger: logging.Logger, ack):
    try:
        ack()

        entity_url = view["entity_url"]
        entity = sample_entities[entity_url]

        attributes = entity.entity_payload.entity_attributes
        attributes.title.text = view["state"]["values"]["title"]["title.input"]["value"]
        entity.entity_payload.entity_attributes = attributes
        
        entity.entity_payload.fields.description.value = view["state"]["values"]["description"]["description.input"]["value"]
        
        if entity is not None:
            client.entity_presentDetails(
                trigger_id=body["trigger_id"], metadata=entity
            )
        else:
            logger.info("No entity found with URL " + entity_url)
    except Exception as e:
        logger.error(
            f"An error occurred while handling the entity_details_requested event: {type(e).__name__} - {str(e)}",
            exc_info=e,
        )


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
