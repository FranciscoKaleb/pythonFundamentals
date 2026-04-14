window.onload = loadRegions;
var regions = []

function loadRegions() {
    fetch("/regions")
    .then(res => res.json())
    .then(data => {

        regions = data

        const select = document.getElementById("region-select")

        data.forEach(r => {
            const option = document.createElement("option")
            option.value = r.region_id
            option.textContent = r.region_description
            select.appendChild(option)
        })

    })
}

function loadProvinces(){

    const region_id = document.getElementById("region-select").value

    fetch("/provinces")
    .then(res => res.json())
    .then(data => {

        const select = document.getElementById("province-select")
        select.innerHTML = ""

        data.forEach(p => {
            
            if(p.region_id == region_id){
                
                const option = document.createElement("option")
                option.value = p.province_id
                option.textContent = p.province_name

                select.appendChild(option)

            }

        })

    })
}

function loadMunicipalities(){

    const province_id = document.getElementById("province-select").value

    fetch("/municipalities")
    .then(res => res.json())
    .then(data => {

        const select = document.getElementById("municipality-select")
        select.innerHTML = ""

        data.forEach(m => {

            if(m.province_id == province_id){

                const option = document.createElement("option")
                option.value = m.municipality_id
                option.textContent = m.municipality_name

                select.appendChild(option)

            }

        })

    })
}


function loadBarangays(){

    const municipality_id = document.getElementById("municipality-select").value

    fetch("/barangays")
    .then(res => res.json())
    .then(data => {

        const select = document.getElementById("barangay-select")
        select.innerHTML = ""

        data.forEach(b => {

            if(b.municipality_id == municipality_id){

                const option = document.createElement("option")
                option.value = b.barangay_id
                option.textContent = b.barangay_name

                select.appendChild(option)

            }

        })

    })
}