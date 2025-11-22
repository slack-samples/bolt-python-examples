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
    EntityFullSizePreview
)

# Update the URL here to match your app's domain
sample_task_unfurl_url = "https://myappdomain.com/task"
sample_file_unfurl_url = "https://myappdomain.com/file"

sample_entities = {
    sample_task_unfurl_url: EntityMetadata(
        entity_type="slack#/entities/task",
        url=sample_task_unfurl_url,
        app_unfurl_url=sample_task_unfurl_url,
        external_ref=ExternalRef(id="sample_task_id"),
        entity_payload=EntityPayload(
            attributes=EntityAttributes(
                title=EntityTitle(
                    text="My Task",
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
    ),
    sample_file_unfurl_url: EntityMetadata(
        entity_type="slack#/entities/file",
        url=sample_file_unfurl_url,
        app_unfurl_url=sample_file_unfurl_url,
        external_ref=ExternalRef(id="sample_task_id"),
        entity_payload=EntityPayload(
            attributes=EntityAttributes(
                full_size_preview=EntityFullSizePreview(is_supported=True, preview_url="https://muertoscoffeeco.com/cdn/shop/articles/Why-Roast-Coffee-scaled_1000x.jpg?v=1592234291"),
                title=EntityTitle(
                    text="My File",
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
