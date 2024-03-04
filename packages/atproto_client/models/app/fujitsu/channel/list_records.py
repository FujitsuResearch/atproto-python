import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
    from atproto_client.models.unknown_type import UnknownType
from atproto_client.models import base


class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.listRecords`."""
    
    channel_repo: str  #: Channel name
    collection: str  #: The NSID of the record collection.
    cursor: t.Optional[str] = None  #: Cursor.
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)  #: Limit.
    reverse: t.Optional[bool] = None  #: Flag to reverse the order of the returned records.
    

class ParamsDict(te.TypedDict):
    channel_repo: str  #: Channel name.
    collection: str  #: The NSID of the record collection.
    cursor: te.NotRequired[t.Optional[str]]  #: Cursor.
    limit: te.NotRequired[t.Optional[int]]  #: Limit.
    reverse: te.NotRequired[t.Optional[bool]]  #: Flag to reverse the order of the returned records.


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.listChannelRecords`."""

    records: t.List['models.AppFujitsuChannelListChannelRecords.Record']  #: Records.
    cursor: t.Optional[str] = None  #: Cursor.


class Record(base.ModelBase):

    """Definition model for :obj:`app.fujitsu.channel.listRecords`."""

    cid: str  #: Cid.
    uri: str  #: Uri.
    value: 'UnknownType'  #: Value.

    py_type: te.Literal['app.fujitsu.channel.listRecords#record'] = Field(
        default='app.fujitsu.channel.listRecords#record', alias='$type', frozen=True
    )
