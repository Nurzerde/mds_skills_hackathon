import logging
import re

import df_engine.conditions as cnd
from df_engine.core import Actor
from df_engine.core.keywords import LOCAL, RESPONSE, TRANSITIONS


# import condition as loc_cnd
import response as rsp
global res
res=str()

plot = {
    "greeting_flow": {
        "start_node": {  # This is an initial node, it doesn't need an `RESPONSE`
            RESPONSE: "",
            TRANSITIONS: {"node1": cnd.regexp(r"hi", re.IGNORECASE)},  # If "Hi" == request of user then we make the transition
        },
        "node1": {
            RESPONSE: "Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?",  # When the agent goes to node1, we return "Hi, how are you?"
            TRANSITIONS: {
                "node2": cnd.any([cnd.regexp(r".*topic*", re.IGNORECASE)], [cnd.regexp(r".*phrase*", re.IGNORECASE)]),
                "node7": cnd.any([cnd.regexp(r".*random*", re.IGNORECASE)], [cnd.regexp(r".*source*", re.IGNORECASE)]),
            },
        },
        "node2": {
            RESPONSE: "Name the Holy Book: Bible or Quran to get sample from.",
            TRANSITIONS: {"node3": cnd.all([cnd.regexp(r".*bible", re.IGNORECASE)]),
                          "node4": cnd.all([cnd.regexp(r".*quran", re.IGNORECASE)])},
            },
        "node3": {
            RESPONSE: "Name the topic",
            TRANSITIONS: {"node5": cnd.any([cnd.regexp(r".*", re.IGNORECASE)])},
            },
        "node4": {
            RESPONSE: "Name the topic",
            TRANSITIONS: {"node6": cnd.any([cnd.regexp(r".*", re.IGNORECASE)])},
            },
        "node5": {
            RESPONSE: rsp.Bible,
            TRANSITIONS: {"node1": cnd.any([cnd.regexp(r".*", re.IGNORECASE)])},
            },
        "node6": {
            RESPONSE: rsp.Quran,
            TRANSITIONS: {"node1": cnd.any([cnd.regexp(r".*", re.IGNORECASE)])},
            },
        "node7": {
            RESPONSE: rsp.RandP,
            TRANSITIONS: {"node1": cnd.any([cnd.regexp(r".*", re.IGNORECASE)])},
            },
        "fallback_node": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Ooops",
            TRANSITIONS: {"node1": cnd.exact_match("Hi")},
        },
    }
}

actor = Actor(plot, start_label=("greeting_flow", "start_node"), fallback_label=("greeting_flow", "fallback_node"))
