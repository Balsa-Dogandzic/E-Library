function borrowBook(){

    var trazena_knjiga = document.getElementById("book-title").value;
    var autor_knjige = document.getElementById("author-name").value;

    var knjige = [
        { naziv: "Where the Crawdads Sing", autor: "Delia Owens", dostupneKnjige: 27, tipSadrzaja: "Tvrde korice"},
        { naziv: "Too Much and Never Enough", autor: "Mary L. Trump", dostupneKnjige: 14, tipSadrzaja: "Tvrde korice | PDF"},
        { naziv: "Midnight Sun", autor: "Stephenie Meyer", dostupneKnjige: 34, tipSadrzaja: "Tvrde korice"},
        { naziv: "Untamed", autor: "Glennon Doyle", dostupneKnjige: 17, tipSadrzaja: "Tvrde korice | PDF"},
        { naziv: "Becoming", autor: "Michelle Obama", dostupneKnjige: 35, tipSadrzaja: "Tvrde korice | PDF"},
        { naziv: "A Promised Land", autor: "Barack Obama", dostupneKnjige: 76, tipSadrzaja: "Tvrde korice"}
      ];

    var noviBrojKnjiga = 0;
    var element = document.getElementById("broj_knjiga-1").value;

      for (var i = 0; i < knjige.length; i++) {
        var knjiga = knjige[i];
        if (knjiga.naziv === trazena_knjiga && knjiga.autor === autor_knjige) {
          noviBrojKnjiga = knjiga.dostupneKnjige - 1;
          element.innerHTML = noviBrojKnjiga + " knjiga dostupno.";
          console.log(knjiga.dostupneKnjige)
          break;
        }
      }

}