<!-- omit in toc -->
# Table of Contents
- [Introduction](#introduction)
- [Infrastructure](#infrastructure)
- [Future Research](#future-research)


<br />

# Introduction

The directory is about the API of the [fintech product](https://github.com/CWJ-K/fintech_product).

<br />


# Infrastructure
![infrastructure](infrastructure.JPG)

* Use Docker Swarm to build services to
  * monitor services
  * isolate the environment of services
* Scrape websites from Taiwan Stock Exchange, Taipei Exchange and Taiwan Futures Exchange in the ETL process
* Services are currently built in the same machine
* Use redash and API to see data
* Apply CI/CD into the web crawler and web API


<br />

# Future Research
* To schedule tasks in Airflow, instead of apscheduler
  * Airflow provides a good UI to see the conditions of tasks.
* Complete the tasks in Celery and rabbitMQ
* Distribute services to different machines