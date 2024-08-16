import grpc
from api.proto import note_pb2_grpc
from api.api import NoteServices
import grpc
from concurrent import futures


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    note_pb2_grpc.add_NoteServiceServicer_to_server(
        NoteServices(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == '__main__':
    serve()
