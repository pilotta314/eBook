# Course Metadata Test

Prototyp für eine Kursvorlage mit Unterstützung bei Metadaten und Lizenzen.

* generiert Metadaten in HTML-Header für OER Repositories and Google Search
* ergänzt Lizenzhinweise nach TULLU-Regel für Wikimedia-Bilder automatisch
* fügt Lizenzhinweis in generierte Dokumente ein

Mit CI werden die folgenden Dokumente generiert

* [course.epub](https://tibhannover.gitlab.io/oer/course-metadata-test/course.epub)
* [course.pdf](https://tibhannover.gitlab.io/oer/course-metadata-test/course.pdf)
* [course.asc](https://tibhannover.gitlab.io/oer/course-metadata-test/course.asc)
* [course.html](https://tibhannover.gitlab.io/oer/course-metadata-test/index.html)

# Nachnutzung

Dieses Projekt als Vorlage für eigene Kurse verwenden.

* dieses Repository auf GitLab clonen
* metadata.yml anpassen
    * manuell
    * mit [Metadaten-Generator](https://tibhannover.gitlab.io/oer/course-metadata-gitlab-form/metadata-generator.html) // UNDER CONSTRUCTION!
* course.md anpassen
* Links in der README.md anpassen

Beim ersten Durchlauf kann es bis zu ca. 15min dauern, bis die Dateien generiert sind. Weitere Änderungen stehen i.d.R. nach <1min bereit.