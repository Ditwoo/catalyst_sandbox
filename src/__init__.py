from catalyst.dl import registry
from catalyst.dl import SupervisedRunner as Runner

from .models import SimpleNet
from .callbacks import DoSomethingWithDataCallback
from .experiment import Experiment


registry.Model(SimpleNet)
registry.Callback(DoSomethingWithDataCallback)
