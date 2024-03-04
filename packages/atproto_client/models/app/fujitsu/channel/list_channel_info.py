import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
from atproto_client.models import base


class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.listChannelInfo`."""
    
    pass

class ParamsDict(te.TypedDict):
    
    pass


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.listChannelInfo`."""

    channel_info: t.List['models.AppFujitsuChannelDefs.ChannelInfo']  #: List of ChannelInfo
    
