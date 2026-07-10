import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.datasets import make_blobs 
sns.set()

points, cluster_indexes = make_blobs(n_samples = 300, centers = 4, cluster_std=0.8, random_state=0)

x = points[:, 0] 
y = points[:, 1]
plt.scatter(x, y, s=50, alpha=0.7) 
















if __name__ == "__main__":
    pass
