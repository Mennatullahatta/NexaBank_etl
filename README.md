Thanks for your patience. Here's your **entire `README.md` as one continuous text block** — **no code fences**, no interruptions, no markdown fences — just a single copy-paste-ready chunk you can drop directly into your `README.md` file:

---

# NexaBank ETL Pipeline

This project implements a scalable, modular ETL pipeline designed for banking and transactional data. It uses a multithreaded producer-consumer pattern to monitor new data files, validate them, transform the data, and load it efficiently into a data lake in Parquet format and HDFS.

## 📚 Table of Contents

* [🚀 Key Features](#-key-features)
* [🧠 Architecture Overview](#-architecture-overview)
* [📁 Project Structure](#-project-structure)
* [🛠️ How It Works](#️-how-it-works)
* [📦 Supported Input Formats](#-supported-input-formats)
* [📄 Logging & Notifications](#-logging--notifications)
* [✅ Run the ETL System](#-run-the-etl-system)
* [📬 Email Alerts](#-email-alerts)
* [📂 HDFS Integration](#-hdfs-integration)
* [👥 Contributors](#-contributors)
* [📃 License](#-license)

## 🚀 Key Features

* 🔄 Producer-Consumer Design Pattern using Python Queue and multithreading
* 📂 File Monitor thread watches for incoming files and enqueues them
* 🏗️ Pipeline thread dequeues files and:

  * Extracts raw data
  * Validates against a defined schema
  * Filters already-processed data using a state\_store
  * Transforms data using appropriate transformer modules
  * Loads data into Parquet + HDFS (via subprocess)
* ✅ Schema validation and stateful deduplication
* 📬 Failure alerts via email
* 📜 Full logging system using a custom Logger

## 🧠 Architecture Overview

File Monitor Thread → puts file path → Shared Queue → picked up by Pipeline Thread
Pipeline steps:

1. Extract
2. Validate
3. Check state\_store
4. Transform
5. Save as Parquet
6. Upload to HDFS
7. Log + Send email on failure

## 📁 Project Structure

src/
├── file\_monitor/ → file\_monitor.py (watches and queues files)
├── pipeline/
│   ├── main.py (starts both threads)
│   ├── pipeline.py (ETL logic)
│   ├── extractors/
│   ├── validators/
│   ├── transformers/
│   ├── loaders/
│   ├── logger/
│   ├── notifier/
│   ├── state\_store/
│   └── support/

## 🛠️ How It Works

The system consists of two main threads:

**1. File Monitor (Producer)**

* Monitors a directory for new files
* Pushes file paths into a shared queue

**2. Pipeline (Consumer)**

* Dequeues a file path
* Extracts data using the appropriate extractor
* Validates the data structure using a schema
* Checks state\_store to avoid reprocessing
* Applies dataset-specific transformations
* Saves final data as a Parquet file
* Uploads the file to HDFS using subprocess
* Logs each step
* Sends email alert if an error occurs

## 📦 Supported Input Formats

* CSV
* JSON
* TXT

You can extend the supported formats by adding extractors in `src/pipeline/extractors/`.

## 📄 Logging & Notifications

* Logs are written to `logs/etl.log`
* On failure:

  * Logs include full error details
  * Email alert is sent to the configured recipients (set in `notifier/email_notifier.py`)

## ✅ Run the ETL System

1. Install dependencies

```bash
pip install -r requirements.txt  
```

2. Start the ETL system

```bash
cd src/  
python main.py  
```

## 📬 Email Alerts

If the pipeline encounters any error:

* The exception is logged
* An email is automatically sent to the configured address with error details

## 📂 HDFS Integration

* Final DataFrames are saved as `.parquet` locally
* Files are uploaded to HDFS using a subprocess and `hdfs dfs -put` command
* Make sure Hadoop is installed and properly configured

## 👥 Contributors

Developed by 
**Ahmed Otifi** 
🔗 [https://github.com/otifi3](https://github.com/otifi3)
**Hania Hesham** 
🔗 [https://github.com/HaniaHesham99](https://github.com/HaniaHesham99)
**Mennatullah ?** 
🔗 [https://github.com/Mennatullahatta](https://github.com/Mennatullahatta)


---
