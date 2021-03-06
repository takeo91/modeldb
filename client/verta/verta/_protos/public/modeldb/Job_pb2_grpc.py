# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..modeldb import Job_pb2 as modeldb_dot_Job__pb2


class JobServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createJob = channel.unary_unary(
        '/ai.verta.modeldb.JobService/createJob',
        request_serializer=modeldb_dot_Job__pb2.CreateJob.SerializeToString,
        response_deserializer=modeldb_dot_Job__pb2.CreateJob.Response.FromString,
        )
    self.getJob = channel.unary_unary(
        '/ai.verta.modeldb.JobService/getJob',
        request_serializer=modeldb_dot_Job__pb2.GetJob.SerializeToString,
        response_deserializer=modeldb_dot_Job__pb2.GetJob.Response.FromString,
        )
    self.updateJob = channel.unary_unary(
        '/ai.verta.modeldb.JobService/updateJob',
        request_serializer=modeldb_dot_Job__pb2.UpdateJob.SerializeToString,
        response_deserializer=modeldb_dot_Job__pb2.UpdateJob.Response.FromString,
        )
    self.deleteJob = channel.unary_unary(
        '/ai.verta.modeldb.JobService/deleteJob',
        request_serializer=modeldb_dot_Job__pb2.DeleteJob.SerializeToString,
        response_deserializer=modeldb_dot_Job__pb2.DeleteJob.Response.FromString,
        )


class JobServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def createJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createJob': grpc.unary_unary_rpc_method_handler(
          servicer.createJob,
          request_deserializer=modeldb_dot_Job__pb2.CreateJob.FromString,
          response_serializer=modeldb_dot_Job__pb2.CreateJob.Response.SerializeToString,
      ),
      'getJob': grpc.unary_unary_rpc_method_handler(
          servicer.getJob,
          request_deserializer=modeldb_dot_Job__pb2.GetJob.FromString,
          response_serializer=modeldb_dot_Job__pb2.GetJob.Response.SerializeToString,
      ),
      'updateJob': grpc.unary_unary_rpc_method_handler(
          servicer.updateJob,
          request_deserializer=modeldb_dot_Job__pb2.UpdateJob.FromString,
          response_serializer=modeldb_dot_Job__pb2.UpdateJob.Response.SerializeToString,
      ),
      'deleteJob': grpc.unary_unary_rpc_method_handler(
          servicer.deleteJob,
          request_deserializer=modeldb_dot_Job__pb2.DeleteJob.FromString,
          response_serializer=modeldb_dot_Job__pb2.DeleteJob.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.modeldb.JobService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
