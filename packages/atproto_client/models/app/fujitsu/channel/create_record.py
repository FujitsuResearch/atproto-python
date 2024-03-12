import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client.models.unknown_type import UnknownInputType
from atproto_client.models import base


class Data(base.DataModelBase):

    """Parameters model for :obj:`app.fujitsu.channel.createRecord`."""

    channel_repo: str  #: Channel name.
    collection: str  #: The NSID of the record collection.
    record: 'UnknownInputType'  #: The record to create.
    rkey: t.Optional[str] = Field(default=None, max_length=15)  #: The key of the record.
    swapCommit: t.Optional[str] = Field(
        default=None, alias='swapCommit'
    )  #: Compare and swap with the previous commit by CID.
    validate: t.Optional[bool] = Field(default=True, alias='validate')  #: Flag for validating the record.
    

class DataDict(te.TypedDict):
    
    channel_repo: str  #: Channel name.
    collection: str  #: The NSID of the record collection.
    record: 'UnknownInputType'  #: The record to create.
    rkey: te.NotRequired[t.Optional[str]]  #: The key of the record.
    swapCommit: te.NotRequired[t.Optional[str]]  #: Compare and swap with the previous commit by CID.
    validate: te.NotRequired[t.Optional[bool]]  #: Flag for validating the record.


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.createRecord`."""

    cid: str  #: Cid.
    uri: str  #: Uri.
