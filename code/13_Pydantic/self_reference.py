from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2"),
        Comment(id=4, content="reply 3"),
        Comment(id=5, content="reply 4", replies=[
            Comment(id=6, content="nested reply")
        ]),
    ]
)