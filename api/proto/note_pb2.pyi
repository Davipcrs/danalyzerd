from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBoolRequest(_message.Message):
    __slots__ = ("id_note", "bool_complete")
    ID_NOTE_FIELD_NUMBER: _ClassVar[int]
    BOOL_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    id_note: int
    bool_complete: bool
    def __init__(self, id_note: _Optional[int] = ..., bool_complete: bool = ...) -> None: ...

class Note(_message.Message):
    __slots__ = ("id_note", "str_text", "str_md_text", "str_date", "bool_completed")
    ID_NOTE_FIELD_NUMBER: _ClassVar[int]
    STR_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_MD_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_DATE_FIELD_NUMBER: _ClassVar[int]
    BOOL_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id_note: int
    str_text: str
    str_md_text: str
    str_date: str
    bool_completed: bool
    def __init__(self, id_note: _Optional[int] = ..., str_text: _Optional[str] = ..., str_md_text: _Optional[str] = ..., str_date: _Optional[str] = ..., bool_completed: bool = ...) -> None: ...

class CreateNoteRequest(_message.Message):
    __slots__ = ("str_text", "str_md_text", "str_date", "bool_completed")
    STR_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_MD_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_DATE_FIELD_NUMBER: _ClassVar[int]
    BOOL_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    str_text: str
    str_md_text: str
    str_date: str
    bool_completed: bool
    def __init__(self, str_text: _Optional[str] = ..., str_md_text: _Optional[str] = ..., str_date: _Optional[str] = ..., bool_completed: bool = ...) -> None: ...

class GetNoteRequest(_message.Message):
    __slots__ = ("id_note",)
    ID_NOTE_FIELD_NUMBER: _ClassVar[int]
    id_note: int
    def __init__(self, id_note: _Optional[int] = ...) -> None: ...

class UpdateNoteRequest(_message.Message):
    __slots__ = ("id_note", "str_text", "str_md_text", "str_date", "bool_completed")
    ID_NOTE_FIELD_NUMBER: _ClassVar[int]
    STR_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_MD_TEXT_FIELD_NUMBER: _ClassVar[int]
    STR_DATE_FIELD_NUMBER: _ClassVar[int]
    BOOL_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id_note: int
    str_text: str
    str_md_text: str
    str_date: str
    bool_completed: bool
    def __init__(self, id_note: _Optional[int] = ..., str_text: _Optional[str] = ..., str_md_text: _Optional[str] = ..., str_date: _Optional[str] = ..., bool_completed: bool = ...) -> None: ...

class DeleteNoteRequest(_message.Message):
    __slots__ = ("id_note",)
    ID_NOTE_FIELD_NUMBER: _ClassVar[int]
    id_note: int
    def __init__(self, id_note: _Optional[int] = ...) -> None: ...

class NoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: Note
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ...) -> None: ...

class DeleteNoteResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class AllNotesResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: _containers.RepeatedCompositeFieldContainer[Note]
    def __init__(self, note: _Optional[_Iterable[_Union[Note, _Mapping]]] = ...) -> None: ...

class IdResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DayRequest(_message.Message):
    __slots__ = ("day",)
    DAY_FIELD_NUMBER: _ClassVar[int]
    day: str
    def __init__(self, day: _Optional[str] = ...) -> None: ...
