# Project Overview

Pollution statistics are usually largely available online in government websites of different countries. On a surface level this data is not very useful but with the correct algorithms and visualisations it is possible to draw meaningful inferences from them.

Here K-means clustering algorithm is implemented to cluster the data of ambient air pollution levels accross differnet cities in India. All data is authentic from the official Indian govenment data website.

The algorithm used euclidean shortest distance to assign the data points their corresponding centroids. The algorithm was implemented from scatch. Moreover all the core functions are unittested for proper functioning.

*Methodology used* : Python datastructures and visualisation modules

# Installation for Mac

```bash
>> brew install python3
```

```bash
>> pip3 install constant
```

```bash
>> pip3 install numpy
```

```bash
>> pip3 install matplotlib
```

Numpy and matplotlib are used for the visualisation of the data points on clustering.

Download python notebook or anaconda navigator package from [here](https://www.anaconda.com/)

## POLLUTION INPUT DATA FILES URL

[AmbientAirQualityData](https://data.gov.in/catalog/ambient-air-quality-respect-particulate-matter-under-national-air-quality-monitoring)


## Script to parse wikepedia file
cat wikepedia_screen_scrape.txt  | grep '[0-9]'|grep -v '^(' | grep -v '[0-9]*to[0-9]*' | awk -F ' ' '{print "\"" $2 "\":\"" $3 "\","}' >> city_population.json

## Architecture

![](images/kmeans_arch.png)

## Output sample

![](images/kMeansOutput.png)
![](images/1.png)

## Project Report:

Click [here](ProjectReport.pdf) to view final report
