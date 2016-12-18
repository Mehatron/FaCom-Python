#!/usr/bin/env python

DATA_BITS_5         = 5
DATA_BITS_6         = 6
DATA_BITS_7         = 7
DATA_BITS_8         = 8

PARITY_OFF          = 0
PARITY_EVEN         = 1
PARITY_ODD          = 2

STOP_BITS_1         = 1
STOP_BITS_2         = 2

BAUD_0              = 0
BAUD_9600           = 9600
BAUD_19200          = 19200

STX                 = 0x02
ETX                 = 0x03

# Discrete types
DISCRETE_X          = 1         # Input discrete
DISCRETE_Y          = 2         # Output discrete
DISCRETE_M          = 3         # Internal memory discrete
DISCRETE_S          = 4         # Step discrete
DISCRETE_T          = 5         # Timer discrete
DISCRETE_C          = 6         # Counter discrete

# Discrete actions
ACTION_DISABLE      = 1
ACTION_ENABLE       = 2
ACTION_SET          = 3
ACTION_RESET        = 4

# PLC on/off actions
ACTION_OFF          = 0
ACTION_ON           = 1

