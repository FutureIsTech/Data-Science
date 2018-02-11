Probabilités et Statistiques
============================


Les variables aléatoires
------------------------



Les différents types de variable aléatoire (v.a.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/types_de_variable.png

On distingue deux catégories de v.a. :

* Qualitatives: Variable portant sur des grandeurs non numériques

  * Nominales : v.a. correspond à des noms sans ordre précis
  * Ordinales : v.a. possédant un ordre

* Quantitatives : Variable portant sur des grandeurs numériques
   
  * Discrètes : v.a. dont les valeurs sont énumérables
  * Continues : v.a. dont les valeurs sont tellement nombreuses qu’elles en deviennent non-énumérable


Espérance (ou moyenne) :math:`\mathbb{E}(X)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C'est la valeur moyenne que prend un v.a.. On note généralement :math:`\mathbb{E}(X) = \overline{x}`.

* Pour une v.a. discrète : :math:`\mathbb{E}(X) = \sum_{i=1}^{+\inf}{x_i p_i}`
* Pour une v.a. continue : :math:`\mathbb{E}(X) = \int_{-\inf}^{+\inf}{xf(x)}`


Variance :math:`V(X)` :
~~~~~~~~~~~~~~~~~~~~~~~

Valeur indiquant la manière dont se disperse la série statistique autour de sa moyenne. Plus la variance est élevée, plus les valeurs de la série sont écartées les unes des autres.

* Pour une v.a. discrète : :math:`V(X) = \sum_{i=1}^{k}{(x_i-\overline{x}) p_i}`
* Pour une v.a. continue : :math:`V(X) = \int{(x-\overline{x})^2f(x)dx}`


Ecart type :math:`\sigma_X` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Valeur indiquant la manière dont se disperse la série statistique autour de sa moyenne. Plus l’écart type est faible, plus les valeurs de la série sont regroupées autour de la moyenne. L’écart type est égal à la racine carré de la variance.

* Formule générale : :math:`\sigma_X=\sqrt{\mathbb{E}[(X-\mathbb{E}(X)]^2}=\sqrt{\mathbb{E}(X^2)-\mathbb{E}(X)^2}`
* Pour une v.a. continue : :math:`\sigma_X=\sqrt{\sum_{i=1}^{k}{(x_i-\overline{x}) p_i}}`
* Pour une v.a. discrète : :math:`\sigma_X=\sqrt{\int{(x-\overline{x})^2f(x)dx}}`


Covariance :math:`\operatorname{Cov}(X,Y)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entre plusieurs v.a., permet de quantifier leur écarts conjoints par rapport à leurs espérances respectives.

* Pour deux v.a. : :math:`\operatorname{Cov}(X,Y)=\mathbb{E}[(X-\overline{X})(Y-\overline{Y})]=\frac{1}{N}\sum_{i=1}^{N}{(X-\overline{X})(Y-\overline{Y})}`

Pour généraliser à N VA, on peut construire la **matrice de covariance** notée :math:`\Sigma`. Ici, on prend X_i comme étant la v.a. :math:`i` avec :math:`i \in N` :

.. math::

   \Sigma = \begin{bmatrix}\operatorname{Cov}(X_1,X_1) & \ldots & \operatorname{Cov}(X_N,X_1)\\ \vdots & \ddots & \vdots \\ \operatorname{Cov}(X_1,X_N) & \ldots & \operatorname{Cov}(X_N,X_N)\end{bmatrix}


Or, :math:`\operatorname{Cov}(X,X) = V(X)`, d'où :

.. math::

   \Sigma = \begin{bmatrix}V(X_1) & \ldots & \operatorname{Cov}(X_N,X_1)\\ \vdots & \ddots & \vdots \\ \operatorname{Cov}(X_1,X_N) & \ldots & V(X_N)\end{bmatrix}




Corrélation :math:`\operatorname{Cor}(X,Y)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entre plusieurs v.a., permet de mesurer l'intensité de la relation pouvant exister entre elles.

* Pour deux v.a. : :math:`\operatorname{Cor}(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y}`

Pour généraliser à N VA, on peut construire la **matrice de corrélation** notée :math:`r`. Ici, on prend X_i comme étant la v.a. :math:`i` avec :math:`i \in N` :

.. math::

   r = \begin{bmatrix}\operatorname{Cor}(X_1,X_1) & \ldots & \operatorname{Cor}(X_N,X_1)\\ \vdots & \ddots & \vdots \\ \operatorname{Cor}(X_1,X_N) & \ldots & \operatorname{Cor}(X_N,X_N)\end{bmatrix}

Or, :math:`\operatorname{Cor}(X,X) = 1`, d'où :

.. math::

   \Sigma = \begin{bmatrix}1 & \ldots & \operatorname{Cor}(X_N,X_1)\\ \vdots & \ddots & \vdots \\ \operatorname{Cor}(X_1,X_N) & \ldots & 1\end{bmatrix}


Homo/Hétéro - scédasticité :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour chaque variable observée, leur variance est soit hétérogène, soit homogène.

TODO

Théorème de Bayes :
~~~~~~~~~~~~~~~~~~~

Dans le cas binomial :
^^^^^^^^^^^^^^^^^^^^^^

.. math::

   \mathbb{P}\left(A|B\right) = \frac{\mathbb{P}\left(B|A\right)\mathbb{P}\left(A\right)}{\mathbb{P}\left(B\right)} \equiv posterior = \frac{likelihood * prior}{evidence}

* :math:`posterior = \mathbb{P}\left(A|B\right) = probabilité à posteriori de A sachant B`
* :math:`likelihood = \mathbb{P}\left(B|A\right) = vraisemblance de A`
* :math:`prior = \mathbb{P}\left(A\right) = probabilité à priori de A`
* :math:`evidence = \mathbb{P}\left(B\right) = probabilité à priori de B`