# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"\xa8\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x61uthor_name\x18\x03 \x01(\t\x12\x1a\n\x05genre\x18\x04 \x01(\x0e\x32\x0b.Book.Genre\x12\x14\n\x0cpublish_year\x18\x05 \x01(\x05\"<\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\n\n\x06POETRY\x10\x01\x12\x0b\n\x07HISTORY\x10\x02\x12\r\n\tBIOGRAPHY\x10\x03\"\x94\x01\n\rInventoryItem\x12\x18\n\x10inventory_number\x18\x01 \x01(\x03\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12%\n\x06status\x18\x03 \x01(\x0e\x32\x15.InventoryItem.Status\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x07\n\x05\x62ooks\"\"\n\x11\x42ookSearchRequest\x12\r\n\x05title\x18\x01 \x01(\t\")\n\x12\x42ookSearchResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"(\n\x11\x42ookCreateRequest\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"%\n\x12\x42ookCreateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x81\x01\n\x10InventoryService\x12\x37\n\nCreateBook\x12\x12.BookCreateRequest\x1a\x13.BookCreateResponse\"\x00\x12\x34\n\x07GetBook\x12\x12.BookSearchRequest\x1a\x13.BookSearchResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=20
  _BOOK._serialized_end=188
  _BOOK_GENRE._serialized_start=128
  _BOOK_GENRE._serialized_end=188
  _INVENTORYITEM._serialized_start=191
  _INVENTORYITEM._serialized_end=339
  _INVENTORYITEM_STATUS._serialized_start=296
  _INVENTORYITEM_STATUS._serialized_end=330
  _BOOKSEARCHREQUEST._serialized_start=341
  _BOOKSEARCHREQUEST._serialized_end=375
  _BOOKSEARCHRESPONSE._serialized_start=377
  _BOOKSEARCHRESPONSE._serialized_end=418
  _BOOKCREATEREQUEST._serialized_start=420
  _BOOKCREATEREQUEST._serialized_end=460
  _BOOKCREATERESPONSE._serialized_start=462
  _BOOKCREATERESPONSE._serialized_end=499
  _INVENTORYSERVICE._serialized_start=502
  _INVENTORYSERVICE._serialized_end=631
# @@protoc_insertion_point(module_scope)
