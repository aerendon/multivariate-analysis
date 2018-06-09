# multivariate-analysis

# Reto Wisconsin Diagnostic Breast Cancer (WDBC)

## Descripcion

El [Wisconsin Diagnostic Breast Cancer (WDBC) dataset](http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) es un conjunto de datos de características de imagenes de lunares cancerigenos o no.

Este dataset contiene alrededror de 500 muestras de características extraidas de lunares para determinar cancer de piel. 

El dataset esta distribuido de la siguiente forma:

* Label (B: 0, M: 1)
* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness (perimeter^2 / area - 1.0)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry 
* fractal dimension ("coastline approximation" - 1)

## Conclusión

Caracteristicas significativas que representan importancia a la hora de decidir si un lunar es maligno:

```
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
texture          0.3777      0.063      5.977      0.000       0.254       0.502
area             0.0475      0.010      4.685      0.000       0.028       0.067
smoothness       74.4357     30.948      2.405      0.016      13.779     135.092
compactness      2.4326     19.004      0.128      0.898     -34.815      39.681
concavity        7.4069      7.713      0.960      0.337      -7.711      22.524
concave points   70.1621     27.678      2.535      0.011      15.913     124.411
symmetry         15.1245     10.345      1.462      0.144      -5.150      35.399
```

___

## Más información

* https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
* [Wisconsin Diagnostic Breast Cancer (WDBC) dataset](http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)
* [Colomb-ia](https://github.com/jcvasquezc/supervised-cancer)