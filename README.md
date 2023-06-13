# FlaskWebApp

Pokretanje aplikacije:

1. Kreiranje okruzenja:

- python -m venv env

2. Aktiviranje okruzenja

- env\Scripts\activate

3. Instalacija biblioteka (flask, flask_mysqldb)

- pip install -r requirements.txt

4. Importovanje SQL fajla u phpMyAdmin
5. Pokretanje app.py fajla

# TODO

Sve knjige:

- Ima tabelu sa svim knjigama i linkovima do njih
- Ima dugme koje otvara formu za dodavanje knjiga (ja cu mu dodat putanju ti ga samo stilizuj)

Pojedinacna knjiga:

- Ima informacije o jednoj knjizi
- Ima dva dugmeta update i delete
- Update dugme vodi na formu za modifikovanje knjige
- Delete dugme bi valjalo da otvara modal prozor kao upozorenje (ima opcije obrisi, i otkazi)

Forme za dodavanje i modifikovanje knjiga:

- Iste su, samo mozes jednu zavrsiti

Sta je meni ostalo da uradim:

- Rezervacije korisnika (bibliotekar ima prikaz svih rezervacija, dok obicni korisnik vidi samo svoje)
- Forma za rezervisanje knjiga
- Autorizacija (ne smije svako da brise i modifikuje bazu podataka)
