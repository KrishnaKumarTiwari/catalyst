# flake8: noqa
from catalyst.dl import SupervisedRunner as Runner
from .experiment import Experiment
from catalyst.dl.registry import MODELS  # isort:skip

#  TODO: fix hack for duplicate SimpleNets
del MODELS["SimpleNet"]  # isort:skip
from .model import SimpleNet  # isort:skip
