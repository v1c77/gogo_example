# -*- coding: utf-8 -*-

from gogo import GogoApplication, dispatcher_with_meta
from example.hello_bro_pb2_grpc import BroServicer
from example.hello_bro_pb2 import HelloReply

app = GogoApplication()


# behavior
def handler_hello():

    user = 'gogo_user'
    msg = 'Hello, {}'.format(user)
    by = 'gogo_server'
    return HelloReply(
        message=msg,
        by=by)


# TODO(vici) I need a meta with hello_bro_pb2_grpc

@app.dispatcher
class Dispatcher(dispatcher_with_meta(BroServicer)):

    """the DispatcherMixin will handle error."""

    def SayHello(self, request, context):
        # a dispatcher method can only connect the handler to grpc service
        # method.
        return handler_hello()


"""
    to run the application. use global shell `vos serve.
"""
