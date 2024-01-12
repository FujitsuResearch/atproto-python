import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
from atproto_client.models import base


class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.listJoinedChannels`."""
    
    pass

class ParamsDict(te.TypedDict):
    
    pass


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.createChannel`."""

    channels: t.List[str]  #: List of channels
