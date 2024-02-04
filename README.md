# PARALLEL ETL PROCESS
The program extracts CSV data from a multiline string, transforms it into JSON using a Pandas DataFrame (the transformation process is parallelized), then loads the parallelized JSON data to the current directory. It maps the ETL process to a number of threads to achieve parallelism at runtime then instantiates and executes the program.
