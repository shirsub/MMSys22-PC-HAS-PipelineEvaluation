# MMSys22-PC-HAS-PipelineEvaluation

This repository contains scripts and resources used for the MMsys22 pipeline evaluation paper

## Experiment Design:
[Protocol Document](https://docs.google.com/document/d/1sYKZRhz2gKFqfMwrYvrU_n1WRwgcIUVP/edit)

## Planning:
### Experiment 1: Systems Evaluation - 3 virtual users + orchestrator:

#### Tasks:
 - Create Experimental Dataset - Need to decide between 3 and 4 camera configurations 

 - Set Experimental Conditions:
	- ~~Finalize Renderer Optimizations~~ 
	- ~~Determine max achievable adaptation set size~~: Seems to be 2 octree levels (8,9) X 2 JPEGQP(25,95), needs further investigation
	- Determine target bitrates: Need to make a decision on voxelization first
	- ~~Determine Limits of segment size supported by signals~~: Seems to be 100 ms to 3000ms (3-90 frames in offline GoP expt 2 and 1-45 frames in live expt1,3) 
	
  - Prepare tile metadata files 

  - Determine fixed point sizes based on codec configuration (real time 5NN based calculation is not possible)

  - Create version of VRTApp that can playback prerecorded navigation paths and expose the relevant parameters in config.json 

    
### Experiment 2: Quality Evaluation User study - 1 user + orchestrator + HMD:
#### Tasks:
 - Implement GoP adaptation with the GoP size set in config.json
 - Select sequences from CWIPC-SXR to use: S3 (Minnie), S1 (Professor), S4R2 (Gerrard), S8 (Steven)
 - Select target bitrates for CWIPC-SXR
 - Select Adaptation Set Size (Maybe we use the max for this experiment)
### Experiment 3: sVR QoE User Study  - 2 users + orchestrator + 2 x HMD
#### Tasks: 
 - Test current state of tiled playout + audio 
## Useful Links:
### Rendering: 
Point cloud rendering tutorial: https://bootcamp.uxdesign.cc/point-cloud-rendering-with-unity-1a07345eb27a
https://medium.com/realities-io/point-cloud-rendering-7bd83c6220c8
Point Cloud Rendering Open Source Project: https://github.com/ahmaderfani12/PointClouds
General shader guidelines: https://github.com/patriciogonzalezvivo/thebookofshaders
Point Cloud Artwork: https://www.youtube.com/watch?v=gfyuuo1LwCE&ab_channel=Dezeen