/*
 * This is the low level driver for the ttun interface. 
 * It hooks up a TCP socket to the mesh interface.
 * 
 * Copyright (C) 2016 GINI Cloud
 */

#ifndef TTUN_H
#define	TTUN_H

#include "vpl.h"
#include "grouter.h"

void *toTtunDev(void *arg);
void* fromTtunDev(void *arg);
vpl_data_t *ttun_connect(short int src_port, uchar* src_IP,
                        short int dst_port, uchar* dst_IP, short int is_server);


#endif	/* TUN_H */