from datetime import datetime

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
        print("provo a caricare uno foglio di calcolo da drive")
        #1wKHi17BEEkTiHOtzvzeiJru_UCldtv4rYYnON2DusRA
        import pandas as pd
        sheet_id = “1wKHi17BEEkTiHOtzvzeiJru_UCldtv4rYYnON2DusRA"
        sheet_name = “Foglio1”
        url = f”https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        pd.read_csv(url)
        print(pd)
        return ("letto")

    return "Non ho capito."