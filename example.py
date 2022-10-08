import bcpscrapper as bcp

path = 'example.json'
writer = bcp.DocxWriter(path)
code = writer.createDocument('output')