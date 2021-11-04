#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ==============================================================================
#          \file   read.py
#        \author   chenghuige  
#          \date   2019-07-26 18:02:22.038876
#   \Description  
# ==============================================================================

  
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys 
import os

from tfrecord_dataset import Dataset

import tensorflow as tf 
flags = tf.app.flags
FLAGS = flags.FLAGS

tf.compat.v1.enable_eager_execution()

FLAGS.train_input = '../input/tfrecord/train'
FLAGS.valid_input = '../input/tfrecord/valid'

FLAGS.use_portrait_emb = True

dataset = Dataset('train')

da = dataset.make_batch()

for i, batch in enumerate(da):
    print('---------------------------', i)
    print(batch[0]['id'], batch[0]['id'].shape, batch[1].shape, batch[0]['index'].shape)
    #print(batch[0]['index'][0])
    print(batch[0])
    print(batch[0]['field'][0])
    if i == 1:
        exit(0)
exit(0)
