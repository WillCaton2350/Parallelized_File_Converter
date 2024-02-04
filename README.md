# PARALLEL ETL PROCESS
This program extracts CSV data from a multiline string, transforms that data into JSON using a Pandas DataFrame (the transformation process is parallelized), then loads the parallelized JSON data to the current directory, maps the ETL process to 'x' number of threads to achieve parallelism at runtime, and finally, instantiates and execute the program.
