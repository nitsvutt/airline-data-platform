# Airline Data Platform

## Abstract

This project is a data platform solution for my previous contribution with my partners at [COMNETSAT](https://comnetsat.org/) called [A Practical Real-time Flight Delay Prediction System using Big Data Technology](https://ieeexplore.ieee.org/document/9994427). With a bounded resource and research purpose only, the following architecture is a first look to the prolem so I only utilize very common technologies (most of them are open-source) to develop the platform including Apache Kafka, Apache Cassandra, Apache Spark, Apache Airflow, Google Cloud Bigquery and Metabase. However, the platform still operate well with ~5,1M row (~2,1GB) of data comming at the same time.

## Introduction

In recent years, [The Bureau of Transportation Statistics (BTS)](https://www.bts.gov/) under [The United States Department of Transportation](https://www.transportation.gov/) has recorded a considerable decrease in the on-time performance of the majority of airlines. These airlines also experienced a moderable decline in the revenue so they really want to be offered an insightful flight delay report from BTS for analytical purposes. Assume that I work as a Data Engineer of BTS and my responsibility is to design a data platform to collect, process, store, build required dashboards and send it to their emails.

Currently, my data platform architecture include an Ingestion layer, a Staging layer, a Processing & Integration layer, a Storage layer, a Pipeline layer and an Analysis & User Inteface layer. The process begins with data ingested from separate sources by Ingestion layer and then stored into the Staging layer. After that, the Processing & Integration layer will extract data from the Staging layer, transform, integrate, and load it into the Storage layer. During this stage, the Pipeline layer will support the Processing & Integration layer devide tasks, implement, schedule and maintain the workflow. Finally, end users are able to interact with ready-to-use data in the Analysis & User Inteface layer.

## Dataset

This dataset was extracted from the Reporting Carrier On-Time Performance (1987-present) table of the "On-Time" database collected by [The Bureau of Transportation Statistics (BTS)](https://www.bts.gov/). It contains 109 columns and more than 5M records per year. With a limited resource (1 machine with 8-core CPU and 8GB RAM), I only practice with 61 columns concentrating on flight delay of the year 2020. The metadata are available [here](https://github.com/nitsvutt/airline-data-platform/blob/main/extracted-data/metadata/metadata.html).

## Results

Present the results of the project, including any analysis, visualizations, or statistical findings. Highlight key observations or trends.

<a href="https://www.youtube.com/embed/PNkLthUdQus?autoplay=1&loop=1&playlist=PNkLthUdQus">
  All airlines - Flight delay report
</a>
</br>
<a href="https://www.youtube.com/embed/SlJLrqRsKXs?autoplay=1&loop=1&playlist=PNkLthUdQus">
  9E airline - Flight delay report
</a>

## Discussion

Discuss the implications of the results and their significance. Analyze the strengths and limitations of the approach and provide insights into potential future directions.

## Conclusion

Summarize the main findings of the project and reiterate its importance. Discuss any potential applications or further research opportunities.

## Acknowledgments

The project is my own contribution, but I am still grateful to my previous partners, [Minh-Tri Vo](https://ieeexplore.ieee.org/author/37089674394), [Duc-The Pham](https://ieeexplore.ieee.org/author/37089673640), and lecturer, [Trong-Hop Do](https://ieeexplore.ieee.org/author/38468172800) for the original ideas.

## References

[1] M. -T. Vo, T. -V. Tran, D. -T. Pham and T. -H. Do, "A Practical Real-Time Flight Delay Prediction System using Big Data Technology," 2022 IEEE International Conference on Communication, Networks and Satellite (COMNETSAT), Solo, Indonesia, 2022, pp. 160-167, doi: 10.1109/COMNETSAT56033.2022.9994427.

## License

Specify the license under which the project is distributed, if applicable.
