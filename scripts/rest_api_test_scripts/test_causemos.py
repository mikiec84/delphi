import sys
import json
from math import exp
from matplotlib import pyplot as plt

output = json.load(sys.stdin)

plt.style.use("ggplot")
fig, ax = plt.subplots(len(output["results"]), 1, figsize=(5,10))

for i, (concept, result) in enumerate(output["results"].items()):
    xs = [value["month"] for value in result["values"]]
    ys = [value["value"]*exp(-t) for t, value in enumerate(result["values"])]
    ax[i].plot(xs, ys, label=concept.split('/')[-1])
    ax[i].legend()

plt.tight_layout()
plt.savefig("figure.pdf")
