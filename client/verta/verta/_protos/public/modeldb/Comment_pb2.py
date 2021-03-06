# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modeldb/Comment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modeldb/Comment.proto',
  package='ai.verta.modeldb',
  syntax='proto3',
  serialized_options=b'P\001Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb',
  serialized_pb=b'\n\x15modeldb/Comment.proto\x12\x10\x61i.verta.modeldb\x1a\x1cgoogle/api/annotations.proto\x1a\x14uac/UACService.proto\"p\n\rEntityComment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x13\n\x0b\x65ntity_name\x18\x03 \x01(\t\x12+\n\x08\x63omments\x18\x04 \x03(\x0b\x32\x19.ai.verta.modeldb.Comment\"\x8b\x01\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x07user_id\x18\x02 \x01(\tB\x02\x18\x01\x12\x11\n\tdate_time\x18\x03 \x01(\x04\x12\x0f\n\x07message\x18\x04 \x01(\t\x12)\n\tuser_info\x18\x05 \x01(\x0b\x32\x16.ai.verta.uac.UserInfo\x12\x10\n\x08verta_id\x18\x06 \x01(\t\"{\n\nAddComment\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\x04\x12\x0f\n\x07message\x18\x03 \x01(\t\x1a\x36\n\x08Response\x12*\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x19.ai.verta.modeldb.Comment\"\x8a\x01\n\rUpdateComment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x11\n\tdate_time\x18\x03 \x01(\x04\x12\x0f\n\x07message\x18\x04 \x01(\t\x1a\x36\n\x08Response\x12*\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x19.ai.verta.modeldb.Comment\"J\n\rDeleteComment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"Y\n\x0bGetComments\x12\x11\n\tentity_id\x18\x01 \x01(\t\x1a\x37\n\x08Response\x12+\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x19.ai.verta.modeldb.Comment2\xea\x04\n\x0e\x43ommentService\x12\x8e\x01\n\x17\x61\x64\x64\x45xperimentRunComment\x12\x1c.ai.verta.modeldb.AddComment\x1a%.ai.verta.modeldb.AddComment.Response\".\x82\xd3\xe4\x93\x02(\"#/v1/comment/addExperimentRunComment:\x01*\x12\x9a\x01\n\x1aupdateExperimentRunComment\x12\x1f.ai.verta.modeldb.UpdateComment\x1a(.ai.verta.modeldb.UpdateComment.Response\"1\x82\xd3\xe4\x93\x02+\"&/v1/comment/updateExperimentRunComment:\x01*\x12\x8f\x01\n\x18getExperimentRunComments\x12\x1d.ai.verta.modeldb.GetComments\x1a&.ai.verta.modeldb.GetComments.Response\",\x82\xd3\xe4\x93\x02&\x12$/v1/comment/getExperimentRunComments\x12\x97\x01\n\x1a\x64\x65leteExperimentRunComment\x12\x1f.ai.verta.modeldb.DeleteComment\x1a(.ai.verta.modeldb.DeleteComment.Response\".\x82\xd3\xe4\x93\x02(*&/v1/comment/deleteExperimentRunCommentBBP\x01Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldbb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,uac_dot_UACService__pb2.DESCRIPTOR,])




_ENTITYCOMMENT = _descriptor.Descriptor(
  name='EntityComment',
  full_name='ai.verta.modeldb.EntityComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.EntityComment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='ai.verta.modeldb.EntityComment.entity_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_name', full_name='ai.verta.modeldb.EntityComment.entity_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='ai.verta.modeldb.EntityComment.comments', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=207,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='ai.verta.modeldb.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.Comment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.modeldb.Comment.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='ai.verta.modeldb.Comment.date_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ai.verta.modeldb.Comment.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_info', full_name='ai.verta.modeldb.Comment.user_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verta_id', full_name='ai.verta.modeldb.Comment.verta_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=349,
)


_ADDCOMMENT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.AddComment.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment', full_name='ai.verta.modeldb.AddComment.Response.comment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=474,
)

_ADDCOMMENT = _descriptor.Descriptor(
  name='AddComment',
  full_name='ai.verta.modeldb.AddComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='ai.verta.modeldb.AddComment.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='ai.verta.modeldb.AddComment.date_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ai.verta.modeldb.AddComment.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADDCOMMENT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=474,
)


_UPDATECOMMENT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.UpdateComment.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment', full_name='ai.verta.modeldb.UpdateComment.Response.comment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=474,
)

_UPDATECOMMENT = _descriptor.Descriptor(
  name='UpdateComment',
  full_name='ai.verta.modeldb.UpdateComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.UpdateComment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='ai.verta.modeldb.UpdateComment.entity_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='ai.verta.modeldb.UpdateComment.date_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ai.verta.modeldb.UpdateComment.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATECOMMENT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=615,
)


_DELETECOMMENT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.DeleteComment.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.modeldb.DeleteComment.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=691,
)

_DELETECOMMENT = _descriptor.Descriptor(
  name='DeleteComment',
  full_name='ai.verta.modeldb.DeleteComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.DeleteComment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='ai.verta.modeldb.DeleteComment.entity_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETECOMMENT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=691,
)


_GETCOMMENTS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.GetComments.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comments', full_name='ai.verta.modeldb.GetComments.Response.comments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=727,
  serialized_end=782,
)

_GETCOMMENTS = _descriptor.Descriptor(
  name='GetComments',
  full_name='ai.verta.modeldb.GetComments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='ai.verta.modeldb.GetComments.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETCOMMENTS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=782,
)

_ENTITYCOMMENT.fields_by_name['comments'].message_type = _COMMENT
_COMMENT.fields_by_name['user_info'].message_type = uac_dot_UACService__pb2._USERINFO
_ADDCOMMENT_RESPONSE.fields_by_name['comment'].message_type = _COMMENT
_ADDCOMMENT_RESPONSE.containing_type = _ADDCOMMENT
_UPDATECOMMENT_RESPONSE.fields_by_name['comment'].message_type = _COMMENT
_UPDATECOMMENT_RESPONSE.containing_type = _UPDATECOMMENT
_DELETECOMMENT_RESPONSE.containing_type = _DELETECOMMENT
_GETCOMMENTS_RESPONSE.fields_by_name['comments'].message_type = _COMMENT
_GETCOMMENTS_RESPONSE.containing_type = _GETCOMMENTS
DESCRIPTOR.message_types_by_name['EntityComment'] = _ENTITYCOMMENT
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['AddComment'] = _ADDCOMMENT
DESCRIPTOR.message_types_by_name['UpdateComment'] = _UPDATECOMMENT
DESCRIPTOR.message_types_by_name['DeleteComment'] = _DELETECOMMENT
DESCRIPTOR.message_types_by_name['GetComments'] = _GETCOMMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntityComment = _reflection.GeneratedProtocolMessageType('EntityComment', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYCOMMENT,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.EntityComment)
  })
_sym_db.RegisterMessage(EntityComment)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), {
  'DESCRIPTOR' : _COMMENT,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.Comment)
  })
_sym_db.RegisterMessage(Comment)

AddComment = _reflection.GeneratedProtocolMessageType('AddComment', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _ADDCOMMENT_RESPONSE,
    '__module__' : 'modeldb.Comment_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.AddComment.Response)
    })
  ,
  'DESCRIPTOR' : _ADDCOMMENT,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.AddComment)
  })
_sym_db.RegisterMessage(AddComment)
_sym_db.RegisterMessage(AddComment.Response)

UpdateComment = _reflection.GeneratedProtocolMessageType('UpdateComment', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOMMENT_RESPONSE,
    '__module__' : 'modeldb.Comment_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.UpdateComment.Response)
    })
  ,
  'DESCRIPTOR' : _UPDATECOMMENT,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.UpdateComment)
  })
_sym_db.RegisterMessage(UpdateComment)
_sym_db.RegisterMessage(UpdateComment.Response)

DeleteComment = _reflection.GeneratedProtocolMessageType('DeleteComment', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _DELETECOMMENT_RESPONSE,
    '__module__' : 'modeldb.Comment_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteComment.Response)
    })
  ,
  'DESCRIPTOR' : _DELETECOMMENT,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteComment)
  })
_sym_db.RegisterMessage(DeleteComment)
_sym_db.RegisterMessage(DeleteComment.Response)

GetComments = _reflection.GeneratedProtocolMessageType('GetComments', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETCOMMENTS_RESPONSE,
    '__module__' : 'modeldb.Comment_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.GetComments.Response)
    })
  ,
  'DESCRIPTOR' : _GETCOMMENTS,
  '__module__' : 'modeldb.Comment_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.GetComments)
  })
_sym_db.RegisterMessage(GetComments)
_sym_db.RegisterMessage(GetComments.Response)


DESCRIPTOR._options = None
_COMMENT.fields_by_name['user_id']._options = None

_COMMENTSERVICE = _descriptor.ServiceDescriptor(
  name='CommentService',
  full_name='ai.verta.modeldb.CommentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=785,
  serialized_end=1403,
  methods=[
  _descriptor.MethodDescriptor(
    name='addExperimentRunComment',
    full_name='ai.verta.modeldb.CommentService.addExperimentRunComment',
    index=0,
    containing_service=None,
    input_type=_ADDCOMMENT,
    output_type=_ADDCOMMENT_RESPONSE,
    serialized_options=b'\202\323\344\223\002(\"#/v1/comment/addExperimentRunComment:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='updateExperimentRunComment',
    full_name='ai.verta.modeldb.CommentService.updateExperimentRunComment',
    index=1,
    containing_service=None,
    input_type=_UPDATECOMMENT,
    output_type=_UPDATECOMMENT_RESPONSE,
    serialized_options=b'\202\323\344\223\002+\"&/v1/comment/updateExperimentRunComment:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='getExperimentRunComments',
    full_name='ai.verta.modeldb.CommentService.getExperimentRunComments',
    index=2,
    containing_service=None,
    input_type=_GETCOMMENTS,
    output_type=_GETCOMMENTS_RESPONSE,
    serialized_options=b'\202\323\344\223\002&\022$/v1/comment/getExperimentRunComments',
  ),
  _descriptor.MethodDescriptor(
    name='deleteExperimentRunComment',
    full_name='ai.verta.modeldb.CommentService.deleteExperimentRunComment',
    index=3,
    containing_service=None,
    input_type=_DELETECOMMENT,
    output_type=_DELETECOMMENT_RESPONSE,
    serialized_options=b'\202\323\344\223\002(*&/v1/comment/deleteExperimentRunComment',
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMENTSERVICE)

DESCRIPTOR.services_by_name['CommentService'] = _COMMENTSERVICE

# @@protoc_insertion_point(module_scope)
