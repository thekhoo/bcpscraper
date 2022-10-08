import bcpscrapper as bcp

path = 'topics.json'
writer = bcp.DocxWriter(path)
code = writer.createDocument('output')