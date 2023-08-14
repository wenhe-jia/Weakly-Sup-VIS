# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.
from detectron2.config import CfgNode as CN


def add_maskformer2_video_config(cfg):
    # video data
    # DataLoader
    cfg.INPUT.SAMPLING_FRAME_NUM = 2
    cfg.INPUT.SAMPLING_FRAME_RANGE = 20
    cfg.INPUT.SAMPLING_FRAME_SHUFFLE = False
    cfg.INPUT.AUGMENTATIONS = []  # "brightness", "contrast", "saturation", "rotation"

    cfg.INPUT.FIXED_SAMPLING_INTERVAL = False

    cfg.MODEL.MASK_FORMER_VIDEO = CN()

    # model inference
    cfg.MODEL.MASK_FORMER_VIDEO.TEST = CN()
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.TRACKER_TYPE = 'org_m2f_offline'  # 'MinVIS' => frame-level tracker
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.WINDOW_INFERENCE = True
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.MULTI_CLS_ON = True
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.APPLY_CLS_THRES = 0.05
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.MERGE_ON_CPU = False
    # clip-by-clip tracking with overlapped frames
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.NUM_FRAMES = 3
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.NUM_FRAMES_WINDOW = 30
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.NUM_MAX_INST = 50
    cfg.MODEL.MASK_FORMER_VIDEO.TEST.CLIP_STRIDE = 1

    # weak supervision
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION = CN()
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.TEMPORAL_PAIRWISE_WEIGHT = 2.0
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.WARM_UP = False
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.TEMPORAL_TOPK = 1
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.FILTER_BY_COLOR = False
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.TEMPORAL_COLOR_THRESH = 0.1
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.USE_INPUT_RESOLUTION = False
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.TEMPORAL_DIST_THRESH = 0.9
    cfg.MODEL.MASK_FORMER_VIDEO.WEAK_SUPERVISION.PCA_SPLIT_MATCH = False


