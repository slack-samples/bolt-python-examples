from slack_sdk.models.metadata import (
    EntityMetadata,
    EntityType,
    ExternalRef,
    EntityPayload,
    EntityAttributes,
    EntityTitle,
    TaskEntityFields,
    EntityStringField,
    EntityTitle,
    EntityAttributes,
    TaskEntityFields,
    EntityStringField,
    EntityEditSupport,
    EntityCustomField,
    ExternalRef,
)

# Update the URL here to match your app's domain
sample_task_unfurl_url = "https://wo-python-nov2025.com/task"

sample_entities = {
    sample_task_unfurl_url: EntityMetadata(
        entity_type="slack#/entities/task",
        url=sample_task_unfurl_url,
        app_unfurl_url=sample_task_unfurl_url,
        external_ref=ExternalRef(id="sample_task_id"),
        entity_payload=EntityPayload(
            attributes=EntityAttributes(
                title=EntityTitle(
                    text="My Title",
                    edit=EntityEditSupport(enabled=True),
                )
            ),
            fields=TaskEntityFields(
                description=EntityStringField(
                    value="Hello World!",
                    edit=EntityEditSupport(enabled=True)
                    )
                ),
            custom_fields=[
                EntityCustomField(
                    key="hello-world",
                    label="hello-world",
                    value="hello-world",
                    type="string",
                )
            ],
        ),
    )
}
