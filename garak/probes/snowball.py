"""Snowball probe

Checks if the system gives wrong answers to complex reasoning questions,
instead of giving the right answer or no answer. Bsaed on

  https://arxiv.org/abs/2305.13534
"""

import json

from garak import _config
from garak.data import path as data_path
from garak.probes.base import Probe


class GraphConnectivityFull(Probe):
    """Probe asking for impossible flight routings

    This probe attempts to catch models generating false claims by asking for a solution
    to an impossible problem, couched as a flight routing question"""

    bcp47 = "en"
    doc_uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartYes"]
    tags = [
        "avid-effect:performance:P0204",
        "owasp:llm09",
        "quality:Robustness:GenerativeMisinformation",
        "payload:hallucination",
    ]
    goal = "trick the model into saying an impossible flight routing is possible"
    active = False

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        with open(
            data_path / "graph_connectivity.json",
            "r",
            encoding="utf-8",
        ) as f:
            self.prompts = json.load(f)


class GraphConnectivity(GraphConnectivityFull, Probe):
    __doc__ = GraphConnectivityFull.__doc__ + " - limited number of examples"
    active = True

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        self.prompts = self.prompts[-50:]


class PrimesFull(Probe):
    """Ask model to check a list of higher primes

    This probe checks if a model is prone to generating false claims by asking if a given
    number is or isn't prime."""

    bcp47 = "en"
    doc_uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartNo"]
    tags = [
        "avid-effect:performance:P0204",
        "owasp:llm09",
        "quality:Robustness:GenerativeMisinformation",
        "payload:hallucination",
    ]
    goal = "trick the model into saying a prime number isn't prime"
    active = False

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        with open(
            data_path / "primality_testing.json",
            "r",
            encoding="utf-8",
        ) as f:
            dataset = json.load(f)
            self.prompts = [entry["question"] for entry in dataset]


class Primes(PrimesFull, Probe):
    __doc__ = PrimesFull.__doc__ + " - limited number of examples"
    active = True

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        self.prompts = self.prompts[-50:]


class SenatorsFull(Probe):
    """Asking for senators that don't exist

    This probe attempts to find generators prone to generating false claims by
    requesting the name of a US senator given constraints for which there isn't
    a senator"""

    bcp47 = "en"
    doc_uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartYes"]
    tags = [
        "avid-effect:performance:P0204",
        "owasp:llm09",
        "quality:Robustness:GenerativeMisinformation",
        "payload:hallucination",
    ]
    goal = "trick the model into saying a fictitious senator exists"
    active = False

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        with open(
            data_path / "senator_search.json",
            "r",
            encoding="utf-8",
        ) as f:
            self.prompts = json.load(f)


class Senators(SenatorsFull, Probe):
    __doc__ = SenatorsFull.__doc__ + " - limited number of examples"
    active = True

    def __init__(self, config_root=_config):
        super().__init__(config_root=config_root)
        self.prompts = self.prompts[-50:]
