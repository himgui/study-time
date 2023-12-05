email_tmpl = """
Hello, %(name)s

Are you interested in playing for %(team)s?

Click now on this %(link)s

This opportunity will give you %(text)s

We have only %(spots)d available!

Current Price is %(price).2f
"""
clients = ["Abel","Endrick","Dudu","Veiga"]

for client in clients:
    print(
        email_tmpl
        % {
            "name": client,
            "team": "Palmeiras",
            "text": "a lot of titles",
            "link": "palmeiras.com.br",
            "spots": 5,
            "price": 100.5,
        }
    )