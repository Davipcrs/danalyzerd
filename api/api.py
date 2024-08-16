import grpc
from concurrent import futures
import time
from database.sql.insert import insert_into_note
from database.sql.delete import delete_note
from database.sql.select import select_one_note, select_all_notes
from api.proto import note_pb2_grpc, note_pb2


class NoteServices(note_pb2_grpc.NoteServiceServicer):
    def CreateNote(self, request, context):
        """Creates a new note
        """
        id = insert_into_note(request.str_text, request.str_md_text,
                              request.str_date, request.bool_complete)
        return note_pb2.IdResponse(id)

    def GetNote(self, request, context):
        """Retrieves a note by ID
        """
        data = select_one_note(request.id_note)
        note = note_pb2.Note(id_note=data[0], str_text=data[1],
                             str_md_text=data[2], str_date=data[3], bool_completed=data[4])
        response = note_pb2.NoteResponse(note)
        return response

    def GetAllNotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        return

    def UpdateNote(self, request, context):
        """Updates a note
        """
        return

    def DeleteNote(self, request, context):
        """Deletes a note
        """
        delete_note(request.id_note)
        return note_pb2.DeleteNoteResponse(True)
