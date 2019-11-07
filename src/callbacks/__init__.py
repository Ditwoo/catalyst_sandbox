from catalyst.dl.core import Callback, CallbackOrder, RunnerState


class DoSomethingWithDataCallback(Callback):
    def __init__(self,
        prefix: str = "accuracy",
        input_key: str = "targets",
        output_key: str = "logits",
        **metric_params):
        super().__init__(CallbackOrder.Internal)
        self.prefix: str = prefix
        self.input_key: str = input_key
        self.output_key: str = output_key
        self.metric_params = metric_params

    def on_epoch_start(self, state: RunnerState):        
        for k, v in vars(state).items():
            print(f'{k}:', v, flush=True)
    
        import pdb; pdb.set_trace()

        return state