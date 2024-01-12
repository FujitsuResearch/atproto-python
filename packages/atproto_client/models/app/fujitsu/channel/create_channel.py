import typing as t

import typing_extensions as te
from pydantic import Field

from atproto_client.models import base


class Data(base.DataModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.createChannel`."""

    channel_name: str = Field(alias='channelName') #: Channel name.


class DataDict(te.TypedDict):
    
    channel_name: str  #: Channel name.


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.createChannel`."""

    handle: str  #: Handle
