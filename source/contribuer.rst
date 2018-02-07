Contribuer
==========

Principe
########

Le contenu de ce site est généré à partir de fichiers .rst permettant :

* De ne pas toucher à la mise en page
* De pouvoir écrire des formules en LaTeX
* De pouvoir afficher du code formaté avec `Pygments <http://pygments.org/>`_
* De pouvoir, par exemple, afficher le schéma matplotlib correspondant au code qui l'a généré


Le format .rst (reStructuredText) est décrit rapidement dans ce `Quickref <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_


Editer les pages
################

Vous pouvez directement éditer les pages via `Github <https://github.com/FutureIsTech/Data-Science>`_ (et effectuer une Pull/Request) afin de modifier les pages existantes mais vous pouvez aussi proposer d'en ajouter.

Toute correction, ajout ou modification est la bienvenue.


Vous pouvez aussi proposer des modifications du template Sphinx pour améliorer l'ergonomie du site.


Guidelines
##########

* Le contenu doit être en Français mais nous acceptons les termes communs en anglais comme "Data Science", "features", "kernels"... tant qu'ils sont définis dans `Les Bases </les_bases.html>`_ ou dans 
* Une page sur une notion doit respecter une certaine forme:

  * Elle doit commencer par les 'requirements': c'est à dire ce que le lecteur a besoin de connaitre avant de pouvoir comprendre cette page. Si possible renvoyer vers d'autres pages du site dans "Les Bases"
  * Elle doit, dans un premier temps, vulgariser le concept, il s'agit d'expliquer concrètement à quoi sert ce modèle et comment il marche. Dans un deuxième temps, la page expliquera en détails son fonctionnement.
  * Elle doit présenter un exemple visuel (avec du code Python)
  
Possibilités offertes par Sphinx
################################

Par exemple on peut afficher du code avec Pygments:

.. code-block:: python3

   for e in bb.stream_single():
      print(e)
   print("Hello world")
   ...



.. plot::

    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np

    # This example demonstrates mplot3d's offset text display.
    # As one rotates the 3D figure, the offsets should remain oriented
    # same way as the axis label, and should also be located "away"
    # from the center of the plot.
    #
    # This demo triggers the display of the offset text for the x and
    # y axis by adding 1e5 to X and Y. Anything less would not
    # automatically trigger it.

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.mgrid[0:6*np.pi:0.25, 0:4*np.pi:0.25]
    Z = np.sqrt(np.abs(np.cos(X) + np.cos(Y)))

    surf = ax.plot_surface(X + 1e5, Y + 1e5, Z, cmap='autumn', cstride=2, rstride=2)
    ax.set_xlabel("X-Label")
    ax.set_ylabel("Y-Label")
    ax.set_zlabel("Z-Label")
    ax.set_zlim(0, 2)

    plt.show()