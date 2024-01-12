import typing as t

import typing_extensions as te
from pydantic import Field

from atproto_client.models import base


class Data(base.DataModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.addChannelMember`."""

    user_did: str = Field(alias='userDid')  #: User did.
    channel: str 


class DataDict(te.TypedDict):
    
    user_did: str  #: User did.
    channel: str 


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.addChannelMember`."""

    channel: str  #: Channel name.
    added_member: str  #: Did.
