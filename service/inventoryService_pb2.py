# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import inventoryItem_pb2 as inventoryItem__pb2
import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16inventoryService.proto\x1a\x13inventoryItem.proto\x1a\nbook.proto\"/\n\x11\x42ookSearchRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"^\n\x12\x42ookSearchResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x61uthor_name\x18\x02 \x01(\t\x12%\n\x06status\x18\x03 \x01(\x0e\x32\x15.InventoryItem.Status\"(\n\x11\x42ookCreateRequest\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"%\n\x12\x42ookCreateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x81\x01\n\x10InventoryService\x12\x37\n\nCreateBook\x12\x12.BookCreateRequest\x1a\x13.BookCreateResponse\"\x00\x12\x34\n\x07GetBook\x12\x12.BookSearchRequest\x1a\x13.BookSearchResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKSEARCHREQUEST._serialized_start=59
  _BOOKSEARCHREQUEST._serialized_end=106
  _BOOKSEARCHRESPONSE._serialized_start=108
  _BOOKSEARCHRESPONSE._serialized_end=202
  _BOOKCREATEREQUEST._serialized_start=204
  _BOOKCREATEREQUEST._serialized_end=244
  _BOOKCREATERESPONSE._serialized_start=246
  _BOOKCREATERESPONSE._serialized_end=283
  _INVENTORYSERVICE._serialized_start=286
  _INVENTORYSERVICE._serialized_end=415
# @@protoc_insertion_point(module_scope)
