import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
    from atproto_client.models.unknown_type import UnknownType
from atproto_client.models import base


class ChannelInfo(base.ModelBase):
    
    """Definition model for :obj:`app.fujitsu.channel.defs`."""
    
    channel_did: str  #: Did.
    channel_handle: str  #: Handle.
    public_type: int  #: Public type.
    created_at: str  #: Created at.
    display_name: str  #: Display name.
    metadata: str  #: Metadata.

    py_type: te.Literal['app.fujitsu.channel.defs#channelInfo'] = Field(
        default='app.fujitsu.channel.defs#channelInfo', alias='$type', frozen=True
    )
    