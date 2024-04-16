The purpose of this code is to process Streamsets workflows in json format and amend the HDFS targets within them to ECS instead.
The output workflows are to be re-imported into the Streamsets UI.
To run the code after inputing general info such as access + secret key values, jceks file location and lastly, s3 bucket name, simply run the process_streamsets.py file in an IDE and it should output the amended workflows. 
Recommended IDE to use is IntelliJ.
