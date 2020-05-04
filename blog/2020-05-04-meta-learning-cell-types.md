title: Meta learning cell types

[TOC]

## Abstract

Recently, [Bribic20](https://doi.org/10.1101/2020.02.25.960302) provided an approach to meta-learn representations of cell types. The preprint presents an end-to-end-trained data-driven approach for classifying (=clustering and annotating) cells based on scRNA-seq measurements and cell type annotations.

To me, the approach appears to be the so-far most systematic and scalable effort to comprehensively address data-driven cell type classification. Here, I review some of the related literature and technical challenges of the problem.

## What is a cell type?

Brbic20 takes a data-driven take on cell type definition while the community still struggles with the precise definition of the notion. While I don't consider Bribic20 to be the first method that learns a cell type embedding, or the first method to jointly leverage annotated and unannotated data.

**Metric cell type embeddings:** To my knowledge, metric learning has been applied to cellular images for many years; for instance, in [Ando17](https://doi.org/10.1101/161422) and follow up work. Efforts have also been made for scRNA-seq, such as with [Chen18](https://doi.org/10.1101/456814). None of these provided methods have matured into usable tools, though.

More recently, also [Xu19](https://doi.org/10.1101/532895) ("scANVI") suggested to use an embedding of landmarks based on cell annotations to probabilistically assign cell labels in unannotated data, using a Gaussian mixture in a VAE, which should automatically induce a metric. The setup, however, leads to a different objective function than in the present manuscript. While the present manuscript compares performance with scVI, the more interesting case would be to compare with scANVI.

**Joint learning on annotated and unannotated data:** The present manuscript discusses a "meta learning" approach according to [Finn16](https://arxiv.org/abs/1703.03400) in the sense that it uses an unsupervised learning task on the target data of interest to better solve the supervised learning task. While this is great, it'd be also worthwhile to point out that a variant of this is standard practice, albeit not referred to as meta learning in the field. The authors please correct me if I'm mistaken.

The standard variant consists in using "batch-correction" approaches, which minimize the distance between the distributions of datasets of interest while maintaining some unsupervised structure, and then training a supervised classifier on this batch-corrected data. If the authors agree, they could present their work as a formalization of this ad-hoc established approach, which is also often used to benchmark batch correction methods.

**Symbolic cell-type representations:** The community standard today is still to operate on symbolic representations of cell types via lists of marker genes, in the form of knowledge that is present in papers. Most systematically, presumably, this is implemented in scMap. Not everyone might be aware of the drawbacks of such symbolic reprsentations and the difficulty to integrate them with data-driven approaches. It'd be interesting if the authors commented on this, in particular as there are experts on knowledge graphs among the authors, who could estimate the feasibility of integrating cell type annotation knowledge from papers with a learned embedding. Again, this is just a potential topic for the discussion.

**Further context:** Independent from this, claims have been made that cell type classification is indeed a very simple problem and gains through deep-learning techniques are limited ([Kohler19](https://doi.org/10.1101/653907)).

**What are challenging cases?**

## How to learn representations of cell types?

**Benchmark availability and reproducibility.** While the code of the package is available on GitHub, and of decent quality, there is no repository for the reproducibility of the results in the paper. The reproducibility repository can also serve for providing tutorials. Without seeing the API in application on at least 3 datasets, in three clean notebooks, I don't think the tool will be widely adapted. It'd be awesmoe if there was a table linking to notebooks that produce the figures of the paper, for instance, comparable to [this](https://github.com/theislab/paga). I hope this is little work for the authors.

**Cross-dataset benchmark.** The manuscript discusses a cell type annotation method that is of potential use for classifying across datasets. However, such cross-dataset benchmarking is not presented. As far as I understand it, the method is not even evaluated for predicting across Tabula Muris to Tabula Muris Senis, even though these two are fairly similarly distributed (similar technical variation); and I would consider this an easy case. For instance, Scanorama integrated 26 completely unrelated datasets in an unsupervised way, and transferred cell type labels between these. This or the Pancreas datasets used in BBKNN could be potential candidates. Conos also presented large-scale integrations of datasets. Another source of benchmarks would be the review by [Abdelall19](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1795-z).

**Initialization of cell type landmarks.** How robust is the method to the number of clusters in k-means clustering for initializing the landmarks. Can you show how information from the annotated dataset leads to the contraction of initialized cell clusters into one cell-type-associated cluster?

**Additional resolution of cell types/ improving on flawed annotations.** Are the separated luminal epithelial cells just an effect of the initialization? Is this "label-splitting" an effect that only happens once? Can you quantify how often it appears by running Leiden clustering on the embedding and comparing its granularity with the granularity of the annotations (or by putting forward a better idea of investigating this)? If the learned representation shows additional cell type resolution, this means that the model managed to overcome flaws in the annotation by transferring information across datasets. Quantifying that information gain and demonstrating that it's meaningful (as has been done for the luminal epithelial example), would be impressive. If there is no such effect, the method is still worth publishing, but it should be stated clearly that meta learning only happens in the sense that existing variation in the unannotated data is maintained, not in the sense that the unsupervised data actually helps to improve the annotations. The latter is what the picked example of the luminal cells suggested.

**Performance on unseen cell types.** Can you report the classification performance on unseen cell lines in the cross-tissue-validation benchmark? It is unclear how much the performance is dominated by seen cell types.

**MARS identifies cell-type-specific signatures of aging.** This is the first benchmark, but neither the figure caption nor the main text explains how train/test splits are chosen, what the meta-learning aspect of this benchmark is, and whether it only holds for a single tissue. How was the compute initialized? Has the model been trained on 3 months, and the rest been held out to initialize cell types in an unsupervised fashion?

**Effect of learning from annotations in combination with the unsupervised task.** Can you contrast the result from learning from the unsupervised task (pure embedding of the auto-encoder) with the joint result? And show how that improves performance when compared to applying a simple classifier (with and without prototypical loss) that was trained on the same annotated datasets to the held-out unannotated dataset? To me, this would but the more appropriate comparison than scVI and SIMLR, which clearly demonstrates the advantage of the specific meta-learning setup chosen.

**Comparing with scANVI.** Besides techniques such as scMap, I think, one should also compare to scANVI, which seems the most related technique in the field, which also learns landmark cell types, albeit with a different setup. Explaining the difference in the supplemental material.

**Community benchmark.**

## Examples

We use the brain adipose tissue (BAT) data from 3 months, 18 months, and 24 months old mice as the annotated experiments. We find that MARS aligns all cell types except the set of natural killer (NK) cells.

Is this surprising? This, so far, only means that batch effect is limited, as no batch-correction component of the objective function has been described.

As is, I don't think that the paragraph "MARS identifies cell-type-specific signatures of aging." captures a result that goes beyond what has been described previously in many instances. See suggestions on clarifications above.

Remarkably, MARS achieves 31% better adjusted Rand index score than the second-best performing SIMLR.

I do think it's confounding to only report a single metric in the main text.

To me, classifying cell types is a typical classification problem prone to class imbalance.

Hence, what I'd expect to see is f1-macro, precision-macro, recall-macro, and a distribution over f1 over the different classes.

I'm aware that Leiden, Louvain, and scVI don't provide that directly, but you report f1 for leiden in Fig. 1b already; so you seem to post-process the clustering output with a "labeling/bookkeeping step".

Can you comment on why f1 is so similar across all methods? I think MARS shows a clear, significant advance. But seeing that scVI is just as good as leiden is somewhat surprise. Also see the suggested additional benchmark of a "simple classifier" above.

Can you discuss how ARI deals with unseen cell types? The only property we want for them is that they don't get misclassified as seen cell types. Right? How is that being accounted for? And how is that resolved in the API - do you output no class label when you have very little confidence that the test observation doesn't belong to a previously observed class? Also these questions have been more concisely summarized above.

Can you demonstrate that both in a tutorial notebook and touch on it in the manuscript?

Error bars are standard errors estimated by bootstrapping cells within tissue with n=20 iterations. MARS is trained in leave-one-tissue-out manner, and the held out tissue was completely unannotated (see Methods).

As you're doing leave-one-out cross validation anyway, why don't you get the error bars from that, and do bootstrapping in addition? Is there a caveat with that?

In contrast, in the embedding space learned by scVI, different cell types are often mixed together without a clear decision boundary between cell types.

That is very much expected and nothing special for an unsupervised method. scVI doesn't use the labels at all. See the remark on an additional model comparison with a "simple classifier" above.

With a more classification-oriented benchmarking metrics, the silhouette coefficient might not be necessary to show anymore; but the authors shall handle that as they see fit.

MARS separates cells annotated as luminal epithelial cells by Tabula Muris into two different clusters (Fig. 3a).

This is obviously very interesting as it hints to meaningful learned features, a more rich representation than the original labels, and potential generalization properties.

Showing a single example, though, is not enough. Is there really just one additional cluster that is not explained by the labels? See the more concise formulation above.

We first investigate the endothelial cells, which appear in 11 tissues, and use thymus tissue as an unannotated experiment.

What is the train-test split for this?

Probabilities are assigned to landmarks in proportion to their probability density under Gaussian centered at a target unannotated cell type.

Also logisitic regression is a probabilistic classifier, but that doesn't mean that predicted class probabilities are useful – they might not be calibrated and domain confounding can completely hamper their usefulness.

With the current proposal, in which probability assignment is not even subject to optimizing the likelihood of the classifier, but implemented in a post-optimization ad-hoc step, I'd love to see a bit more explanation for why the predicted probabilities are useful. Are they calibrated? How do they relate to confidence intervals based on bootstrapping? What would an approximate Bayesian version look like (no need to implement anything)? How does this compare to the fully probabilistic approach of scANVI?
