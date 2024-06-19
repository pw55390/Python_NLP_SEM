Instrukcja: 
w systemie powinny znajdować się biblioteki*: 
- PyTorch (wersja 2.3.1) - pip install torch
- transformers (wersja 4.41.2) - pip install transformers
- scikit-learn ( wersja 1.2.2) - pip install scikit-learn
- googletrans ( wersja 4.0.0) - pip install googletrans 
- tkinter - pip install tk


Aplikacje można uruchamić za pomocą skryptu main.py.Do użytkowania aplikacji konieczne jest połączenie z siecią Internet. 

1 ) uruchomić main.py - z poziomu konsoli w folderze głównym projektu: python main.py
2 ) UWAGA: Pierwsze uruchomienie aplikacji rozpocznie pobieranie modelu językowego, a następnie jego instalację. To może chwilę potrwać. 
Kolejne uruchomienia aplikacji będą bez porównania sprawniejsze.

Używanie aplikacji: 

 - do okienka GUI można wkleić teraz dowolny tekst w języku angielskim - aplikacja dokona jego analizy (przycisk PROCESS) i wypisze krótkie podsumowanie. 
Następnie aplikacja w pamięci przetłumaczy tekst na język polski i na podstawie własnego modelu językowego 
dokona próby klasyfikacji tego tekstu ze względu na kategorie: /bajka,biografia,fantastyka,horror,nauka,proza/romans,reportaż,kryminał/

- w katalogu głównym znajduje się plik pattern.txt zawierający tekst w języku angielskim. Można wkleić do niego dowolny inny angielski tekst, który będzie analizowany 
przy starcie aplikacji oraz wyświetlany w okienku GUI

- przykładowe teksty do wklejenia, które mogą ułatwić weryfikację działania aplikacji, znajdują się w folderze /przykladowe_teksty

*biblioteki do zaintalowania znajdują się także w pliku: requirements.txt ( pip install -r requirements.txt ) 