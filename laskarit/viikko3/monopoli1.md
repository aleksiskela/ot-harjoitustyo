classDiagram
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "2" Noppa
    Monopoli "1" -- "2...8" Pelaaja
    Pelaaja "1" -- "1" Pelinappula
    Pelilauta "1" *-- "40" Ruutu
    Pelinappula "0...8" -- "1" Ruutu
    class Ruutu{
        seuraavaRuutu()
    }