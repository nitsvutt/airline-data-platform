# Airline Data Platform

## Abstract

This project is a data platform solution for my previous contribution with my partners at [COMNETSAT](https://comnetsat.org/) called [A Practical Real-time Flight Delay Prediction System using Big Data Technology](https://ieeexplore.ieee.org/document/9994427). With a limited resources, the following architecture is a first look to the prolem so I just utilize very common technologies (most of them are open-source) to develop the platform including Apache Kafka, Apache Cassandra, Apache Spark, Apache Airflow, Google Cloud Bigquery and Metabase. However, the platform still operate well with ~5,1M row (~2,1GB) of data comming at the same time.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [References](#references)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Introduction

In recent years, [The Bureau of Transportation Statistics (BTS)](https://www.bts.gov/) under [The United States Department of Transportation](https://www.transportation.gov/) has recorded a considerable decrease in the on-time performance of the majority of airlines. These airlines also experienced a moderable decline in the revenue so they really want to be offered an insightful flight delay report from BTS for analytical purposes. Assume that I work as a Data Engineer of BTS and my responsibility is to design a data platform to collect, process, store, build required dashboards and send it to their emails.

Currently, my data platform architecture include an Ingestion layer, a Staging layer, a Processing & Integration layer, a Storage layer, and an Analysis & User Inteface layer connected by a Pipeline layer. The process begins with data ingested from separate sources by Ingestion layer and then stored into the Staging layer. After that, the Processing & Integration layer will extract data from the Staging layer, transform, integrate, and load it into the Storage layer. During this stage, the Pipeline layer will support the Processing & Integration layer devide tasks, implement, schedule and maintain the workflow. Finally, end users are able to interact with ready-to-use data in the Analysis & User Inteface layer.

## Methodology

Explain the methodology or approach used to address the research problem or achieve the project goal. Include details about data collection, experimental setup, algorithms, or techniques employed.

## Results

Present the results of the project, including any analysis, visualizations, or statistical findings. Highlight key observations or trends.

## Discussion

Discuss the implications of the results and their significance. Analyze the strengths and limitations of the approach and provide insights into potential future directions.

## Conclusion

Summarize the main findings of the project and reiterate its importance. Discuss any potential applications or further research opportunities.

## References

List any references or sources used in the project, following a specific citation format (e.g., APA, IEEE, etc.).

## License

Specify the license under which the project is distributed, if applicable.

## Authors

List the names or usernames of the project contributors.

## Acknowledgments

Acknowledge any individuals, organizations, or resources that provided support, guidance, or inspiration for the project.


<a href="https://www.youtube.com/embed/PNkLthUdQus?autoplay=1&loop=1&playlist=PNkLthUdQus">
  All airlines - Flight delay report
</a>
</br>
<a href="https://www.youtube.com/embed/SlJLrqRsKXs?autoplay=1&loop=1&playlist=PNkLthUdQus">
  9E airline - Flight delay report
</a>
