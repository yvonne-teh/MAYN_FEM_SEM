import math
import counted_verb_dicts
from softmax import softmax_dict

LOG_DICTS = []
for d in counted_verb_dicts.dict_original:
    LOG_DICTS.append(({key: math.log10(value)
                     for key, value in d[0].items()}, d[1]))

SOFTMAXED_DICTS = []
for d in counted_verb_dicts.dict_original:
    SOFTMAXED_DICTS.append((softmax_dict(d[0]), d[1]))

for dic in SOFTMAXED_DICTS:
    print(dic)