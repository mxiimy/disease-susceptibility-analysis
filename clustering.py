import hdbscan
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as data
import pandas as pd

def read_pollution_data(f):
    df = pd.read_csv(f)
    print(df)
    print(df.columns)
    df = df.drop([" SO2", " CO", " LAT", " LONG"], axis = 1)
    df = df.drop(["Location Name", " Dataset Code"], axis = 1)

    data = df.to_numpy()
    return data
def cluster_data(data):
    plot_kwds = {'alpha' : 0.5, 's' : 80, 'linewidths':0}
    # moons, _ = data.make_moons(n_samples=50, noise=0.05)
    # blobs, _ = data.make_blobs(n_samples=50, centers=[(-0.75,2.25), (1.0, 2.0)], cluster_std=0.25)
    # test_data = np.vstack([moons, blobs])
    test_data = data

    plt.scatter(test_data.T[0], test_data.T[1], color='b', **plot_kwds)


    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, gen_min_span_tree=True)
    clusterer.fit(test_data)
    hdbscan.HDBSCAN(algorithm='best', alpha=2.0, approx_min_span_tree=True,
        gen_min_span_tree=True, leaf_size=20,
        metric='euclidean', min_cluster_size=1, min_samples=None, p=None)
    palette = sns.color_palette()
    cluster_colors = [sns.desaturate(palette[col], sat)
                      if col >= 0 else (0.5, 0.5, 0.5) for col, sat in
                      zip(clusterer.labels_, clusterer.probabilities_)]
    print(clusterer.labels_)
    plt.scatter(test_data.T[0], test_data.T[1], c=cluster_colors, **plot_kwds)
    plt.show()
    return clusterer.labels_
def top_n(genes: list[list[str]], n: int):
    gene_counts = {}
    for gene_list in genes:
        for gene in gene_list:
            if gene in gene_counts:
                gene_counts[gene] += 1
            else:
                gene_counts[gene] = 1

    keys, vals = gene_counts.items()
    return sorted(keys, key=lambda x: vals[keys.index(x)])[:n]

if __name__ == '__main__':
    count_matrix = np.random.rand(20, 100)

    data = read_pollution_data("AQData.csv")
    d = cluster_data(data)
    design_matrix = np.c_[count_matrix, d]
    design_matrix = pd.DataFrame(design_matrix, columns = list(range(100)) + ['Target'])
    print(design_matrix)
    count_matrix = pd.DataFrame(design_matrix, columns = list(range(100)))
    count_matrix.to_csv('count_matrix.csv')
    design_matrix.to_csv('design_matrix.csv')
    print(count_matrix)
