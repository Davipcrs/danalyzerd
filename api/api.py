import grpc
from concurrent import futures
import time
from database.sql.update import update_note
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
        """Retrieves All Notes"""
        all_notes = select_all_notes()

        message = note_pb2.AllNotesResponse()
        for data in all_notes:
            aux = note_pb2.Note(id_note=data[0], str_text=data[1],
                                str_md_text=data[2], str_date=data[3], bool_completed=data[4])
            message.note.append(aux)
        return message

    def GetNoteByDay(self, request, context):
        return super().GetNoteByDay(request, context)

    def UpdateBool(self, request, context):
        return super().UpdateBool(request, context)

    def UpdateNote(self, request, context):
        """Updates a note
        """
        update_note(request.id_note, request.str_text,
                    request.str_md_text, request.str_date, request.bool_complete)
        return note_pb2.IdResponse(request.id_note)

    def DeleteNote(self, request, context):
        """Deletes a note
        """
        delete_note(request.id_note)
        return note_pb2.DeleteNoteResponse(True)
