import csv
import datetime
import pg8000

databaseName        = "csvBase"
databaseUser        = "postgres"
databasePassword    = "postgres"
databaseTableName   = "NewsArticle"
fileName            = "nieuws.csv"

class NewsArticle:
    def __init__(self, title: str, subtitle: str, datePublished: [str, str, str], article: str):
        self.title = title
        self.subtitle = subtitle
        self.article = article
        self.datePublished = datetime.datetime(
            int("20" + datePublished[2]), 
            int(datePublished[1]), 
            int(datePublished[0])
        )

    def toQuery(self, tableName: str) -> str:
        return "INSERT INTO {0} (Title, Subtitle, DatePublished, Article) VALUES ('{1}', '{2}', '{3}', '{4}')".format(
            tableName,
            self.title, 
            self.subtitle, 
            self.datePublished.strftime('%Y-%m-%d'), 
            self.article
        )


databaseConnection  = pg8000.connect(
                        user = databaseUser, 
                        password = databasePassword, 
                        database = databaseName
                    )
                    
databaseCursor      = databaseConnection.cursor()
dataList            = []

with open(fileName, newline = '\n') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ';')

    for row in csvReader:
        title, subtitle, datePublished, article = row
        dataList.append(NewsArticle(title, subtitle, datePublished.split('-'), article))

for dataObject in dataList:
    databaseCursor.execute(dataObject.toQuery(databaseTableName), ())

databaseConnection.commit()
databaseConnection.close()