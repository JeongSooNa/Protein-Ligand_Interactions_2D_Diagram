# Protein-Ligand_Interactions_2D_Diagram

Draw Protein Ligand Interactions 2D diagram Using Protein Plus poseview API (ZBH - Center for Bioinformatics)

JeongSoo Na

Create At : 2024.06.25

Update At : 2024.06.25

---

### Installization

### Usage

- run main.py
```sh
python main.py --pdb test.pdb --lig UNK_A_0 --output_dir 2d_diagram/
```


# REST API Usage Documentation : PoseView : 2D-Interaction diagrams

#### Create PoseView Job
Creates a new PoseView job passing json data in body and returns json data about the location of the results.

- URL

    https://proteins.plus/api/poseview_rest

- Method:

    POST

- URL Params

    None

- Data Params
- Required:
```
poseview=[hash] - Contains the following parameters:

pdbCode=[string] - Select a structure form the Protein Data Bank (PDB) via its PDB code.

ligand=[string] - Set a ligand with respect to specified pdbCode or "".
```

- Success Response:
    - Code: 200  
    Content: ```{ status_code: 200, location: "", message: "Job already exists" }```

        OR
    - Code: 202  
    Content: ```{ status_code: 202, message: "The job will be created in the specified location", location: "" }```

        OR
    - Code: 202  
    Content: ```{ status_code: 202, message: "Job exists and is still in 'processing' state", location: "" }```

- Error Response:
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Parameter values must be strings" }```
        
        OR
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Invalid number of parameters or incorrect parameter name" }```
    
        OR
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Invalid pdbCode" }```
    
        OR
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Invalid ligand" }```
    
        OR
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Job saving error" }```
    
        OR
    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Job loading error" }```
    
        OR
    - Code: 429 TOO MANY REQUESTS
    Content: ```{ status_code: 429, error: "Too Many Requests", message: "Throttle limit reached. Retry later." }```

- Sample Data:
```
    {
        "poseview": {
            "pdbCode":"1kzk",
            "ligand":"JE2_A_701"}
    }
```

- Sample Call (curl):
```
    curl -d '{"poseview": {"pdbCode":"1kzk","ligand":"JE2_A_701"}}' -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://proteins.plus/api/poseview_rest
```

#### Show PoseView Job
Returns json data about a single PoseView job.

- URL

    https://proteins.plus/api/poseview_rest/:id

- Method:

    GET

- URL Params  

- Required:
```
id=[string]
```

- Data Params

    None

- Success Response:

    - Code: 200  
    Content: ```{ status_code: 200, result_png_picture: "", result_pdf_picture: "", result_svg_picture: "" }```
    
        OR
    - Code: 202  
    Content: ```{ status_code: 202, message: "Job exists and is still in 'processing' state", location: "" }```

- Error Response:

    - Code: 400 BAD REQUEST
    Content: ```{ status_code: 400, error: "Bad Request", message: "Job loading error" }```
    
        OR
    - Code: 404 NOT FOUND
    Content: ```{ status_code: 404, error: "Not Found", message: "Invalid ID" }```
    
        OR
    - Code: 429 TOO MANY REQUESTS
    Content: ```{ status_code: 429, error: "Too Many Requests", message: "Throttle limit reached. Retry later." }```

- Sample Call (curl):
```
    curl https://proteins.plus/api/poseview_rest/ixenp5kLNHohrRbj56fbt4dd
```

- Output:
```
result_png_picture - 2D-diagram of protein-ligand interactions (PNG-file)

result_pdf_picture - 2D-diagram of protein-ligand interactions (PDF-file)

result_svg_picture - 2D-diagram of protein-ligand interactions (SVG-file)
```

---

### Reference

[Protein-Plus REST API service](https://proteins.plus/help/index#REST-help)

API requests can be sent with the command line tool curl or with a browser rest client plugin. The API allows the user to create jobs for the respective tools with the HTTP method POST, each requiring a different set of parameters.
Calculation results can then be accessed and downloaded with the HTTP method GET. The base url for current version (v1) is https://proteins.plus/api.
For performance and security reasons, the API endpoints are subject to rate limiting (30 jobs/minute). Inidividual rate limits for some of the tools with heavy CPU/RAM usage do exist (e.g., for DoGSiteScorer). Please consider using the offline versions of the tools in case you need higher throughput (Software Server ZBH). Exceeding the limit, a HTTP status code 429 with the message "Throttle limit reached. Retry later" will be sent.
Custom PDBs can be used in order to create tool jobs. These PDBs have to be added priorly: