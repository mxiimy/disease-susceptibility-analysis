# disease-susceptibility-analysis

Create a tool capable of predicting susceptibility to disease in remote or otherwise underserved areas.


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Abstract

The project aims to create a tool to provide public health officials and epidemiologists with a way of predicting susceptibility to disease in remote or otherwise underserved areas. 
The tool will accomplish this by taking environmental and climate data, which is readily available for many regions without access to robust medical testing and predicting over and under expressed genes which can be interpreted as biomarkers and used to predict disease susceptibility.
The tool will accomplish this by using two layers. 
First, by data scraping online repositories of environmental data from agencies such as the EPA, NCEI, NOAA and international equivalents it will determine a score in each environmental metric to summarize the conditions over a biologically relevant time scale. 
Using this data and user input RNA-seq data tagged with geographic information we will train a machine learning model to predict over and under expressed genes in specific tissue given a set of environmental conditions. 
The model can then be applied to a map of environmental data to determine heatmaps for gene expression. 
A second model will scan literature for references to biomarkers and create maps of disease susceptibility given the gene expression heatmaps. 
We believe the intermediary use of RNA-seq data would allow the models to interpret disease susceptibility in regions with novel environmental conditions.
Some diseases require multifarious gene expression anomalies, but the environmental aspects facilitating these anomalies may not be simultaneously present in the training data so the disease may not be seen in the training population.
However, the model could still predict the presence of all necessary biomarkers even in a novel environment since RNA-seq data allows the model to work with more degrees of freedom.

## Installation

Provide instructions on how to install and set up the project, such as installing dependencies and preparing the environment.

```bash
# Example command to install dependencies (Python)
pip install project-dependencies

# Example command to install dependencies (R)
install.packages("project-dependencies")
```

## Quick Start

Provide a basic usage example or minimal code snippet that demonstrates how to use the project.

```python
# Example usage (Python)
import my_project

demo = my_project.example_function()
print(demo)
```
```r
# Example usage (R)
library(my_project)

demo <- example_function()
print(demo)
```

## Usage

Add detailed information and examples on how to use the project, covering its major features and functions.

```python
# More usage examples (Python)
import my_project

demo = my_project.advanced_function(parameter1='value1')
print(demo)
```
```r
# More usage examples (R)
library(demoProject)

demo <- advanced_function(parameter1 = "value1")
print(demo)
```

## Contribute

Contributions are welcome! If you'd like to contribute, please open an issue or submit a pull request. See the [contribution guidelines](CONTRIBUTING.md) for more information.

## Support

If you have any issues or need help, please open an [issue](https://github.com/hackbio-ca/disease-susceptibility-analysis/issues) or contact the project maintainers.

## License

This project is licensed under the [MIT License](LICENSE).
