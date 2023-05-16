##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import Optional

from atproto.xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.bsky.notification.getUnreadCount`.

    Attributes:
        seenAt: Seen at.
    """

    seenAt: Optional[str] = None


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.bsky.notification.getUnreadCount`.

    Attributes:
        count: Count.
    """

    count: int