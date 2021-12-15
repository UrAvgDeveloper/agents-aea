# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="register.proto",
    package="aea.fetchai.register.v1_1_0",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x0eregister.proto\x12\x1b\x61\x65\x61.fetchai.register.v1_1_0"\xa9\x06\n\x0fRegisterMessage\x12P\n\x05\x65rror\x18\x05 \x01(\x0b\x32?.aea.fetchai.register.v1_1_0.RegisterMessage.Error_PerformativeH\x00\x12V\n\x08register\x18\x06 \x01(\x0b\x32\x42.aea.fetchai.register.v1_1_0.RegisterMessage.Register_PerformativeH\x00\x12T\n\x07success\x18\x07 \x01(\x0b\x32\x41.aea.fetchai.register.v1_1_0.RegisterMessage.Success_PerformativeH\x00\x1a\xa0\x01\n\x15Register_Performative\x12Z\n\x04info\x18\x01 \x03(\x0b\x32L.aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x9e\x01\n\x14Success_Performative\x12Y\n\x04info\x18\x01 \x03(\x0b\x32K.aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xc1\x01\n\x12\x45rror_Performative\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12W\n\x04info\x18\x03 \x03(\x0b\x32I.aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0cperformativeb\x06proto3',
)


_REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=441,
    serialized_end=484,
)

_REGISTERMESSAGE_REGISTER_PERFORMATIVE = _descriptor.Descriptor(
    name="Register_Performative",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=324,
    serialized_end=484,
)

_REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=441,
    serialized_end=484,
)

_REGISTERMESSAGE_SUCCESS_PERFORMATIVE = _descriptor.Descriptor(
    name="Success_Performative",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=487,
    serialized_end=645,
)

_REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=441,
    serialized_end=484,
)

_REGISTERMESSAGE_ERROR_PERFORMATIVE = _descriptor.Descriptor(
    name="Error_Performative",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.error_code",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="error_msg",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.error_msg",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="info",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.info",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=648,
    serialized_end=841,
)

_REGISTERMESSAGE = _descriptor.Descriptor(
    name="RegisterMessage",
    full_name="aea.fetchai.register.v1_1_0.RegisterMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.error",
            index=0,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="register",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.register",
            index=1,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.success",
            index=2,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _REGISTERMESSAGE_REGISTER_PERFORMATIVE,
        _REGISTERMESSAGE_SUCCESS_PERFORMATIVE,
        _REGISTERMESSAGE_ERROR_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.fetchai.register.v1_1_0.RegisterMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=48,
    serialized_end=857,
)

_REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY.containing_type = (
    _REGISTERMESSAGE_REGISTER_PERFORMATIVE
)
_REGISTERMESSAGE_REGISTER_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY
_REGISTERMESSAGE_REGISTER_PERFORMATIVE.containing_type = _REGISTERMESSAGE
_REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY.containing_type = (
    _REGISTERMESSAGE_SUCCESS_PERFORMATIVE
)
_REGISTERMESSAGE_SUCCESS_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY
_REGISTERMESSAGE_SUCCESS_PERFORMATIVE.containing_type = _REGISTERMESSAGE
_REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY.containing_type = (
    _REGISTERMESSAGE_ERROR_PERFORMATIVE
)
_REGISTERMESSAGE_ERROR_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY
_REGISTERMESSAGE_ERROR_PERFORMATIVE.containing_type = _REGISTERMESSAGE
_REGISTERMESSAGE.fields_by_name[
    "error"
].message_type = _REGISTERMESSAGE_ERROR_PERFORMATIVE
_REGISTERMESSAGE.fields_by_name[
    "register"
].message_type = _REGISTERMESSAGE_REGISTER_PERFORMATIVE
_REGISTERMESSAGE.fields_by_name[
    "success"
].message_type = _REGISTERMESSAGE_SUCCESS_PERFORMATIVE
_REGISTERMESSAGE.oneofs_by_name["performative"].fields.append(
    _REGISTERMESSAGE.fields_by_name["error"]
)
_REGISTERMESSAGE.fields_by_name[
    "error"
].containing_oneof = _REGISTERMESSAGE.oneofs_by_name["performative"]
_REGISTERMESSAGE.oneofs_by_name["performative"].fields.append(
    _REGISTERMESSAGE.fields_by_name["register"]
)
_REGISTERMESSAGE.fields_by_name[
    "register"
].containing_oneof = _REGISTERMESSAGE.oneofs_by_name["performative"]
_REGISTERMESSAGE.oneofs_by_name["performative"].fields.append(
    _REGISTERMESSAGE.fields_by_name["success"]
)
_REGISTERMESSAGE.fields_by_name[
    "success"
].containing_oneof = _REGISTERMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["RegisterMessage"] = _REGISTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterMessage = _reflection.GeneratedProtocolMessageType(
    "RegisterMessage",
    (_message.Message,),
    {
        "Register_Performative": _reflection.GeneratedProtocolMessageType(
            "Register_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY,
                        "__module__": "register_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _REGISTERMESSAGE_REGISTER_PERFORMATIVE,
                "__module__": "register_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Register_Performative)
            },
        ),
        "Success_Performative": _reflection.GeneratedProtocolMessageType(
            "Success_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY,
                        "__module__": "register_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _REGISTERMESSAGE_SUCCESS_PERFORMATIVE,
                "__module__": "register_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Success_Performative)
            },
        ),
        "Error_Performative": _reflection.GeneratedProtocolMessageType(
            "Error_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY,
                        "__module__": "register_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _REGISTERMESSAGE_ERROR_PERFORMATIVE,
                "__module__": "register_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage.Error_Performative)
            },
        ),
        "DESCRIPTOR": _REGISTERMESSAGE,
        "__module__": "register_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.register.v1_1_0.RegisterMessage)
    },
)
_sym_db.RegisterMessage(RegisterMessage)
_sym_db.RegisterMessage(RegisterMessage.Register_Performative)
_sym_db.RegisterMessage(RegisterMessage.Register_Performative.InfoEntry)
_sym_db.RegisterMessage(RegisterMessage.Success_Performative)
_sym_db.RegisterMessage(RegisterMessage.Success_Performative.InfoEntry)
_sym_db.RegisterMessage(RegisterMessage.Error_Performative)
_sym_db.RegisterMessage(RegisterMessage.Error_Performative.InfoEntry)


_REGISTERMESSAGE_REGISTER_PERFORMATIVE_INFOENTRY._options = None
_REGISTERMESSAGE_SUCCESS_PERFORMATIVE_INFOENTRY._options = None
_REGISTERMESSAGE_ERROR_PERFORMATIVE_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)
