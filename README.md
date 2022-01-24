# datadog-filecheck

a datadog custom check to verify if a file exists and its last modification

returns a check:

* filecheck.exists

and 2 metrics:

1. filecheck.modified : the timestamp of the last modification 
2. filecheck.age : the delta between now and the last modification (in second)