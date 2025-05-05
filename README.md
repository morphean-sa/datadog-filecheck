# Archive Notice

## Important: This repository has been archived

**As of 5 May 2025,** `datadog-filecheck` is no longer actively maintained.

### Why is this repository being archived?

We have moved our monitoring and observability infrastructure from Datadog to the Grafana stack.
The code remains available for historical reference.

### What this means for you

* **Read‑only:** Issues and pull requests are frozen.  
* **No further releases or security updates** will be published.  

> Using this project in production after archival is at your own risk.
>

# datadog-filecheck

a datadog custom check to verify if a file exists and its last modification

returns a check:

* filecheck.exists

and 2 metrics:

1. filecheck.modified : the timestamp of the last modification
2. filecheck.age : the delta between now and the last modification (in second)
