import sys
import numpy as np
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri, Formula
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr
from statsmodels.stats.multitest import multipletests

# Design matrix should have cluster numbers in a column named 'Target'.
# Clusters should be labelled 0 - cluster_number - 1.
def compute_differentially_expressed_genes(count_matrix: str, design_matrix: str, cluster_number: int, num_clusters: int):
    count_matrix = pd.read_csv(count_matrix)
    design_matrix = pd.read_csv(design_matrix)
    cluster_labels_without_curr = list(range(cluster_number))
    cluster_labels_without_curr.remove(cluster_number)
    design_matrix = design_matrix.replace(cluster_labels_without_curr, [1])

    base = importr('base')
    stats = importr('stats')
    limma = importr('limma', lib_loc='path to the downloaded R package limma')
    writexl = importr('writexl',
                      lib_loc='path to the downloaded R package writexl')

    # Covert to R dfs.
    with localconverter(ro.default_converter + pandas2ri.converter):
        count_matrix = ro.conversion.py2ri(count_matrix)
        design_matrix = ro.conversion.py2ri(design_matrix)

        # Get strings corresponding to genes separately.
        genes = ro.StrVector(
        [
            str(index)
            for index in count_matrix.index.tolist()
        ]
    )

    # Get unique values of CC status.
    f = base.factor(design_matrix.rx2('Target'),
                    levels=base.unique(design_matrix.rx2('Target')))
    form = Formula('~0 + f')
    form.environment['f'] = f
    design_matrix = stats.model_matrix(form)
    design_matrix.colnames = base.levels(f)

    # Fit a model for each gene.
    fit = limma.lmFit(count_matrix, design_matrix)
    # Finds relative difference between models (?). Specifies range of case control statuses.
    contr = limma.makeContrasts(f"{design_matrix.colnames[0]}-{design_matrix.colnames[-1]}", levels=design_matrix)

    # Fit a bayesian model on contrasts and estimate significant contrasts using p values.
    bayes_fit = limma.contrasts_fit(fit, contr)
    bayes_fit = limma.eBayes(bayes_fit)

    # Write best genes by p values.
    top_genes = limma.topTable(bayes_fit, sort_by="P")
    writexl.write_xlsx(top_genes, "limma_output.xlsx")
