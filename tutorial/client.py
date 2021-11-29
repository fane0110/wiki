import grpc
from account_proto import account_pb2
from account_proto import account_pb2_grpc


with grpc.insecure_channel('localhost:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)
    response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=1))
    print(response, end='')