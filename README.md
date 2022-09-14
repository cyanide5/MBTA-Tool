## Set up Instructions

---
1. In the terminal change to the project directory <br />```cd ../MBTA-Tool_FLASK```
2. Install the dependencies <br /> ```pip install -r requirements.txt```
3. Start the Flask Server ```python run.py```
---
### Usage:

Once the flask server is running navigate to the following in your browser of choice. 
```http://localhost:8080/MBTAtool/```
 <br />

What you are viewing here are the integrated docs generated using RestX in SwaggerUI.
<br />

Each endpoint can be run directly in the browser by clicking on ```Try It Out```
<br />

- ```/v1/all_routes/``` Takes No parameters and will return the 'ids' for all routes
- ```/v1/all_stops/``` Takes in a routeId (like the ones returned from the previous endpoint)
and returns all the associated stops for that route. 
[Note: the route id field IS case sensitive]