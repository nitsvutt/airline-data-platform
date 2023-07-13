# Airline Data Platform

![license](https://img.shields.io/github/license/nitsvutt/airline-data-platform)
![stars](https://img.shields.io/github/stars/nitsvutt/airline-data-platform)
![forks](https://img.shields.io/github/forks/nitsvutt/airline-data-platform)

## Abstract

This project is a data platform solution for my previous contribution with my partners at **COMNETSAT** called *A Practical Real-time Flight Delay Prediction System using Big Data Technology*<sup>[[1]](#references)</sup>. With a bounded resources and research purpose only, the following architecture is a first look to the problem so I only utilize very common technologies (most of them are open-source) to develop the platform, including Apache Kafka, Apache Cassandra, Apache Spark, Apache Airflow, Google Bigquery and Metabase. However, the platform still operate well with about 225.000 (rows/batch) batch ingestion throughput or approximately 10.000 (rows/s) streaming ingestion throughput with an acceptable overall latency.

## Introduction

In recent years, **The Bureau of Transportation Statistics (BTS)** under **The United States Department of Transportation** has recorded a considerable decrease in the on-time performance of the majority of airlines, thereby, these airlines also experienced a moderate fall in the revenue. Based on a thorough analysis, they have determined that customer services, including flight delay, significantly contribute to this decline. As a result, they really want to be offered an insightful flight delay report from **BTS** for analytical purpose. Assume that I work as a Data Engineer of **BTS** and my responsibility is to design a data platform to collect, process, store, and build required dashboards to embed to their apps or periodically send it to their emails.

## Dataset

This dataset was extracted from *The Reporting Carrier On-Time Performance (1987-present)* table of *The On-Time Database* collected by **BTS**. It contains 109 columns and more than 5M records per year. With a limited resource (1 machine with an Apple Silicon chip 8-core CPU and 8GB RAM), I only practice with 61 columns and 10.683.751 rows of data, concentrating on flight delay, of the year 2020 and 2021. The metadata are available [here](https://github.com/nitsvutt/airline-data-platform/blob/main/extracted-data/metadata/metadata.html).

## Methodology

To cope with this problem, my data platform architecture include an Ingestion layer, a Staging layer, a Processing layer, a Integration & Storage layer, and an Analysis & User Inteface layer. The process begins with data ingested from separate sources by Ingestion layer and then stored into the Staging layer. After that, the Processing & Integration layer will extract data from the Staging layer, transform, integrate, and load it into the Storage layer. Finally, end users are able to interact with ready-to-use data in the Analysis & User Inteface layer. The following design illustrates the paticular architecture:

<p align="center">
  <img src="https://github.com/nitsvutt/airline-data-platform/blob/main/asset/architecture.png" width="75%" title="architecture" alt="architecture">
</p>

On the source side, I implement a relational database, MySQL, and a document-based database, MongoDB, to simulate more available sources which the platform can ingest from. On the platform side, Apache Airflow serves as a workflow scheduler and orchestrator for the entire data journey on the platform. Begin with Ingestion layer, I deploy Apache Kafka (with Docker) for streaming ingestion and Apache Spark for batch ingestion. Apache Spark can also be used as a processing tool for Apache Kaka output, however, it requires your Apache Kafka service must be very durable. In the persistent Staging layer (which can also be temporary), or Data Lake, wide-column based database named Apache Cassandra is usually a good choice due to its highly write and read performance. At the subsequent layer, Processing layer, Apache Spark is one of the most efficient solution. Having been processed, data is then integrated into Google Bigquery, a high scalable columnar Data Warehouse. Finally, an easy-to implement and use BI tool called Metabase will help end-users can easily interact with the data.

## Results

The data platform is able to batch ingest 225.000 (rows/batch) with a permissible delay or stream ingest around 10.000 (rows/s), in fact, the throughput depends on your data size intead of number of rows. Additionally, the platform offers Data Analysts a friendly interface to analyze quality data, build reports and schedule to send them to the airlines. In this case, I also take responsible for this work, the 2 following dashboards are examples, one is the *All Airlines Report* for the **BTS** manager and another is the *9E Airline Report* for the **9E airline**:
<ul>
  <li>
    <a href="https://www.youtube.com/embed/PNkLthUdQus?autoplay=1&loop=1&playlist=PNkLthUdQus">All airlines - Flight delay report</a>
  </li>
  <li>
    <a href="https://www.youtube.com/embed/SlJLrqRsKXs?autoplay=1&loop=1&playlist=SlJLrqRsKXs">9E airline - Flight delay report</a>
  </li>
</ul>

## Discussion

On the one hand, the carriers can get very informative insights about the delay of their flights to initiate research and take necessary actions. On the other hand, they are unable to address the issue immediately, necessitating the implementation of temporary measures to improve their services. One recommendation I propose is that they should build a Machine Learning model to accurately forecast flight delays, enabling swift and informed decision-making.

## Conclusion

In conclusion, this project serves as an research endeavor in standalone mode. In order to deal with the practical problem, it is necessary to have additional resources to deploy a more powerful platform. And as I mentioned before, a Machine Learning model will be highly benefical in handle the recent state.

## Acknowledgments

Although the project is my own contribution, I am still grateful to my previous partners, **Minh-Tri Vo**, **Duc-The Pham**, and lecturer, **Trong-Hop Do** for the original ideas.

## References

<sup>[1]</sup> M. -T. Vo, T. -V. Tran, D. -T. Pham and T. -H. Do, "A Practical Real-Time Flight Delay Prediction System using Big Data Technology," 2022 IEEE International Conference on Communication, Networks and Satellite (COMNETSAT), Solo, Indonesia, 2022, pp. 160-167, doi: 10.1109/COMNETSAT56033.2022.9994427.
