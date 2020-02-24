
# Remote Method Invocation (RMI) with Python

-	Pyro4 is a Python package developed to support RMI in Python, and we will develop different applications. 
- Pyro can be used to distribute and integrate various kinds of resources or responsibilities including computational (hardware) resources (CPU, storage, printers), informational resources (data, privileged information) and business logic (departments, domains).
- Pyro enables code to call methods on objects even if that object is running on a remote machine


# Developing a Load Balancer with RMI

- A server that will perform a simple operation, e.g. count how many times a number exists in the dataset.
- We will launch a nameserver
- We will replicate the server and will run it as a different instance of the counter.
  For the sake of testing our servers, we will provide log messages, to monitor which server used each time.
- A load balancer to distribute requests to our two server instances.
  A round robin load balancer forwards a client request to each server in turn. When it reaches the end of the list, the load balancer loops back and goes down the list again.
- Two clients to connect to the load balancer and test the requests.
