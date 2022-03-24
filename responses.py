from datetime import datetime

def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("hello", "hi", "Ciao", "ciao"):
        return "Ciao! Come butta?"

    if userMessage in ("come stai?", "Come stai?", "come stai", "Come stai"):
        return "Alla grandissima."

    if userMessage in ("che si vinca", " Che si vinca"):
        return " o che si perda..... Forza Juve e Inter Merda"

    if userMessage in ("chi sei?", "Chi sei?", "chi sei", "Chi sei"):
        return "Sono il tuo bot!  😄"

    if userMessage in ("gazzetta", "Gazzetta", "sport", "Sport"):
        import feedparser
        NewsFeed = feedparser.parse("https://www.gazzetta.it/rss/home.xml")
        entry = NewsFeed.entries[1]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return "www.gazzetta.it"

    if userMessage in ("time", "Che ore sono","che ore sono?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(dateTime)

    if userMessage in ("news", "News", "Notizie", "notizie"):
        import feedparser
        NewsFeed = feedparser.parse("http://www.ansa.it/sito/notizie/topnews/topnews_rss.xml")
        entry = NewsFeed.entries[1]
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


    if userMessage in ("juve", "Juve", "Juventus", "juventus"):
        import feedparser
        NewsFeed = feedparser.parse("https://www.tuttojuve.com/rss")
        entry = NewsFeed.entries[1]
        if entry.summary != " ":
            return str(entry.link)

        else:
            return str("Nulla di nuovo")

    if userMessage in ("apple", "Apple", "Iphone", "iphone"):
        import feedparser
        NewsFeed = feedparser.parse("https://feeds.feedburner.com/iphoneitalia")
        entry = NewsFeed.entries[1]
        if entry.summary != " ":
            return str(entry.link)
        else:
            return str("Nulla di nuovo")


    if userMessage in ("hwupgrade", "Hwupgrade", "Tecnologia", "tecnologia"):
        import feedparser
        NewsFeed = feedparser.parse("https://feeds.hwupgrade.it/rss_hwup.xml")
        entry = NewsFeed.entries[1]
        if entry.summary != " ":
            return str(entry.link)
        else:
            return str("Nulla di nuovo")

    return "Non ho capito."