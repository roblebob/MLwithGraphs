.# CS224W

[https://web.stanford.edu/class/cs224w/](https://web.stanford.edu/class/cs224w/)

[GRL_Book](https://www.cs.mcgill.ca/~wlh/grl_book/files/GRL_Book.pdf)

[youtube](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn)

<br>

_graph_

$\mathcal{G} = (\mathcal{V} , \mathcal{E}) \qquad with \quad \mathcal{E} \  \subset \ \ \mathcal{V} \times \mathcal{V} \ \ = \ \ \{ (u, v) \ \| \ u, v \in \mathcal{V}\}$

<br>

_adjacency matrix_

$\mathbf{A} \in \mathbb{R}^{ | \mathcal{V} |  \times  | \mathcal{V} |}$

<br>

_neighborhood_

$\mathcal{N}(u) = \left\{v \in \mathcal{V} \ \ : \ \ (u,v) \in \mathcal{E} \right\}$


<br>

### multi-relational graphs

having different _types_ $(\tau)$ of edges: &emsp; $(u,\tau,v) \in \mathcal{E}$

with an _adjacency matrix_ per edge type: &emsp; $\mathbf{A}_\tau$

summerizeds by an _adjacency tensor_: &emsp; $\mathcal{A} \in \mathbb{R}^{ | \mathcal{V} | \times | \mathcal{R} | \times | \mathcal{V} | }$

where $\mathcal{R}$ is the set of relations.

<br>

#### heterogeneous graphs

nodes imbued with _exlusive types_ $\implies$ partitioning into _disjoint sets_: &emsp;  $\mathcal{V} = \mathcal{V}_1 \cup \mathcal{V}_2 \cup \ldots \cup \mathcal{V}_k \qquad with \qquad \mathcal{V}_i \cap \mathcal{V}_j = \emptyset \ , \ \forall i \neq j$  

with edges constraint by those types,

e.g.:  certain edges only connect nodes of certain kinds: &emsp; $(u,\tau_i,v) \in \mathcal{E} \implies u \in \mathcal{V}_j, \ v \in \mathcal{V}_k$

special case: _multipartite graphs_, edges can only connect nodes of different type: &emsp; $j \neq k$


<br>

#### muliplex graphs

decomposed into a set of $k$ _layers_  (every node belongs to every layer)

each layer corresponding to a unique relation, representing the _intra-layer_ edge type for that layer

<img src="https://dl.acm.org/cms/attachment/5e4843b5-752f-4f60-b002-fb0292ac289c/www18companion-304-fig1.jpg" width="200">





<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>



### Node Classification


___homophily___ which is the tendency for nodes to share attributes with their neighbors in the graph

___structural  equivalence___ which is the idea that nodes with similar  local  neighborhood  structures  will  have  similar  labels

___heterophily___, which presumes that nodes will be preferentially connected to nodes with  different  labels

<br><br>

### Relation Prediction / Link Prediction / Graph Completion / Relational Inference

___given:___ &emsp; $\mathcal{V}\ ,\ \mathcal{E}_{train}$  &emsp;&emsp; with &emsp; $\mathcal{E}_{train} \subset \mathcal{E}$

___infer:___ &emsp; $\mathcal{E} \setminus \mathcal{E}_{train}$


<br><br>

### Clustering + Community-detection


<br><br>

### Graph classification, regression, and clustering







<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
## Example Medici

<img src="https://www.researchgate.net/profile/Stephen-Borgatti/publication/222538101/figure/fig4/AS:305206182072325@1449778232432/Padgetts-data-on-marriage-ties-among-Renaissance-Florentine-families-isolate-removed.png" width=666>
<br><br><br>
NOTE!!! -> edge between STROZZI and PERUZZI is hidden by the name STROZZI



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>


## Graph Statistics and Kernel Methods

### Node-level statistics and features

<br>

#### Node degree
$\displaystyle d_u = \sum_{v \in \mathcal{V}}\mathbf{A}[u,v]$

<br>

#### Node centrality

_eigenvector centrality_  
$\displaystyle e_{u} =  \frac{1}{\lambda} \sum_{v \in \mathcal{V}} \mathbf{A}[u,v] \ e_v \qquad \forall u \in \mathcal{V}$

$\lambda \mathbf{e} = \mathbf{A} \mathbf{e}$   

assuming: &ensp; $\forall u \in \mathcal{V}: e_u \geq 0 \implies \mathbf{e}$ is  that eigenvector with largest eigenvalue $\lambda$    

+ ranks the likelihood that a node is visited on a random walk of infinite length on the graph

<br>

#### Clustering Coefficient

$\displaystyle c_u = \frac{\left|  (v_1,v_2) \in \mathcal{E} \ : \ v_1, v_2 \in \mathcal{N}(u)  \right|}{ \binom{d_u}{2} }$







last --> page 18 (2.2.2 Global overlap measures)
