# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UA.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UA.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x08UA.proto\":\n\x08\x41Product\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x12\r\n\x05\x63ount\x18\x03 \x02(\x05\"A\n\x05\x41Pack\x12\r\n\x05whnum\x18\x01 \x02(\x05\x12\x19\n\x06things\x18\x02 \x03(\x0b\x32\t.AProduct\x12\x0e\n\x06shipid\x18\x03 \x02(\x03\"R\n\rUAShipRequest\x12\x17\n\x07package\x18\x01 \x02(\x0b\x32\x06.APack\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x12\n\nupsAccount\x18\x04 \x01(\t\"?\n\rUATrackArrive\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\r\n\x05whnum\x18\x02 \x02(\x05\x12\x0e\n\x06shipid\x18\x03 \x02(\x03\"c\n\x0e\x41mazonCommands\x12 \n\x08req_ship\x18\x01 \x01(\x0b\x32\x0e.UAShipRequest\x12\x1b\n\x13req_deliver_truckid\x18\x02 \x01(\x05\x12\x12\n\ndisconnect\x18\x03 \x01(\x08\"2\n\x0cUPSResponses\x12\"\n\nresp_truck\x18\x01 \x01(\x0b\x32\x0e.UATrackArrive')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_APRODUCT = _descriptor.Descriptor(
  name='AProduct',
  full_name='AProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AProduct.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='AProduct.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='AProduct.count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=70,
)


_APACK = _descriptor.Descriptor(
  name='APack',
  full_name='APack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='whnum', full_name='APack.whnum', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='things', full_name='APack.things', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipid', full_name='APack.shipid', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=137,
)


_UASHIPREQUEST = _descriptor.Descriptor(
  name='UAShipRequest',
  full_name='UAShipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package', full_name='UAShipRequest.package', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='UAShipRequest.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='UAShipRequest.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upsAccount', full_name='UAShipRequest.upsAccount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=221,
)


_UATRACKARRIVE = _descriptor.Descriptor(
  name='UATrackArrive',
  full_name='UATrackArrive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UATrackArrive.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='whnum', full_name='UATrackArrive.whnum', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipid', full_name='UATrackArrive.shipid', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=286,
)


_AMAZONCOMMANDS = _descriptor.Descriptor(
  name='AmazonCommands',
  full_name='AmazonCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req_ship', full_name='AmazonCommands.req_ship', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req_deliver_truckid', full_name='AmazonCommands.req_deliver_truckid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='AmazonCommands.disconnect', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=387,
)


_UPSRESPONSES = _descriptor.Descriptor(
  name='UPSResponses',
  full_name='UPSResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp_truck', full_name='UPSResponses.resp_truck', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=439,
)

_APACK.fields_by_name['things'].message_type = _APRODUCT
_UASHIPREQUEST.fields_by_name['package'].message_type = _APACK
_AMAZONCOMMANDS.fields_by_name['req_ship'].message_type = _UASHIPREQUEST
_UPSRESPONSES.fields_by_name['resp_truck'].message_type = _UATRACKARRIVE
DESCRIPTOR.message_types_by_name['AProduct'] = _APRODUCT
DESCRIPTOR.message_types_by_name['APack'] = _APACK
DESCRIPTOR.message_types_by_name['UAShipRequest'] = _UASHIPREQUEST
DESCRIPTOR.message_types_by_name['UATrackArrive'] = _UATRACKARRIVE
DESCRIPTOR.message_types_by_name['AmazonCommands'] = _AMAZONCOMMANDS
DESCRIPTOR.message_types_by_name['UPSResponses'] = _UPSRESPONSES

AProduct = _reflection.GeneratedProtocolMessageType('AProduct', (_message.Message,), dict(
  DESCRIPTOR = _APRODUCT,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:AProduct)
  ))
_sym_db.RegisterMessage(AProduct)

APack = _reflection.GeneratedProtocolMessageType('APack', (_message.Message,), dict(
  DESCRIPTOR = _APACK,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:APack)
  ))
_sym_db.RegisterMessage(APack)

UAShipRequest = _reflection.GeneratedProtocolMessageType('UAShipRequest', (_message.Message,), dict(
  DESCRIPTOR = _UASHIPREQUEST,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UAShipRequest)
  ))
_sym_db.RegisterMessage(UAShipRequest)

UATrackArrive = _reflection.GeneratedProtocolMessageType('UATrackArrive', (_message.Message,), dict(
  DESCRIPTOR = _UATRACKARRIVE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UATrackArrive)
  ))
_sym_db.RegisterMessage(UATrackArrive)

AmazonCommands = _reflection.GeneratedProtocolMessageType('AmazonCommands', (_message.Message,), dict(
  DESCRIPTOR = _AMAZONCOMMANDS,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:AmazonCommands)
  ))
_sym_db.RegisterMessage(AmazonCommands)

UPSResponses = _reflection.GeneratedProtocolMessageType('UPSResponses', (_message.Message,), dict(
  DESCRIPTOR = _UPSRESPONSES,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPSResponses)
  ))
_sym_db.RegisterMessage(UPSResponses)


# @@protoc_insertion_point(module_scope)
