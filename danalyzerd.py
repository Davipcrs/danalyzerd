''''''
# Feito por Davi Coelho 28/09/2024
#
# Main File do sistema, entrypoint.
#
''''''




from concurrent import futures
import modules.conf.create_conf  # This import execute some code!
import os
import grpc
from api.proto import note_pb2_grpc
from api.api import NoteServices
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    note_pb2_grpc.add_NoteServiceServicer_to_server(
        NoteServices(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
