## `class` DocxWriter(data)

* **data : dict**
*The JSON data found in the JSON File.*

This class handles:
* Creation of `ProcedurePDF` Objects
* Creation of `Topic` Objects
* Writing the data into a Word document (.docx)

### 🔸 .doc
```py
DocxWriter.doc -> Document()
```

The document object from the `docx` module that will handle writing the document into a word file.

### 🔸 .doc_title
```py
DocxWriter.doc_title -> str
```

The title that the document will be saved as. Reference from the JSON file using the key `doc_title`.

### 🔸 .doc_data
```py
DocxWriter.doc_data -> dict
```

The dictionary of all the topics and their respective sections and subsections that should be extracted for this document.

```py
dict({
     "Topic 1" : dict({
          "title": : "",
          "sections": : dict({
               "[section]" : [subsections]
               .
               .
               .
          })
     })
     .
     .
     .
})
```

### 🔸 .topics
```py
DocxWriter.topics -> List[Topic]
```

List of Topic objects for the document.

### 🔸 .pdfs
```py
DocxWriter.pdfs -> List[ProcedurePDF]
```

List of ProcedurePDF objects that are required for the document.

### 🔹 .createDocument()
```py
DocxWriter.createDocument(
     folder : str

) -> int
```

* **folder : str**
*The folder where the word document will be saved.*

Creates the word file document (.docx) and saves it in the specified folder. Returns an integer that signifies the return code on whether the code ran successfully or if any errors are present.

### 🔹 ._getJSONData()
```py
DocxWriter._getJSONData() -> dict
```

Takes the file path given to the object and gets the JSON file. The JSON data is then converted into a dictionary.

Returns this dictionary:
```py
dict({
    "doc_title": "<doc_title>",
    "doc_data": dict({
            "[topic]" : dict({
                "title": "<title>",
                "sections": dict({
                    "<subsection>": [20,21]
            })
        })
    })
})
```

### 🔹 ._writeTopicData()
```py
DocxWriter._writeTopicData(
     topic : Topic

) -> int
```

* **topic : Topic**
*The Topic object created from the JSON file.*

Writes the data of the topic to the document.

### 🔹 ._getTopicsAndPDFs()
```py
DocxWriter._getTopicsAndPDFs() -> int
```

Gets an array of Topic and ProcedurePDF objects to fill the pdfs and topics property of this class.

### 🔹 ._getPDFObjects()
```py
DocxWriter._getPDFObjects() -> int
```

Gets an array of ProcedurePDF objects to fill the pdfs property of this class.
