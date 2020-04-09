// Webdav-server
package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"

	"golang.org/x/net/webdav"
)

var mapL string //type Dir string

func main() {

	mapF := flag.String("m", "C:/webdav_test", "Map die gehost wordt") //mapF staat voor map Flag
	httpF := flag.Int("p", 80, "Luister port (HTTP)")                  //httpF staat voor http Flag

	flag.Parse() //verwerkt bovenstaande flags

	mapL = *mapF //Locatie van de map wordt van een pointer omgezet in een value en opgeslagen in mapL(Map Locatie)

	srv := &webdav.Handler{
		FileSystem: webdav.Dir(mapL),  //Dit is het virtuele bestand systeem, waar de map locatie wordt doorgegeven.
		LockSystem: webdav.NewMemLS(), //Update de lock waardes van alle bestanden in het lock management systeem.
		Logger: func(l *http.Request, err error) {
			if err != nil {
				log.Printf("WEBDAV ERROR %s [%s]: %s, ERROR: %s \n", l.Host, l.Method, l.URL, err) //Genereerd de volgende output in console :WEBDAV ip [HANDELING] ERROR!: locatie waar het fout is gegaan, bijv  C:\webdav_test\randombestand: wat de err is.
			} else {
				log.Printf("WEBDAV %s [%s]: %s  \n", l.Host, l.Method, l.URL) //Genereerd de volgende output in console: WEBDAV ip [HANDELING] locatie van de actie.
			}
		},
	}
	http.Handle("/", srv)
	if err := http.ListenAndServe(fmt.Sprintf(":%d", *httpF), nil); err != nil {
		log.Fatalf("De server is tegen het volgende probleem aangelopen: %v", err) //Kijkt of de port vrij is of dat er al een instantie draait en geeft dan een foutmelding waarna de server afgesloten wordt.
	}

}
