# Vorlage für OER-Kurse

Prototyp für eine Kursvorlage mit Unterstützung bei Metadaten und Lizenzen. Die Vorlage kann auch für andere Text, wie z.B. Studien- oder Masterarbeiten verwendet werden.

* generiert Metadaten in HTML-Header für OER Repositories and Google Search
* ergänzt Lizenzhinweise nach TULLU-Regel für Wikimedia-Bilder automatisch
* fügt Lizenzhinweis in generierte Dokumente ein

Mit CI werden die folgenden Dokumente generiert

* [Kurs als Ebook](https://tibhannover.gitlab.io/oer/course-metadata-test/course.epub)
* [Kurs als PDF](https://tibhannover.gitlab.io/oer/course-metadata-test/course.pdf)
* [Kurs als HTML](https://tibhannover.gitlab.io/oer/course-metadata-test/index.html)

# Nachnutzung

Dieses Projekt als Vorlage für eigene Kurse verwenden.

* dieses Repository auf GitLab clonen
* metadata.yml anpassen
    * manuell
    * mit [Metadaten-Generator](https://tibhannover.gitlab.io/oer/course-metadata-gitlab-form/metadata-generator.html) // UNDER CONSTRUCTION!
* course.md anpassen
* Links in der README.md anpassen

Beim ersten Durchlauf kann es bis zu ca. 15min dauern, bis die Dateien generiert sind. Weitere Änderungen stehen i.d.R. nach <1min bereit.

# Auffindbar machen

Wenn der Kurs die ersten erkennbaren Inhalte enthält, kann er auf einem der Landesportale veröffentlicht werden.

* [Niedersachsen](http://service.tib.eu/edu-sharing/components/search) oder Projekt-URL per [Mail](mailto:support.oer-nds@tib.eu)
* [Baden-Württemberg](https://www.oerbw.de/edu-sharing/components/search)
* ...

# Updates

* 2019-10-28 - Automatische TULLU-Regel für Wikimedia Bilder
* 2019-10-28 - Automatischer Lizenzhinweis auf Basis der Metadaten in metadata.yml
