from datetime import datetime
import homework as lez

def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("hello", "hi", "ciao"):
        return "Ciao! Come butta?"

    if userMessage in ("come stai?", "come stai"):
        return "Alla grandissima."

    if userMessage in ("che si vinca"):
        return " o che si perda..... Forza Juve e Inter Merda"

    if userMessage in ("chi sei?", "chi sei"):
        return "Sono il tuo bot!  😄"

    if userMessage in ("gazzetta", "sport"):
        import feedparser
        NewsFeed = feedparser.parse("https://www.gazzetta.it/rss/home.xml")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return "www.gazzetta.it"

    if userMessage in ("time", "che ore sono?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(dateTime)

    if userMessage in ("news", "notizie"):
        import feedparser
        NewsFeed = feedparser.parse("http://www.ansa.it/sito/notizie/topnews/topnews_rss.xml")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return str("Nulla di nuovo")

    if userMessage in ("news audio", "news podcast"):
        import feedparser
        NewsFeed = feedparser.parse("https://feeds.transistor.fm/thevisionbriefing")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return str("Nulla di nuovo")


    if userMessage in ("juve", "juventus"):
        import feedparser
        NewsFeed = feedparser.parse("https://www.tuttojuve.com/rss")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return str("Nulla di nuovo")

    if userMessage in ("apple", "iphone"):
        import feedparser
        NewsFeed = feedparser.parse("https://feeds.feedburner.com/iphoneitalia")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)
        else:
            return str("Nulla di nuovo")


    if userMessage in ("hwupgrade", "tecnologia"):
        import feedparser
        NewsFeed = feedparser.parse("https://feeds.hwupgrade.it/rss_hwup.xml")
        entry = NewsFeed.entries[0]
        if entry.summary != " ":
            return str(entry.link)
        else:
            return str("Nulla di nuovo")

    if userMessage in ("carica lezione"):
        import pandas as pd

        #print("provo a caricare uno foglio di calcolo da drive")
        googleSheetId = '1Xf4kelhoKtDt5vEKMOiYJeCtf95mD4dpaRIjqPFYdjI'
        #print(googleSheetId)
        worksheetName = 'Foglio1'
        #print(worksheetName)
        URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            googleSheetId,
            worksheetName
        )
        #print(URL)
        df = pd.read_csv(URL, sep='\t')
        print(df)
        sql1 = lez.cancella_lezione();
        sql2 = lez.importa_lezione(df);


        return ("letto")

    return "Non ho capito."