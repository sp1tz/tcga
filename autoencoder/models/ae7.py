import torch


class AE(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.eH0 = torch.nn.Linear(  # encoderHiddden
            in_features=kwargs["input_shape"], out_features=11880
        )
        self.eH1 = torch.nn.Linear(
            in_features=11880, out_features=5945
        )
        self.eH2 = torch.nn.Linear(
            in_features=5945, out_features=10
        )
        self.eO = torch.nn.Linear(  # encoderOutput
            in_features=10, out_features=10
        )
        self.dH0 = torch.nn.Linear(  # decoderHidden
            in_features=10, out_features=10
        )
        self.dH1 = torch.nn.Linear(
            in_features=10, out_features=5945
        )
        self.dH2 = torch.nn.Linear(
            in_features=5945, out_features=11880
        )
        self.dO = torch.nn.Linear(
            in_features=11880, out_features=kwargs["input_shape"]
        )

    def forward(self, features):
        a = self.eH0(torch.nn.functional.tanh(features))  # activation
        a = self.eH1(torch.nn.functional.tanh(a))
        a = self.eH2(torch.nn.functional.tanh(a))
        a = self.eO(torch.nn.functional.tanh(a))
        a = self.dH0(torch.nn.functional.tanh(a))
        a = self.dH1(torch.nn.functional.tanh(a))
        a = self.dH2(torch.nn.functional.tanh(a))
        return self.dO(torch.nn.functional.tanh(a))