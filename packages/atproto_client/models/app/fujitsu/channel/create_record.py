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
    swap_commit: t.Optional[str] = None  #: Compare and swap with the previous commit by CID.
    validate_: t.Optional[bool] = None  #: Can be set to 'false' to skip Lexicon schema validation of record data.
    

class DataDict(te.TypedDict):
    
    channel_repo: str  #: Channel name.
    collection: str  #: The NSID of the record collection.
    record: 'UnknownInputType'  #: The record to create.
    rkey: te.NotRequired[t.Optional[str]]  #: The key of the record.
    swap_commit: te.NotRequired[t.Optional[str]]  #: Compare and swap with the previous commit by CID.
    validate: te.NotRequired[
        t.Optional[bool]
    ]  #: Can be set to 'false' to skip Lexicon schema validation of record data.


class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.fujitsu.channel.createRecord`."""

    cid: str  #: Cid.
    uri: str  #: Uri.
