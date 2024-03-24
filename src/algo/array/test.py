a = {}

a["k1"] = {"key2": 2}

a.update({
            "memory-usage-before": 1,
            "memory-usage-after": 1,
            "cpu-usage-before": 1,
            "cpu-usage-after": 1
        })
print(a)