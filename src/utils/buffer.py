#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from binascii import hexlify
import struct


class BytesBuffer(object):
    def __init__(self, capacity, littleEndian):
        self._data = bytearray(capacity)
        self._capacity = capacity
        self._index = 0
        if littleEndian:
            self._endian = '<'
        else:
            self._endian = '>'

    def writeByte(self, val):
        # self._data[self._index:self._index+1] = val.to_bytes(1, self._endian)
        self._data[self._index:self._index +
                               1] = struct.pack(self._endian + 'B', val)
        self._index = self._index + 1

    def writeInt(self, val):
        # self._data[self._index:self._index +
        #    4] = val.to_bytes(4, byteorder=self._endian)
        self._data[self._index:self._index +
                               4] = struct.pack(self._endian + 'I', val)
        self._index = self._index + 4

    def writeLong(self, val):
        # self._data[self._index:self._index +
        #    8] = val.to_bytes(8, byteorder=self._endian)
        self._data[self._index:self._index +
                               8] = struct.pack(self._endian + 'Q', val)
        self._index = self._index + 8

    def writeString(self, val):
        if not isinstance(val, bytes):
            val = val.encode(encoding='utf-8')
        self._data[self._index:self._index + len(val)] = val
        self._index = self._index + len(val)

    def tobytes(self):
        return self._data[:self._index]

    def tohex(self):
        return hexlify(self.tobytes())


def main():
    byteBuffer = BytesBuffer(1 + 4 + 32 + 32 + 8 + 8 + 64 + 64 + 0, True)
    byteBuffer.writeByte(10)
    byteBuffer.writeInt(1092)
    byteBuffer.writeLong(30)
    byteBuffer.writeString("hello world")
    print(byteBuffer.tohex())


if __name__ == "__main__":
    main()
