#!/usr/bin/env python

import ctypes;
from .error import *;
from .const import *;

class Facom:
    'Class for communicate with Fatek PLC ussing facom C library'

    def __init__(self):
        'Construct object of type Facom, open library for communication'

        self.is_open = False
        try:
            self.facom = ctypes.CDLL('libfacom.so');
        except:
            assert False, 'Can\'t find "libfacom.so" (FaCom library)'

    def __del__(self):
        'Destructor of object of type Facom, close communication'

        self.close();

    def open(self, port, station_number = 0x01):
        'Open communication to Fatek PLC'

        c_port = ctypes.c_char_p(port);
        c_station_number = ctypes.c_uint8(station_number);

        error = self.facom.FACOM_open(c_port, c_station_number);
        if error < 0:
            self.is_open = False;
        else:
            self.is_open = True;
        return error;

    def close(self):
        'Close communication with Fatek PLC'

        if self.is_open:
            return self.facom.FACOM_close();
        return ERROR;

    def set_data_bits(self, data_bits):
        'Set number of data bits'

        c_data_bits = ctypes.c_int(data_bits);
        return self.facom.FACOM_setDataBits(c_data_bits);

    def set_parity(self, parity):
        'Set parity'

        c_data_bits = ctypes.c_int(parity);
        return self.facom.FACOM_setParity(c_parity);

    def set_stop_bits(self, stop_bits):
        'Set number of stop bits'

        c_stop_bits = ctypes.c_int(stop_bits);
        return self.facom.FACOM_setStopBits(c_stop_bitsy);

    def set_baud_rate(self, baud_rate):
        'Set baud rate (speed)'

        c_baud_rate = ctypes.c_int(baud_rate);
        return self.facom.FACOM_setBaudRate(c_baud_rate);

    def start(self):
        'Set PLC run mode to On'

        return self.facom.FACOM_start();

    def stop(self):
        'Set PLC run mode to Off'

        return self.facom.FACOM_stop();

    def set_discrete(self, discrete_type, discrete_number, action):
        'Set discrete'

        c_discrete_type = ctypes.c_uint8(discrete_type);
        c_discrete_number = ctypes.c_int(discrete_number);
        c_action = ctypes.c_uint8(action);
        return self.facom.FACOM_setDiscrete(c_discrete_type,
                                            c_discrete_number,
                                            c_action);

    def set_discretes(self, discrete_type,
                            discrete_number,
                            discrete_count,
                            data):
        'Set multiple continous discretes'

        count = discrete_count;
        if count == 0:
            count = 256;
        c_discrete_type = ctypes.c_uint8(discrete_type);
        c_discrete_number = ctypes.c_int(discrete_number);
        c_discrete_count = ctypes.c_uint8(discrete_count);
        return self.facom.FACOM_setDiscretes(c_discrete_type,
                                             c_discrete_number,
                                             c_discrete_count,
                                             data);

    def get_discretes(self, discrete_type,
                            discrete_number,
                            discrete_count,
                            data):
        'Get multiple continous discretes'

        count = discrete_count;
        if count == 0:
            count = 256;
        c_discrete_type = ctypes.c_uint8(discrete_type);
        c_discrete_number = ctypes.c_int(discrete_number);
        c_discrete_count = ctypes.c_uint8(discrete_count);
        c_data = (ctypes.c_int8 * count)();
        ctypes.cast(c_data, ctypes.POINTER(ctypes.c_int8));
        error = self.facom.FACOM_getDiscretes(c_discrete_type,
                                              c_discrete_number,
                                              c_discrete_count,
                                              c_data);
        if error == SUCCESS:
            for byte in c_data:
                data.append(byte);
        return error;

