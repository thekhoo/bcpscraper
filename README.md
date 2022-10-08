# Blackstone's Criminal Procedure 2022 PDF Scraper

**IMPORTANT:** This is a tool that helps with scraping PDF files for Blackstone's Criminal Proedure 2022 downloaded from LexisLibrary. It will **NOT** work if you don't have the PDF files beforehand.

## Introduction

This is a mini project and my first attempt at writing a package and pushing it to Github and PyPi. Aside from helping my friend with a quicker way to copy from the law document, I used this as an opportunity to practice version control, sharpen my understanding of regex and pattern recognition, understanding how to write and publish packages on PyPi and practice good documentation behaviour.

This package is designed to get all the sections and subsections from Blackstone's Criminal Practice 2022 Documents based on the input in a JSON file. All the text will then be formatted appropriately and exported in a word document (.docx) per the structure described in that initial JSON file.

TL;DR - A tool to extract subsections as required from Blackstone's Criminal Practice 2022 from Lexis Library into a word document.

> **NOTE:** This program was designed purely for Part D of the Blackstone's Criminal Practice 2022 Document from Lexis Library. 

> **Update 06/10/22:** The program seems to work fine on Parts D, E, F and R from Blackstone's Criminal Practice 2022 from Lexis Library.

## How to use the tool

1. Use pip to install the package as follows.

    ```console
    pip install bcpscraper
    ```

2. Create a folder called `data` that contains all the PDF files. These files should be named according to their section *(i.e. D5.pdf OR E14.pdf)*
> For more information, refer to the "PDF File Naming Convention" section below.

3. Create a JSON file with the structure below so the program knows which sections and subsections to extract and how to organise them in the word document. This is the instruction file that is read by the program.

    ```js
    // All text with angle brackets <> are variables and can be named according to preference.
    // All other text are constants that are used as keys throughout the program.

    {
        "doc_title": "",    // This is the title of the .docx file that will be created.

        "doc_data": {       // This is the data that the program should look for.

            // Start of a Topic
            "<topic_name>" : {        // This is the start of a topic. There can be as many topics as you want within this JSON file.

                "title": "",            // The title of this topic.
                "sections": {           // The sections and subsections that the progrma should look for

                    // The keys here are actually variables but I've displayed them as text as an example situation.

                    "D5": [1,2,3,4,5],           // Use a list for the subsections within that particular section 
                    "D9": [2,3,4,5,6,7,8]        // Example: D5.1 - D5.5 and D9.2 - D9.8
                    .
                    .
                    .
                }
            }
            // End of a Topic
            .
            .
            .
        }
    }
    ```

4. Import bcpscraper into your project.
    ```py
    import bcpscraper as bcp
    ```

5. Specify the path of the JSON file when creating the bcp DocxWriter object.
    ```py
    writer = bcp.DocxWriter('example.json')
    ```

6. Use the function `createDocument(folder)` to create the document. The parameter `folder` is the directory that the word file will be exported to.
    ```py
    writer.createDocument('output')     # This stores it in the output folder
    ```

An overall example of how this would look like in your code would be:

```py
import bcpscrapper as bcp

path = 'example.json'
writer = bcp.DocxWriter(path)
code = writer.createDocument('output')
```

This is shown in `example.py` and `example.json`.

## PDF File Naming Convention

Name the PDF file based on the Part and Section that it belongs to. For example:

*Part D5 - Starting a Prosecution and Preliminary Proceedings in Magistrates' Court should be named as **D5.pdf**.*

The file should be saved in a folder called `data`.

## Future Work

1. Different log category classifications.
2. Introduce tests in the code.

## Documentation

Check out the [code documentation wiki page](https://github.com/thekhoo/bcpscraper/wiki/Code-Documentation) for the official documentation.
