import pandas as pd

Datos = pd.DataFrame({"hora": ["0.29 [0.15-0.48]", "6.586 [0.15-0.48]", "9800 [10-200]", "3 [10-200]", "6.586 [0.15-0.48]"]})
Datos["hora"] = Datos["hora"].str.extract(r"(.*\d\s)")
print(Datos)