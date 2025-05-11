from etl.pipeline.logger.logger import Logger
from etl.pipeline.pipeline import Pipeline  
from etl.file_monitor.file_monitor import FileMonitor 

def main():
    # Set up logging file path
    log_file = "/path/to/logfile.log"  # Set the log file path
    logger = Logger(log_file)  # Instantiate the Logger with the file path

    # Instantiate your pipeline with the logger
    pipeline = Pipeline(logger)

    # Create an instance of the FileMonitor with the pipeline and directory path
    file_monitor = FileMonitor(pipeline, base_dir="/path/to/data")

    # Start the file monitor to continuously check for new files and process them
    file_monitor.start()

if __name__ == "__main__":
    main()
