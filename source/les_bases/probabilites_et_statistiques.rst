Probabilités et Statistiques
============================


Les variables aléatoires
------------------------



Les différents types de variable aléatoire (VA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On distingue deux catégories de VA :

* Qualitatives: Variable portant sur des grandeurs non numériques

  * Nominales : VA correspond à des noms sans ordre précis
  * Ordinales : VA possédant un ordre

* Quantitatives : Variable portant sur des grandeurs numériques
   
  * Discrètes : VA dont les valeurs sont énumérables
  * Continues : VA dont les valeurs sont tellement nombreuses qu’elles en deviennent non-énumérable

.. image:: img/types_de_variable.png


Espérance (ou moyenne) :math:`\mathbb{E}(X)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C'est la valeur moyenne que prend un VA. On note généralement :math:`\mathbb{E}(X) = \overline{x}`.

* Pour une VA discrète : :math:`\mathbb{E}(X) = \sum_{i=1}^{+\inf}{x_i p_i}`
* Pour une VA discrète : :math:`\mathbb{E}(X) = \int_{-\inf}^{+\inf}{xf(x)}`

Variance :math:`V(X)` :
~~~~~~~~~~~~~~~~~~~~~~~

Valeur indiquant la manière dont se disperse la série statistique autour de sa moyenne. Plus la variance est élevée, plus les valeurs de la série sont écartées les unes des autres.

* Pour une VA discrète : :math:`V(X) = \sum_{i=1}^{k}{(x_i-\overline{x}) p_i}`
* Pour une VA discrète : :math:`V(X) = \int{(x-\overline{x})^2f(x)dx}`



Ecart type :math:`\sigma_X` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Valeur indiquant la manière dont se disperse la série statistique autour de sa moyenne. Plus l’écart type est faible, plus les valeurs de la série sont regroupées autour de la moyenne. L’écart type est égal à la racine carré de la variance.





Covariance :math:`\operatorname{Cov}(X,Y)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

    \operatorname{Cov}(X,Y)


Corrélation :math:`\operatorname{Cor}(X,Y)` :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Homo/Hétéro - scédasticité :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Théorème de Bayes :
~~~~~~~~~~~~~~~~~~~


