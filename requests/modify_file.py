import pandas as pd

url="https://drive.google.com/file/d/1-YxGNv8xhwr0Jca_Ra5J2oyaI-gYZIQq/view?usp=sharing"
df = pd.read_csv(url)
print(df)
pass