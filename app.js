let main = document.getElementById("main")

async function getSalary(){
  await fetch("jobsal.json").then((response)=>{
    response.json().then((sal)=>{
      let mediaSalarial = sal[0]["Media salárial"]
      let qtdSal = sal[0]["Quantidade de Salario Reportado"]
      let tituloSal = sal[0].Title
      
      main.innerHTML = `<h1 id="tituloDaPagina">${tituloSal}</h1>
                      <div class="container-salario">
                          <div class="square1" id="mediaSal">
                              <h5>Media Salarial</h5>
                              <p>${mediaSalarial}</p>
                          </div>
                          <div class="square2" id="qtdSal">
                              <h5>Numero de salario reportados</h5>
                              <p>${qtdSal}</p>
                          </div>
                      </div>`
    })
  })
}

async function getJobs(){
  await fetch("jobs.json").then((response)=>{
    response.json().then((jobs)=>{
      for(let i=0;i<jobs.length;i++){

        let titulo = jobs[i].title
        let subtitle = jobs[i].location
        let description = jobs[i].description
        if (subtitle == "Qualquer lugar"){
            subtitle = "Remoto"
        }else{
            subtitle = jobs[i].location
        }
        card = `<ul><li><div class="card cover key=${i}">
                            <div class="card-body">
                                <h5 class="card-title">${titulo}</h5>
                                <h6 class="card-subtitle mb-2 text-muted">${subtitle}</h6>
                                <a href="#" class="card-link">Ler a desrição completa  </a>
                                <p class="card-text overflow-y-hidden">${description}</p>
                            </div>
                        </div></li></ul>`
        main.innerHTML += card
      }
      card = document.querySelectorAll(".card")

      card.forEach(function(cards){
        cards.addEventListener('click', function(){
          cards.classList.toggle("cover")
        })
      })
    })
  })
}

async function allContent(){
  await getSalary()
  await getJobs()
}