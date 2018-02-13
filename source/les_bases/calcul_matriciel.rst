Calcul matriciel
================


Notations
~~~~~~~~~


Scalaire ou Matrice ?
---------------------

On notera les scalaires en minuscule et les matrices en majuscule.


Taille d'une matrice
--------------------

.. math:

   M_{3,2} = \begin{bmatrix}a & b\\ c & d \\ e & f\end{bmatrix}


* Cette matrice :math:`M_{3,2}` contient 3 lignes et 2 colonnes, on dira qu'elle est de taille 3x2 et non pas 2x3.


Comment parler d'un élément spécifique dans la matrice ?
--------------------------------------------------------

Pour une matrice :math:`M`, l'élément à la ligne :math:`i` et à la colonne :math:`j` se trouve à :math:`(M_{i,j})` (avec les parenthèses pour ne pas confondre avec la taille d'une matrice).



Définitions
~~~~~~~~~~~

Propriétés des matrices
-----------------------

* :math:`PDP^{T}=P^{T}DP` où :math:`D` :pink:`est une matrice des valeurs propres et P une matrice des vecteurs propres`
* Associativité : :math:`A*(B*C)=(A*B)*C`
* Distributivité : :math:`A*(B+C)=A*B+A*C`
* Distributivité : :math:`(A+B)*C=A*C+B*C`
* :math:`c(A*B)=(cA)*B=A*(cB)`


Matrice **creuse** (ou **sparse** matrix)
-----------------------------------------

Se dit d'une matrice qui contient beaucoup de zéros. Elle peut donc être compressée en utilisant une structure de données appropriée.


Matrice **pleine** (ou **dense** matrix)
----------------------------------------

Se dit d’une matrice dont toutes les composantes (cases) sont utilisées.


Matrice **nulle**
-----------------

Se dit d'une matrice dont tous les coefficients sont nuls.


.. math:

   M = \begin{bmatrix}0 & \ldots &  0\\ \vdots & \ddots & \vdots \\ 0 & \ldots & 0\end{bmatrix}



Matrice **carrée**
------------------

Se dit d'une matrice qui dispose du même nombre de lignes que de colonnes.


Matrice **diagonale** (!= matrice diagonalisable)
-------------------------------------------------

Se dit d'une matrice carrée nulle sauf sur sa diagonale.

.. math:

   D = \begin{bmatrix}42 & 0 &  0\\ 0 & -36 & 0 \\ 0 & 0 & -2i\end{bmatrix} = diag(42, -36, -2i)


Matrice **identité**, notée :math:`I`
-------------------------------------

Se dit d’une matrice carrée de taille supérieur à 1, avec des 1 sur sa diagonale et des 0 partout ailleurs.

.. math:

   I = \begin{bmatrix}1 & \ldots &  0\\ \vdots & \ddots & \vdots \\ 0 & \ldots & 1\end{bmatrix} = diag(1, ..., 1)

Pour une matrice identité de taille 2, on pourra la noter :math:`I_2`.

.. math:

   I_2 = \begin{bmatrix}1 & 0\\ 0 & 1\end{bmatrix} = diag(1, 1)


La matrice identité dispose d'une propriété interessante (:pink:`TODO: la définir`) :

.. math:

   A_{2,3} = \begin{bmatrix}a & b & c \\ d & e & f\end{bmatrix} = \begin{bmatrix}1 & 0 \\ 0 & 1 \end{bmatrix}*\begin{bmatrix}a & b & c \\ d & e & f\end{bmatrix} = \begin{bmatrix}a & b & c \\ d & e & f\end{bmatrix} * \begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}


Matrice de passage
------------------

:pink:`TODO`


Matrice transposée, notée :math:`U^{T}`
---------------------------------------

C'est une transformation transposant une matrice par rapport à sa diagonale.

.. math:

   \textrm{Si } U = \begin{bmatrix}1+i & 1 & i-2 \\ 2 & 4 & 1 \\ 3 & -i & i\end{bmatrix}\textrm{alors } U^{T} = \begin{bmatrix}1+i & 2 & 3 \\ 1 & 4 & -i \\ i-2 & 1 & i\end{bmatrix}


.. math:

   \textrm{Si } U = \begin{bmatrix}1 & 2 \\ 3 & 4 \\ 5 & 6\end{bmatrix}\textrm{alors } U^{T} = \begin{bmatrix}1 & 3 & 5 \\ 2 & 4 & 6\end{bmatrix}

On a donc :math:`(M_{i,j})=(M_{j,i})`