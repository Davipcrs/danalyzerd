''''''
# Feito por Davi Coelho 28/09/2024
#
# Arquivo contém as funções chamadas pelo serviço de gRPC, ler os comentários de cada função
# Para documentação.
#
''''''




from concurrent import futures
from datetime import datetime
import grpc
import time
from database.sql.update import update_note, update_note_bool
from database.sql.insert import insert_into_note
from database.sql.delete import delete_note
from database.sql.select import select_one_note, select_all_notes, select_notes_by_day
from api.proto import note_pb2_grpc, note_pb2
class NoteServices(note_pb2_grpc.NoteServiceServicer):
    def CreateNote(self, request, context):
        """Creates a new note
        """
        id = insert_into_note(request.str_text, request.str_md_text,
                              request.str_date.split('T')[0], request.str_date.split('T')[1], request.bool_completed)

        return note_pb2.IdResponse(id)

    def GetNote(self, request, context):
        """Retrieves a note by ID
        """
        data = select_one_note(request.id_note)
        date_auxiliar = data[3] + 'T' + data[4]
        date_obj = datetime.fromisoformat(date_auxiliar)
        response = note_pb2.Note(id_note=data[0], str_text=data[1],
                                 str_md_text=data[2], str_date=date_obj.isoformat(), bool_completed=data[5])
        return response

    def GetAllNotes(self, request, context):
        """Retrieves All Notes"""
        all_notes = select_all_notes()

        message = note_pb2.AllNotesResponse()
        for data in all_notes:
            date_auxiliar = data[3] + 'T' + data[4]
            date_obj = datetime.fromisoformat(date_auxiliar)
            aux = note_pb2.Note(id_note=data[0], str_text=data[1],
                                str_md_text=data[2], str_date=date_obj.isoformat(), bool_completed=data[5])
            message.note.append(aux)
        # print('request')
        return message

    def GetNoteByDay(self, request, context):
        '''Get All Notes in One Day'''
        day_notes = select_notes_by_day(request.day)

        message = note_pb2.AllNotesResponse()
        for data in day_notes:
            date_auxiliar = data[3] + 'T' + data[4]
            date_obj = datetime.fromisoformat(date_auxiliar)
            aux = note_pb2.Note(id_note=data[0], str_text=data[1],
                                str_md_text=data[2], str_date=date_obj.isoformat(), bool_completed=data[5])
            message.note.append(aux)
        return message

    def UpdateBool(self, request, context):
        '''Updates if a note is active or no'''
        update_note_bool(request.id_note, request.bool_completed)
        return note_pb2.empty()

    def UpdateNote(self, request, context):
        """Updates a note
        """
        auxilar_date = str(request.str_date).split('T')
        update_note(request.id_note, request.str_text,
                    request.str_md_text, auxilar_date[0], auxilar_date[1], request.bool_completed)
        return note_pb2.IdResponse(request.id_note)

    def DeleteNote(self, request, context):
        """Deletes a note
        """
        delete_note(request.id_note)
        return note_pb2.DeleteNoteResponse(True)
