/******************************************************************************
 * Copyright 2015-2016 Espressif Systems
 *
 * FileName: mesh_json.c
 *
 * Description: mesh demo for JSON protocol parser
 *
 * Modification history:
 *     2016/03/15, v1.1 create this file.
*******************************************************************************/
#include "mesh_parser.h"

void mesh_json_proto_parser(void *arg, uint8_t *pdata, uint16_t len)
{
    MESH_PARSER_PRINT("%s\n", __func__);
    MESH_PARSER_PRINT("len:%u, data:%s\n", len, pdata);
}
