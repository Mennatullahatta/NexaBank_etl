# NexaBank ETL Pipeline

This project implements a scalable, modular ETL pipeline designed for banking and transactional data. It uses a multithreaded producer-consumer pattern to monitor new data files, validate them, transform the data, and load it efficiently into a data lake in Parquet format and HDFS.

## 📚 Table of Contents

* [🚀 Key Features](#-key-features)
* [🧠 Architecture Overview](#-architecture-overview)
* [📁 Project Structure](#-project-structure)
* [🛠️ How It Works](#️-how-it-works)
* [📦 Supported Input Formats](#-supported-input-formats)
* [📄 Logging & Notifications](#-logging--notifications)
* [📬 Email Alerts](#-email-alerts)
* [📂 HDFS Integration](#-hdfs-integration)
* [✅ Run the ETL System](#-run-the-etl-system)
* [👥 Contributors](#-contributors)

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


Thanks for the screenshot! I see the tree structure is getting messy with long comments in a single line. To improve readability and make it look neat in the README, you can:

* Use **indented multiline comments** instead of inline comments.
* Avoid wrapping long comments on the same line with the file or folder name.
* Use bullet points or a description list style after the tree structure.

Here is a cleaned-up, clear and well-formatted version that looks good in Markdown README:



## 📁 Project Structure

```
src/
├── main.py
├── file_monitor/
│   └── file_monitor.py
├── pipeline/
│   ├── pipeline.py
│   ├── extractors/
│   │   ├── csv_extractor.py
│   │   ├── json_extractor.py
│   │   └── txt_extractor.py
│   ├── validators/
│   │   └── schema_validator.py
│   ├── transformers/
│   │   ├── customer_transformers.py
│   │   ├── credit_transformers.py
│   │   ├── loans_transformers.py
│   │   ├── money_transfers_transformers.py
│   │   └── support_transformers.py
│   ├── loaders/
│   │   ├── parquet_loader.py
│   │   └── hdfs_loader.py
│   ├── logger/
│   │   └── logger.py
│   ├── notifier/
│   │   └── email_notifier.py
│   ├── state_store/
│   │   └── state.py
│   └── support/
│       ├── schemas.json
│       └── english_words.txt
```




### Descriptions:

- **main.py**  
  Entry point: creates a Pipeline instance, passes it to FileMonitor, and starts monitoring.

- **file_monitor/file_monitor.py**  
  Implements FileMonitor which monitors directories, queues new files, and feeds them into the pipeline via a producer-consumer pattern.

- **pipeline/pipeline.py**  
  Core controller that orchestrates ETL stages: extraction, validation, filtering, transformation, loading, and error handling.

- **pipeline/extractors/**  
  Extractor classes for different file types:  
  - `csv_extractor.py`: reads CSV files  
  - `json_extractor.py`: reads JSON files  
  - `txt_extractor.py`: reads delimited TXT files

- **pipeline/validators/schema_validator.py**  
  Validates input data against JSON schemas.

- **pipeline/transformers/**  
  Dataset-specific transformation logic for customers, credits, loans, money transfers, and support tickets.

- **pipeline/loaders/**  
  Responsible for writing output data:  
  - `parquet_loader.py`: saves DataFrames as local Parquet files in `/tmp`  
  - `hdfs_loader.py`: uploads Parquet files to HDFS compatible with Hive external tables

- **pipeline/logger/logger.py**  
  Custom logger writing detailed logs to `./logs/etl.log`.

- **pipeline/notifier/email_notifier.py**  
  Sends email notifications via SMTP (Gmail) on pipeline failures.

- **pipeline/state_store/state.py**  
  Tracks already processed records to avoid duplication.

- **pipeline/support/**  
  Helper files including:  
  - `schemas.json`: JSON schemas for validation  
  - `english_words.txt`: Wordlist used for brute-force decryption in loans transformation







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


## 📬 Email Alerts

If the pipeline encounters any error:

* The exception is logged
* An email is automatically sent to the configured address with error details

## 📂 HDFS Integration

- Final DataFrames are first saved locally as `.parquet` using a **ParquetLoader** class, typically into a temporary directory.
- The **HdfsLoader** class then moves these files into HDFS using a `subprocess` call with the `hdfs dfs -put` command.
- The target HDFS directory is configured to align with **Hive external tables**, enabling direct querying from Hive.
- Ensure Hadoop is installed and properly configured in the environment for successful upload and Hive integration.

  ## ✅ Run the ETL System

1. **Start the services using Docker Compose**

   ```bash
   docker-compose up -d
   ```

2. **Access the `etl_py` container**

   ```bash
   docker exec -it etl_py bash
   ```

3. **Run the ETL process**

   ```bash
   cd src/
   python main.py
   ```


## 👥 Contributors

- **Ahmed Otifi** 🔗 [https://github.com/otifi3](https://github.com/otifi3)  
- **Hania Hesham** 🔗 [https://github.com/HaniaHesham99](https://github.com/HaniaHesham99)  
- **Mennatullah** 🔗 [https://github.com/Mennatullahatta](https://github.com/Mennatullahatta)

