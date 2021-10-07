# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:58:54 2021

@author: subraman

Script to filter point cloud, mesure encode/decode time and point count 
"""
import os
import argparse
import csv
import pandas as pd
import time
import cwipc
import cwipc.codec
import _cwipc_codec
import cwipc.util
import open3d
parser = argparse.ArgumentParser(description="Read all point cloud frames from a target folder, apply a filter on the tile numbers and report encode/decode time and point count")
parser.add_argument(
        "--dir",
        default="C:/Users/subraman/Desktop/dev/clientSideTiling/DataAnalyses/NavigationData/NavDataSourceCleaned/",
        help="Directory with individual point cloud frames in separate files"
	)
parser.add_argument(
        "--tiles",
        help="List of tile numbers to use",
        nargs="+",
        type=int
	)
parser.add_argument(
        "--csv",
        default="codecstats.csv",
        help="Path to output csv file"
	)
parser.add_argument(
    "--octreedepths",
    nargs="+",
    type=int
    )
parser.add_argument(
    "--jpegQP",
    nargs="+",
    type=int
    )
args = parser.parse_args()
pcframes = os.listdir(args.dir)
columns = ["Filename","readtime","filesize","pointcount","encodetime","encodesize","decodetime","decodedpointcount"]
dataframes = pd.DataFrame(columns=columns)
for i in range (0, len(pcframes)):
    pcpath=os.path.join(args.dir,pcframes[i])
    filesize = os.path.getsize(pcpath)
    start_time = time.time()
    pc = cwipc.cwipc_read(pcpath,1234)
    end_time = time.time();
    readtime = (end_time - start_time) * 1000
    #xxxshishir we are missing the tile filtering part
    points=pc.get_points()
    pointcount = len(points)
    #Iterate through target octree depth and jpegqp values
    for j in range (0,len(args.octreedepths)):
        for k in range(0,len(args.jpegQP)):
            encoder = _cwipc_codec.cwipc_new_encoder(octree_bits=args.octreedepths[j],jpeg_quality=args.jpegQP[k])
            decoder = _cwipc_codec.cwipc_new_decoder()
            start_time = time.time()
            encoder.feed(pc)
            end_time = time.time()
            encodetime = (end_time - start_time) * 1000
            encodedData = encoder.get_bytes()
            encodesize = len(encodedData)
            start_time=time.time()
            decoder.feed(encodedData)
            decoded_pc = decoder.get()
            end_time = time.time()
            decodetime = (end_time - start_time) * 1000
            decpoints = decoded_pc.get_points()
            decodedpointcount = len(decpoints)
            encoder.free()
            decoder.free()
            decoded_pc.free()
            dataframes = dataframes.append({'Filename':pcframes[i],'readtime':readtime,'filesize':filesize,'pointcount':pointcount,'encodetime':encodetime,'encodesize':encodesize,'decodetime':decodetime,'decodedpointcount':decodedpointcount},ignore_index=True)
    pc.free()
dataframes.to_csv(args.csv)