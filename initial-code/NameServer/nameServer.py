import sys
sys.path.insert(1, '../Contract/target/generated-sources/protobuf/python')
immport grpc
import NameServer_pb2 as pb2
import NameServer_pb2_grpc as pb2_grpc
from NameServerService import NameServer
from concurrent import futures
# define the port
PORT = 5001

if __name__ == '__main__':
    try:
        # print received arguments
        print("Received arguments:")
        for i in range(1, len(sys.argv)):
            print("  " + sys.argv[i])

        # create server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        # add service
        pb2_grpc.add_NameServerServiceServicer_to_server(NameServer(), server)
        # listen on port 5001
        server.add_insecure_port('[::]:5001')
        # start server
        server.start()
        # print message
        print("Server listening on port 5001")
        # wait for server to finish
        server.wait_for_termination()

    except KeyboardInterrupt:
        print("HelloServer stopped")
        exit(0)
