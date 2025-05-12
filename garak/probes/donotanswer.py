"""
Do-Not-Answer Probes

https://github.com/Libr-AI/do-not-answer
https://arxiv.org/abs/2308.13387

An open-source dataset to evaluate LLMs' safety mechanism at a low cost.
The dataset consists of prompts to which language models are often trained not to answer.
"""

# import sys
# from garak import _config
# from garak.data import path as data_path
# from garak.probes.base import Probe

# this = sys.modules[__name__]


# def load_local_data(self):
#     # prompts
#     with open(
#         data_path / "donotanswer" / f"{self.dna_category}.txt",
#         encoding="utf=8",
#     ) as f:
#         self.prompts = f.read().strip().split("\n")


# def local_constructor(self, config_root=_config):
#     super(self.__class__, self).__init__(config_root=config_root)
#     self.load_data()


# DNA_PROBE_TAGS = {
#     "discrimination_exclusion_toxicity_hateful_offensive": [
#         "avid-effect:ethics:E0301",
#         "quality:Behavioral:ContentSafety:Toxicity",
#         "quality:Behavioral:ContentSafety:HateHarassment",
#         "quality:Behavioral:ContentSafety:Violence",
#         "quality:Behavioral:ContentSafety:Profanity",
#     ],
#     "human_chatbox": [
#         "avid-effect:security:S0301",
#         "quality:Behavioral:ContentSafety:Unauthorized",
#     ],
#     "information_hazard": [
#         "owasp:llm06",
#         "avid-effect:security:S0301",
#         "quality:Security:Confidentiality",
#     ],
#     "malicious_uses": [
#         "quality:Behavioral:ContentSafety:LegalGoodsServices",
#     ],
#     "misinformation_harms": [
#         "quality:Robustness:GenerativeMisinformation",
#         "avid-effect:ethics:E0402",
#         "owasp:llm09",
#     ],
# }

# for probe_class in list(DNA_PROBE_TAGS.keys()):
#     failure_name = probe_class.replace("_", " ")
#     classname = probe_class.title().replace("_", "")
#     goal = f"get model to respond as {failure_name}"
#     descr = f"Implementation of {probe_class} probes in DoNotAnswer_Prompts"
#     doc = f"Do Not Answer probe\n\nA curated list of questions to which LLMs should not respond back, specifically testing {failure_name}"

#     # define class
#     setattr(
#         this,
#         classname,
#         type(
#             classname,
#             (Probe,),
#             {
#                 "__init__": local_constructor,
#                 "__doc__": doc,
#                 "uri": "https://arxiv.org/abs/2308.13387",
#                 "bcp47": "en",
#                 "description": descr,
#                 "primary_detector": "mitigation.MitigationBypass",
#                 "prompts": [],
#                 "load_data": load_local_data,
#                 "goal": goal,
#                 "dna_category": probe_class,
#                 "tags": DNA_PROBE_TAGS[probe_class],
#                 "active": True,  # strong content norms not applicable in many scenarios
#             },
#         ),
#     )

import sys
from garak import _config
from garak.data import path as data_path
from garak.probes.base import Probe

# def load_local_data(self):
#     # prompts
#     with open(
#         data_path / "donotanswer" / f"{self.dna_category}.txt",
#         encoding="utf=8",
#     ) as f:
#         self.prompts = f.read().strip().split("\n")


class DiscriminationExclusionToxicityHatefulOffensive(Probe):
    """Do Not Answer probe

    A curated list of questions to which LLMs should not respond back, specifically testing discrimination exclusion toxicity hateful offensive"""
    with open(
        data_path / "donotanswer" / "discrimination_exclusion_toxicity_hateful_offensive.txt",
        encoding="utf=8",
    ) as f:
        prompts = f.read().strip().split("\n")
        # garak/data/donotanswer/discrimination_exclusion_toxicity_hateful_offensive.txt

    uri = "https://arxiv.org/abs/2308.13387"
    bcp47 = "en"
    description = "Implementation of discrimination_exclusion_toxicity_hateful_offensive probes in DoNotAnswer_Prompts"
    primary_detector = "mitigation.MitigationBypass"
    prompts = prompts
    dna_category = "discrimination_exclusion_toxicity_hateful_offensive"
    goal = "get model to respond as discrimination exclusion toxicity hateful offensive"
    tags = [
        "avid-effect:ethics:E0301",
        "quality:Behavioral:ContentSafety:Toxicity",
        "quality:Behavioral:ContentSafety:HateHarassment",
        "quality:Behavioral:ContentSafety:Violence",
        "quality:Behavioral:ContentSafety:Profanity",
    ]
    active = True

    # def __init__(self, config_root=_config):
    #     super().__init__(config_root=config_root)
    #     self.load_data()

    # def load_data(self):
    #     load_local_data(self)



class HumanChatbox(Probe):
    """Do Not Answer probe

    A curated list of questions to which LLMs should not respond back, specifically testing human chatbox"""
    # garak/data/donotanswer/human_chatbox.txt
    with open(
        data_path / "donotanswer" / "human_chatbox.txt",
        encoding="utf=8",
    ) as f:
        prompts = f.read().strip().split("\n")

    uri = "https://arxiv.org/abs/2308.13387"
    bcp47 = "en"
    description = "Implementation of human_chatbox probes in DoNotAnswer_Prompts"
    primary_detector = "mitigation.MitigationBypass"
    prompts = prompts
    dna_category = "human_chatbox"
    goal = "get model to respond as human chatbox"
    tags = [
        "avid-effect:security:S0301",
        "quality:Behavioral:ContentSafety:Unauthorized",
    ]
    active = True


class InformationHazard(Probe):
    """Do Not Answer probe

    A curated list of questions to which LLMs should not respond back, specifically testing information hazard"""
    # garak/data/donotanswer/information_hazard.txt
    with open(
        data_path / "donotanswer" / "information_hazard.txt",
        encoding="utf=8",
    ) as f:
        prompts = f.read().strip().split("\n")

    uri = "https://arxiv.org/abs/2308.13387"
    bcp47 = "en"
    description = "Implementation of information_hazard probes in DoNotAnswer_Prompts"
    primary_detector = "mitigation.MitigationBypass"
    prompts = prompts
    dna_category = "information_hazard"
    goal = "get model to respond as information hazard"
    tags = [
        "owasp:llm06",
        "avid-effect:security:S0301",
        "quality:Security:Confidentiality",
    ]
    active = True

class MaliciousUses(Probe):
    """Do Not Answer probe

    A curated list of questions to which LLMs should not respond back, specifically testing malicious uses"""
    # garak/data/donotanswer/malicious_uses.txt
    with open(
        data_path / "donotanswer" / "malicious_uses.txt",
        encoding="utf=8",
    ) as f:
        prompts = f.read().strip().split("\n")

    uri = "https://arxiv.org/abs/2308.13387"
    bcp47 = "en"
    description = "Implementation of malicious_uses probes in DoNotAnswer_Prompts"
    primary_detector = "mitigation.MitigationBypass"
    prompts = prompts
    dna_category = "malicious_uses"
    goal = "get model to respond as malicious uses"
    tags = [
        "quality:Behavioral:ContentSafety:LegalGoodsServices",
    ]
    active = True


class MisinformationHarms(Probe):
    """Do Not Answer probe

    A curated list of questions to which LLMs should not respond back, specifically testing misinformation harms"""
     # garak/data/donotanswer/misinformation_harms.txt
    with open(
        data_path / "donotanswer" / "misinformation_harms.txt",
        encoding="utf=8",
    ) as f:
        prompts = f.read().strip().split("\n")

    uri = "https://arxiv.org/abs/2308.13387"
    bcp47 = "en"
    description = "Implementation of misinformation_harms probes in DoNotAnswer_Prompts"
    primary_detector = "mitigation.MitigationBypass"
    prompts = prompts
    dna_category = "misinformation_harms"
    goal = "get model to respond as misinformation harms"
    tags = [
        "quality:Robustness:GenerativeMisinformation",
        "avid-effect:ethics:E0402",
        "owasp:llm09",
    ]
    active = True
