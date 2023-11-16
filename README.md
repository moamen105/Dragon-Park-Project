# Dragon Park Maintenance System
Welcome to the Dragon Park Maintenance System! This system is designed to help manage the maintenance and safety of Dragon Park facilities efficiently.

# How to Set Up and Run the Code
Prerequisites
Python (version 3.x recommended)
Flask (install via pip install Flask)
SQLite (usually comes with Python installations)

# Steps : 
Clone the Repository
Set Up Virtual Environment
Install Dependencies
Run the Flask Application
Your Flask application will be running at http://127.0.0.1:5000/ by default.



# Documentation of the API

API Endpoints

GET /:
Returns a greeting message.

GET /about:
Returns information about the project.

GET /zones:
Returns a list of all zones and their statuses.

GET /zones/:zoneId:
Returns details for a specific zone.

POST /nudls-webhook:
Simulates processing NUDLS™ webhook events.


# Technical Questions

1. Uptime Guarantee (99.99%)
To achieve a 99.99% uptime guarantee, the following strategies are implemented:

- Use a reliable hosting service with a history of high availability.
- Implement redundancy and failover mechanisms to handle server failures.
- Regularly monitor and log application performance, setting up alerts for potential issues.
- Deploy updates during low-traffic periods to minimize disruptions.

2. Handling Scale for 1 Million Dragons
To handle a significant increase in scale (1 million dragons), consider the following:

- Optimize database queries and indexing for efficient data retrieval.
- Use a more scalable database solution (e.g., PostgreSQL) if needed.
- Implement caching mechanisms for frequently accessed data.
- Use load balancing and auto-scaling for the web server to distribute traffic.
- Consider asynchronous processing for resource-intensive tasks.
