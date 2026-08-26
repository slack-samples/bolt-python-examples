from slack_sdk import WebClient
from slack_sdk.models.blocks import PlainTextObject, SectionBlock

# Initialize (blocks.validate is unauthenticated, so no token is needed)
client = WebClient()

# Call the blocks.validate method
response = client.blocks_validate(
    blocks=[SectionBlock(text=PlainTextObject(text="Hello world"))],
)

# Inspect the response
print(response)
