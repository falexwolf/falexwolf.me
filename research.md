Title: Research

In the past years, machine learning has started to help map, understand, and predict the molecular biology of single cells.

Before joining the field in 2015, I developed computational approaches to predict the emergent behavior of strongly correlated quantum materials, basic models of quantum computers, and chemical reactions in solar cells.

This page covers academic research only.

---

[TOC]

---

## Software for single-cell analytics and data management

[<img src="https://scanpy.readthedocs.io/en/latest/_static/Scanpy_Logo_BrightFG.svg" style="width: 120px; margin: 15px 10px 5px 0px"  align="left">](/publications#P23)
[Scanpy](https://scanpy.readthedocs.io) [[P23](/publications#P23)] is a scalable toolkit for analyzing single-cell gene expression data. Together with the underlying [anndata](http://anndata.readthedocs.org/) [[P33](/publications#P33)] it has become widely used and lead to an ecosystem of tools, with >600k downloads and >500 dependent repositories. It has been selected as an [*Essential Open Source Software for Science*](https://chanzuckerberg.com/newsroom/chan-zuckerberg-initiative-awards-5-million-for-open-source-software-projects-essential-to-science/) by CZI among [32 projects](https://chanzuckerberg.com/eoss/proposals/), alongside giants such as numpy, pandas, scikit-learn, matplotlib, and others. See [software](../software/).

{P33}

{P23}


## Dynamical modeling of RNA velocity

[<img src="../img/NatureBiotechCover2020-12.png" style="width: 120px; margin: 15px 20px 5px 0px"  align="left">](/publications#P28)
The introduction of RNA velocity in single cells has opened up new ways of studying cellular differentiation in scRNA-seq [[LaManno18](https://www.nature.com/articles/s41586-018-0414-6/)]. It describes the rate of gene expression change for an individual gene at a given time point based on the ratio of its spliced and unspliced mRNA. With [scVelo](https://scvelo.org), we solve the full transcriptional dynamics of splicing kinetics using a likelihood-based dynamical model to generalize RNA velocity to a wide variety of systems comprising transient cell states, which are common in development and in response to perturbations. With [Fabian Theis](https://scholar.google.de/citations?user=sqWpn2AAAAAJ).

{P28}


## Generative modeling of single-cell perturbation effects

[<img src="https://pbs.twimg.com/media/EAq3dqdUwAEQssP?format=jpg&name=900x900" style="width: 140px; margin: 15px 20px 5px 0px"  align="left">](/publications#P27)
We showed that generative models are able to predict single-cell perturbation responses out-of-distribution [[P27](/publications#P27)]. In principle, this approach should enable training models to predict the effects of disease and disease treatment across cell types and species. While the first implementation of the approach (scGen) relied on latent space vector arithmetics, we recently published an end-to-end-trained model based on a conditional variational autoencoder (trVAE) [[P29](/publications#P29)] and a deep factor model [[P32](/publications#P32)]. We wrote a review about the emerging field [[P31](/publications#P31)]. With [Fabian Theis](https://scholar.google.de/citations?user=sqWpn2AAAAAJ).

{P32}

{P31}

{P29}

{P27}


## Mapping the coarse-grained connectivity of complex manifolds

[<img src="https://pbs.twimg.com/media/D2FmvihWkAA9wmG?format=jpg&name=medium" title="Hematopoietic lineages as captured in scRNA-seq from Paul et al., Cell (2015). See [P26]." style="width: 250px; margin: 15px 10px 5px 0px"  align="left">](/publications#P24)
Partition-based graph abstraction (PAGA) aims to reconcile clustering with manifold learning by explaining variation using both discrete and continuous latent variables [[P26](/publications#P26)]. PAGA generates coarse-grained maps of manifolds with complex topologies in a computationally efficient and robust way. In [[P24](/publications#P24)], we used it to infer the first lineage tree of a whole complex animal - a [Science breakthrough](https://vis.sciencemag.org/breakthrough2018/) of the year 2018. It has been benchmarked as the overall best performing trajectory inference method in a review of ~70 methods by [Saelens *et al.* (Nat. Biotechn., 2019](https://www.nature.com/articles/s41587-019-0071-9)) [[tweet]](https://twitter.com/falexwolf/status/1113002674209873920). PAGA also builds on *diffusion pseudotime* [[P19]](/publications#P19), which defined a robust global measure of similarity among cells. With [Fabian Theis](https://scholar.google.de/citations?user=sqWpn2AAAAAJ).

{P26}

{P24}

{P19}


## Interpretable knowledge-enriched latent representations of scRNA-seq

[<img src="../img/p30.png" style="width: 140px; margin: 15px 10px 5px 0px"  align="left">](/publications#P30)

Existing methods for learning latent representations for single-cell RNA-seq data are based on autoencoders and factor models where the former are hard to interpret and the latter have limited flexibility. Here, we introduce a framework for learning interpretable autoencoders based on regularized linear decoders, decomposing variation into interpretable components using prior knowledge.

{P30}


## Reconstructing cell cycle and disease progression using deep learning

[<img src="../img/170712_featured_image_suggestion.png" title="Reconstructed cell cycle. See [P20]." style="width: 150px; margin: 15px 10px 5px 0px"  align="left">](/publications#P20) Using large-scale imaging data, we show how to reconstruct continuous biological processes using deep learning for the examples of cell cycle and disease progression in diabetic retinopathy [[P20](/publications#P20)]. See a [video](../blog/2017-09-10-deepflow). With [Fabian Theis](https://scholar.google.de/citations?user=sqWpn2AAAAAJ).

{P20}


## Deep-learning based diagnosis of lung cancer from images

[<img src="../img/dsb3-nodule_new.jpg" title="Lung CT scan with a marked nodule. Data from Data Science Bowl 2017 on Kaggle." style="width: 120px; margin: 15px 10px 5px 0px"  align="left">](https://www.kaggle.com/c/data-science-bowl-2017/leaderboard) The goal of the [Data Science Bowl 2017](http://www.datasciencebowl.com/about/) was to predict lung cancer from tomography scans. It was the highest endowed machine learning competition with $1M total in prize money in 2017. We won the [7th prize](https://www.kaggle.com/falexwolf) among [nearly 2.4k teams](https://datasciencebowl.com/about/) and more than 10k participants; the best result among all German teams.

{O7}


## Solving dynamical mean-field theory using tensor trains

[<img src="../img/dmft.png" title="Dynamical mean-field theory." style="width: 200px; margin: 15px 10px 5px 0px"  align="left">](/publications#O6)
[Tensor trains](https://en.wikipedia.org/wiki/Matrix_product_state) ([MPS](https://en.wikipedia.org/wiki/Matrix_product_state), [DMRG](https://en.wikipedia.org/wiki/Density_matrix_renormalization_group)) constitute - together with [quantum monte carlo](https://en.wikipedia.org/wiki/Quantum_Monte_Carlo) and the [numerical renormalization group](https://en.wikipedia.org/wiki/Numerical_renormalization_group) - the key numerical approach for tackling the exponential [computational complexity](https://en.wikipedia.org/wiki/Computability) of models of [strongly correlated materials](https://en.wikipedia.org/wiki/Strongly_correlated_material) and quantum computers.

We developed a way to use tensor trains within [dynamical mean-field theory](https://en.wikipedia.org/wiki/Dynamical_mean-field_theory) to enabable the simulation of previously inaccessible emergent properties of strongly correlated materials [[O6](/publications#O6),[P12-P18](/publications#P18)] - this worked to some degree, but turned out to be a hard problem. This is computational many-body physics at the interface of quantum information and field theory.
With [U. Schollwöck](https://scholar.google.de/citations?user=MYARbMAAAAAJ&hl=en) and [A. Millis](https://scholar.google.com/citations?user=ZVaMoP0AAAAJ&hl=en).

{O6}

{P18}

{P17}

{P16}

{P15}

{P14}

{P13}

{P12}


## Modeling diffusion-reaction chemistry of solar cells to improve conversion efficiency

The low energy conversion efficiency of established solar cells is largely due to chemical imperfections of the material at which excited photons recombine. While at Bosch research, I established models for material syntheses to optimize processes for the minimization of such imperfections [[O5](/publications#O5),[P8-P11](/publications#P11)]. Mathematically, these models reduce to diffusion-reaction equations. I wrote a proprietary software, which was productionized at Bosch Solar Energy. With [P. Pichler](https://scholar.google.de/citations?hl=en&user=Dh1sQ8wAAAAJ).

{O5}

{P11}

{P10}

{P9}

{P8}


## Dynamics of the quantum Rabi model

[<img src="../img/wolf12.png" title="Time evolution of photon excitation through entanglement with a quantum bit. From [P6]." style="width: 100px; margin: 15px 10px 5px 0px"  align="left">](/publications#P6)
The [quantum Rabi model](https://physics.aps.org/articles/v4/68) is the basic model for understanding decoherence of a Q-bit that is coupled to a bath, and in that sense a basic model for the technical foundations of quantum computing [[P6,P7](/publications#P7)]. By exploiting a recent exact solution of the static system, we established several dynamical properties, amonth others, Schroedinger-cat like states that show particular robustness towards decoherence. With [D. Braak](https://www.google.de/search?q=Integrability+of+the+Rabi+Model).

{P7}

{P6}


## Supercurrent through grain boundaries

[<img src="../img/grain-boundary.png" title="Grain boundary and super conductivity parameters of electrons." style="width: 120px; margin: 15px 10px 5px 0px"  align="left">](/publications#O4)
During studies, I focused on emergent properties of quantum-many body systems and their applications. Using a phenomenological theory of superconductivity (Bogoliubov de Gennes), we showed how [grain boundaries](http://dx.doi.org/10.1038/nphys1739) and strong correlations affect [high-temperature superconductivity](https://en.wikipedia.org/wiki/High-temperature_superconductivity) [[P5](/publications#P5)]. With [T. Kopp](https://www.physik.uni-augsburg.de/exp6/staff/kopp_t/).

{O4}

{P5}


## Coherent expansions of quantum matter and matter wave lasers

[<img src="../img/jreissaty12.png" title="Expanding cloud of coherent atoms - a 'matter laser' - in a 2d lattice. From [P4]." style="width: 100px; margin: 15px 10px 5px 0px"  align="left">](/publications#P4)
Collapse and revival oscillations and coherent expansions have been suggested for realizing matter-wave lasers. The following two projects [[P2,P4](/publications#P4)] provided first in-depth models in one- and two-dimensional lattices. With [M. Rigol](https://scholar.google.com/citations?user=MeS-yJgAAAAJ).

{P4}

{P2}


## Relaxation of a quantum many-body system after perturbation

We investigated the non-equilibrium behavior of quantum many-body systems [[P1-P4](/publications#P4)], in particular, the fundamental problem of how such systems transition from an excited state to equilibrium. This happens through chaotic dynamics in the classical case, but is an active area of research in the [quantum case](http://dx.doi.org/10.1038/nature06838). We showed that the transition proceeds through an intermediate, prethermalized, plateau for which we developed a statistical theory. I contributed the central analytical calculation [[T1](../talks/#T1)] to the highly cited paper [[P3](/publications#P3)] during a summer lab project. With [M. Kollar](http://myweb.rz.uni-augsburg.de/~mkollar/).

{P3}

{P1}


## Sartre at Stammheim

[<img src="../img/sartre_a_stammheim.jpg" title="Sartre in Stammheim. From [O1], original from H. M. Schleyer: RAF Geschichte." style="width: 100px; margin: 15px 10px 5px 0px"  align="left">](/publications#O1)
During high school, I tried to gain a better understanding of how philosophical and political ideas stimulate change in society and culture. In my thesis, I investigated why J.-P. Sartre publicly supported the German terrorist group RAF upon his visit in Stammheim in 1974 [[O1](/publications#O1)]. For more context, see [Der Spiegel (2013)](http://www.spiegel.de/spiegel/print/d-90848693.html).

{O1}
