# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prometheus.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10prometheus.proto\x12\x1d\x61\x65\x61.fetchai.prometheus.v1_0_0"\xdf\x06\n\x11PrometheusMessage\x12^\n\nadd_metric\x18\x05 \x01(\x0b\x32H.aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Add_Metric_PerformativeH\x00\x12Z\n\x08response\x18\x06 \x01(\x0b\x32\x46.aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Response_PerformativeH\x00\x12\x64\n\rupdate_metric\x18\x07 \x01(\x0b\x32K.aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Update_Metric_PerformativeH\x00\x1a\xe0\x01\n\x17\x41\x64\x64_Metric_Performative\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x64\n\x06labels\x18\x04 \x03(\x0b\x32T.aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Add_Metric_Performative.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xe4\x01\n\x1aUpdate_Metric_Performative\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61llable\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\x12g\n\x06labels\x18\x04 \x03(\x0b\x32W.aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Update_Metric_Performative.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aN\n\x15Response_Performative\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0emessage_is_set\x18\x03 \x01(\x08\x42\x0e\n\x0cperformativeb\x06proto3'
)


_PROMETHEUSMESSAGE = DESCRIPTOR.message_types_by_name["PrometheusMessage"]
_PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE = _PROMETHEUSMESSAGE.nested_types_by_name[
    "Add_Metric_Performative"
]
_PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY = _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE.nested_types_by_name[
    "LabelsEntry"
]
_PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE = _PROMETHEUSMESSAGE.nested_types_by_name[
    "Update_Metric_Performative"
]
_PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY = _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE.nested_types_by_name[
    "LabelsEntry"
]
_PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE = _PROMETHEUSMESSAGE.nested_types_by_name[
    "Response_Performative"
]
PrometheusMessage = _reflection.GeneratedProtocolMessageType(
    "PrometheusMessage",
    (_message.Message,),
    {
        "Add_Metric_Performative": _reflection.GeneratedProtocolMessageType(
            "Add_Metric_Performative",
            (_message.Message,),
            {
                "LabelsEntry": _reflection.GeneratedProtocolMessageType(
                    "LabelsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY,
                        "__module__": "prometheus_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Add_Metric_Performative.LabelsEntry)
                    },
                ),
                "DESCRIPTOR": _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Add_Metric_Performative)
            },
        ),
        "Update_Metric_Performative": _reflection.GeneratedProtocolMessageType(
            "Update_Metric_Performative",
            (_message.Message,),
            {
                "LabelsEntry": _reflection.GeneratedProtocolMessageType(
                    "LabelsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY,
                        "__module__": "prometheus_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Update_Metric_Performative.LabelsEntry)
                    },
                ),
                "DESCRIPTOR": _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Update_Metric_Performative)
            },
        ),
        "Response_Performative": _reflection.GeneratedProtocolMessageType(
            "Response_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage.Response_Performative)
            },
        ),
        "DESCRIPTOR": _PROMETHEUSMESSAGE,
        "__module__": "prometheus_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.v1_0_0.PrometheusMessage)
    },
)
_sym_db.RegisterMessage(PrometheusMessage)
_sym_db.RegisterMessage(PrometheusMessage.Add_Metric_Performative)
_sym_db.RegisterMessage(PrometheusMessage.Add_Metric_Performative.LabelsEntry)
_sym_db.RegisterMessage(PrometheusMessage.Update_Metric_Performative)
_sym_db.RegisterMessage(PrometheusMessage.Update_Metric_Performative.LabelsEntry)
_sym_db.RegisterMessage(PrometheusMessage.Response_Performative)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY._options = None
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY._serialized_options = (
        b"8\001"
    )
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY._options = None
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY._serialized_options = (
        b"8\001"
    )
    _PROMETHEUSMESSAGE._serialized_start = 52
    _PROMETHEUSMESSAGE._serialized_end = 915
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE._serialized_start = 364
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE._serialized_end = 588
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY._serialized_start = 543
    _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE_LABELSENTRY._serialized_end = 588
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE._serialized_start = 591
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE._serialized_end = 819
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY._serialized_start = 543
    _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE_LABELSENTRY._serialized_end = 588
    _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE._serialized_start = 821
    _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE._serialized_end = 899
# @@protoc_insertion_point(module_scope)
