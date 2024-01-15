#!/bin/bash

# Import GIT Diseases collection
mongoimport --host mongodb --db MedicalInfoDB --collection GIT\ Diseases --type json  --file /MedicalInfoDB/GIT\ Diseases.json --jsonArray

# Import Photos collection
mongoimport --host mongodb --db MedicalInfoDB --collection Photos --type json  --file /MedicalInfoDB/Photos.json --jsonArray

# Import Miscellaneous collection
mongoimport --host mongodb --db MedicalInfoDB --collection Miscellaneous --type json --file /MedicalInfoDB/Miscellaneous.json --jsonArray

# Import Pediatric Emergency collection
mongoimport --host mongodb --db MedicalInfoDB --collection Pediatric\ Emergency --type json --file /MedicalInfoDB/Pediatric\ Emergency.json --jsonArray

# Import Respiratory Diseases collection
mongoimport --host mongodb --db MedicalInfoDB --collection Respiratory\ Diseases --type json --file /MedicalInfoDB/Respiratory\ Diseases.json --jsonArray

# Import Urinary Tract Diseases collection
mongoimport --host mongodb --db MedicalInfoDB --collection Urinary\ Tract\ Diseases --type json --file /MedicalInfoDB/Urinary\ Tract\ Diseases.json --jsonArray
