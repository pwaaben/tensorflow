"""Main Scikit Flow module."""
#  Copyright 2015 Google Inc. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import collections
import random

import json
import os
import datetime

import numpy as np
import tensorflow as tf

from google.protobuf import text_format

from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.utils import check_array
from sklearn.utils.validation import NotFittedError

from skflow.trainer import TensorFlowTrainer
from skflow import models
from skflow import data_feeder
from skflow import preprocessing
from skflow import ops
from skflow.io import *
from skflow.estimators import *

