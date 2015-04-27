# dd: data diff

usage:

```
./csv_to_triples.py iris.csv
## ('69', 'petal width (cm)', '1.1')
## ...
```

Yadda yadda yadda... Check this out though:

```
./csv_diff.py iris.csv iris_one_change.csv
## < ('7', 'petal length (cm)', '1.5')
## ---
## > ('7', 'petal length (cm)', '1.6')
```

Compare with:

```
diff iris.csv iris_one_change.csv
## 9c9
## < 7,5.0,3.4,1.5,0.2,setosa
## ---
## > 7,5.0,3.4,1.6,0.2,setosa
```
