# %%  # noqa: INP001
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz  # plot tree
from sklearn.metrics import roc_curve, auc  # model eval
from sklearn.metrics import classification_report  # model eval
from sklearn.metrics import confusion_matrix  # model eval

import warnings

warnings.filterwarnings("ignore")

# %%
rng = np.random.default_rng(12345)

sns.set_theme(
    style="ticks", palette="Spectral", font_scale=1.2, rc={"figure.figsize": (12, 8)}
)
sns.color_palette(palette="Spectral", as_cmap=True)
# %%
_df = pd.read_csv("./data/heart-disease.csv")
_df.head()
_df.info()

# %%
_df["target"].value_counts()
# %%
# Data Prep
_df.columns = [
    "age",
    "sex",
    "chest_pain_type",
    "resting_bp",
    "cholest",
    "fasting_cho",
    "rest_ecg",
    "max_hr_achieved",
    "exercise_induced_angina",
    "st_depress",
    "st_slope",
    "num_maj_vessels",
    "thalessemia",
    "target",
]
_df.head()
# %%
# train/test split time
X = _df.iloc[:, :-1]
Y = _df.iloc[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0
)

# %%
# fitting a random forest classifier w/ 20 estimators and computing the AUC achieved.
## Training and fitting a random forest model
model_rf = RandomForestClassifier(n_estimators=20, max_depth=5, random_state=0).fit(
    X_train, Y_train
)

## Making predictions on the test set
Y_pred = model_rf.predict_proba(X_test)[:, 1]

## Print the AUC achieved by the classifier on the test set
fpr, tpr, thresholds = roc_curve(Y_test, Y_pred)
auc(fpr, tpr)  # 0.9189570119802678
### Now have our model and our predictions. Explore different ways to understand the model and its predictions in a more meaningful way.
# %%
from sklearn.inspection import permutation_importance

result = permutation_importance(
    model_rf, X_test, Y_test, n_repeats=30, n_jobs=2, random_state=0
)

# %%
result.importances_mean.argsort()
# %%
# Visualizing the distributions.
sorted_idx = result.importances_mean.argsort()

fig, ax = plt.subplots()
boxplot = ax.boxplot(
    result.importances[sorted_idx].T,
    vert=False,
    labels=X_test.columns[sorted_idx],
    patch_artist=True,
)

colors = [
    "blue",
    "green",
    "purple",
    "tan",
    "pink",
    "red",
    "blue",
    "green",
    "purple",
    "tan",
    "pink",
    "red",
]
for patch, color in zip(boxplot["boxes"], colors):
    patch.set_facecolor(color)

ax.set_title("Permutation Importances")
fig.tight_layout()
plt.show()
# %%
