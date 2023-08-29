import os 
os.chdir('/disk7T/ypguo/FedScale')

import sys
import fedscale.cloud.config_parser as parser
from fedscale.cloud.execution.torch_client import TorchClient
from fedscale.cloud.aggregation.aggregator import Aggregator

test_Aggregation = Aggregator(parser.args)


import fedscale.cloud.config_parser as parser
from fedscale.cloud.execution.torch_client import TorchClient
from fedscale.cloud.execution.executor import Executor
### On CPU
parser.args.use_cuda = "False"
Demo_Executor = Executor(parser.args)
Demo_Executor.run()
