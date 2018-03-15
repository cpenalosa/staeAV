## AV Data Specification

The following provides the fields for the Autonomous Vehicle data types. All data needs to be in JSON with location data encoded in [GeoJSON](http://geojson.org/). 

### AV Data Types
The fields marked with an asterisk are already populated when you create the data source for your autonomous vehicle in Stae. 

| Field | Data type | Description | Validation | Example
| ---   | --- 		| ---         | ---		   | ---
|id*    | Text      | Represents a fully autonomous vehicle operating on a street. | Not empty | "Automated Vehicle"
|name*  | Text      | Descriptive name given to the vehicle by the operator. | Not empty | "AV Shuttle Test"
|type   | Text      | Categorization of the vehicle. |  Not empty, max character length: 2048 | "AV Shuttle Bus"
|notes* | Text 		| Description or further notes about the vehicle. | Not empty | "Initial pilot project for Shuttle Bus Services"
|operators| Array 	| List of agencies of people responsible for the vehicle. | Not empty, max character length: 2048 | ["Department of Trasnportation"]
|manufacturer| Text | Make/manufacturer of the vehicle. | Not empty, max character length: 2048 | "Ford"
|model  | Text 		| Model of the vehicle. | Not empty, max character length: 2048 | "Fusion"
|color  | Text 		| Color of the vehicle exterior. | Not empty, max character length: 2048 | "Shadow Black"
|vin | Number 	| Unique legal identification number for the vehicle. | Not empty, max character length: 2048 | "1ABCD23EFGHI456789"
|registered | Text 	| Jurisdiction the vehicle is registered in. | Not empty, max character length: 2048 | "Jersey City, NJ"
|plate | Number 	| Registered license plate code for the vehicle. | Not empty, max character length: 2048 | "ABC1234"
|active | Boolean 	| True/false if the vehicle is currently in service. | True/False | "True"
|heading | Number (degrees) 	| Direction the vehicle is pointing | Min: 0, Max: 360 | "175.45"
|speed 	| Number (KM/H) | Speed the UAS is currently going. | Min: 0, Max: 1000 | "5 KM/H" 
|images | Array 	| List of images related to the autonomous vehicle | Not empty, max character length: 2048 | [https://stae.co/AV1.jpg, https://stae.co/AV2.jpg]
|location | Point 	| Location where the autonomous vehicle exists. | GEOJSON format | {"type": "Point", "coordinates": [-74.0429, 40.744]}
